import requests
from lxml import html

class leakedsource():
    def check(self,email):
        url = 'https://www.leakedsource.com/main/?email=%s' % email
        r = requests.get(url)
        tree = html.fromstring(r.content)
        leaks = tree.xpath('/html/body/center/form/li/text()[1]')
        if leaks:
            leaks = [leak.replace(' has: ','') for leak in leaks]
            return leaks
        else:
            return False
