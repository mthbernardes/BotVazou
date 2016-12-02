# -*- coding: utf-8 -*-

import requests
from pprint import pprint

class hackedemails():
    def check(self,email):
        url = "https://hacked-emails.com/api?q=%s" % email
        r = requests.get(url)
        leaks_f = False
        leaks = r.json()
        if leaks['status'] != 'notfound':
            leaks_f = [leak['title'].replace('.com','').lower() for leak in leaks['data']]
        return leaks_f
