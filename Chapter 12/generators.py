import pprint as pp
import requests

"""
    Generators
"""

urls = ('http://microsoft.com','http://google.com','http://twitter.com',)

# this is a list comp
for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)
print()
# this is the generator version. Very easy replace the square brackets with parans around the outer for loop
for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '-->', resp.status_code, '-->', resp.url)
print('this is the generator version')