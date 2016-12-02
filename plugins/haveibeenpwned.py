# -*- coding: utf-8 -*-

import requests
from pprint import pprint

class haveibeenpwned():
    def check(self,email):
        url = 'https://haveibeenpwned.com/api/v2/breachedaccount/%s' % email
        r = requests.get(url)
        #pprint(r.json())
        if r.content:
            a = [leak['Title'] for leak in r.json()]
            return a
        else:
            return False
