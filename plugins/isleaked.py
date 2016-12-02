# -*- coding: utf-8 -*-

import requests
from lxml import html

class isleaked():
    def check(self,email):
        url_token = 'https://isleaked.com/'
        r = requests.get(url_token)
        cookies = r.cookies
        tree = html.fromstring(r.content)
        token_name = tree.xpath('//*[@id="_post_token"]/@name')
        token_value = tree.xpath('//*[@id="_post_token"]/@value')

        url_consult = 'https://isleaked.com/check/'
        data = {'data':email,token_name[0]:token_value[0]}
        headers = {''}
        r = requests.post(url_consult,data=data,cookies=cookies)
        tree = html.fromstring(r.content)
        return tree.xpath('/html/body/div[2]/div/p[1]/text()')[0]
