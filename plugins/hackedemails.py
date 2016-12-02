import requests
from pprint import pprint

class hackedemails():
	def check(self,email):
	    url = 'https://hacked-emails.com/api?q=%s' % email
	    r = requests.get(url)
	    if r.content:
	        a = [leak['title'] for leak in r.json()['data']]
	        print a
	        		
	    else:
	        return False