# -*- coding: utf-8 -*-

import re
import sys
import time
import telepot

sys.path.append('../')
from monitor.notify import notify
from plugins.checkemail import checkemail
from config.parser import config

textos = config().textos()
telegram_api = config().telegram()

class telegram():
    def __init__(self,*args,**kwargs):
        self.bot = telepot.Bot(telegram_api['telegram_api'])
        self.leak = kwargs.get('leak', None)

    def start(self,):
        self.bot.message_loop(self.handle_message,run_forever=True)
        while 1:
            time.sleep(10)

    def notify(self,service,user_id):
        msg = textos['novo_leak'].format(service)
        self.bot.sendMessage(user_id,msg)

    def handle_message(self,msg):
        user_id = msg['from']['id']
        msg = msg['text']

        if msg.startswith('/start') or msg.startswith('/help'):
            msg = msg.lower()
            self.bot.sendMessage(user_id,open('response/help.txt').read())

        elif msg.startswith('/monitor'):
            msg = msg.lower()
            response = notify().monitor(user_id,msg)
            self.bot.sendMessage(user_id,response)

        elif msg.startswith('/active'):
            response = notify().verify(user_id,msg,self.leak)
            self.bot.sendMessage(user_id,response)

        elif msg.startswith('/delete'):
            response = notify().delete(user_id,msg)
            self.bot.sendMessage(user_id,response)
            
        else:
            msg = msg.lower()
            check_email = checkemail(msg)
            if check_email != None:
                response = textos['aviso']
                self.bot.sendMessage(user_id,response)
                list_leaks = self.leak.check(msg)
                leaks = '\n'.join(list_leaks)
                if leaks:
                    response = textos['leaks_encontrados'].format(len(list_leaks),'-'*35,leaks)
                    self.bot.sendMessage(user_id,response)
                else:
                    response = textos['zero_leaks_encontrados']
                    self.bot.sendMessage(user_id,response)
            else:
                response = textos['email_invalido']
                self.bot.sendMessage(user_id,response)
