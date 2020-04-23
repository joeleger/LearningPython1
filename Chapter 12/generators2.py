from url_utils import gen_from_urls

"""
    Generators
"""

urls = (
'http://microsoft.com', 'http://google.com', 'http://twitter.com', 'http://talkpython.fm', 'http://pythonpodcast.com',
'http://python.org')

# this is the generator version. Very easy replace the square brackets with parans around the outer for loop
for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)
print()
import pprint
#turned the above into a dictionary generator. Notice the ommission of the status code below using an '_' char
urls_res = {url: size for size, _, url in gen_from_urls(urls)}
pprint.pprint(urls_res)
