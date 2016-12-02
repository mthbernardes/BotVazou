import requests
from pprint import pprint

class hackedemails():
    def check(self,email):
        f_leaks = False
        url = "https://hacked-emails.com/api?q=%s" % email
        r = requests.get(url)
        leaks = r.json()
        if leaks['status'] != 'notfound':
            f_leaks = [leak['title'].replace('.com','').lower() for leak in leaks['data']]
        return f_leaks
