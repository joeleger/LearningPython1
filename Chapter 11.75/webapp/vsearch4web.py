import os
from time import sleep
from threading import Thread
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in
from flask import Flask, render_template, request, session, copy_current_request_context
from vsearch import search4letters

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


app.secret_key = os.urandom(16)


@app.route('/logout')
def do_logout() -> str:
    if 'logged_in' in session:
        session.pop('logged_in')
        return 'You are now logged out'
    else:
        return 'You were never logged in'


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """Log details of the web request and the results."""
        sleep(15)  # This makes log_request really slow...
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
                    (phrase, letters, ip, browser_string, results)
                    values
                    (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form[r'letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res,))
    title = "Here are your results:"
    phrase = request.form['phrase']
    letters = request.form['letters']

    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request,args=(request, results))
        t.start()

    except Exception as err:
        print("*******Something went wrong!!", str(err))
    except ConnectionError() as err:
        print("Is your database switched on? Error:", str(err))
    except CredentialsError as err:
        print("User-id/Password issues. Error:", str(err))
    return render_template("results.html",
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    """Display the contents of the log table as an HTML table"""
    try:

        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results
            from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
            titles = ('Phrase', 'Letters', 'Remote address', 'User agent', 'Results')
            return render_template('viewlog.html',
                                   the_title='View Log',
                                   the_row_titles=titles,
                                   the_data=contents,
                                   )
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'Error'


if __name__ == '__main__':
    app.run(debug=True)
