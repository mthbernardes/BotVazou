import requests
from pprint import pprint

class hackedemails():
    def check(self,email):
        url = "https://hacked-emails.com/api?q=%s" % email
        r = requests.get(url)
        leaks = r.json()
        #pprint(leaks)
        if leaks['status'] != 'notfound':
            leaks = [leak['title'].replace('.com','').lower() for leak in leaks['data']]
        return leaks
