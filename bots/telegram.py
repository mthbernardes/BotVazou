# -*- coding: utf-8 -*-

import re
import time
import telepot

class telegram(object):
    def __init__(self,api,leak):
        self.bot = telepot.Bot(api)
        self.leak = leak
        self.bot.message_loop(self.handle_message,run_forever=True)
        while 1:
            time.sleep(10)

    def handle_message(self,msg):
        user_id = msg['from']['id']
        msg = msg['text'].lower()
        if msg == '/start' or msg == '/help':
            self.bot.sendMessage(user_id,open('response/help.txt').read())
        else:
            check_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', msg)
            if check_email != None:
                response = 'AVISO!!\nUtilize esse serviço somente para buscar informações referentes ao seu e-mail.Caso seu e-mail tenha vazado em alguma vez, você recebera uma msg informando em quais serviçoes ocorreram o vazamento.'
                self.bot.sendMessage(user_id,response)
                list_leaks = self.leak.check(msg)
                leaks = '\n'.join(list_leaks)
                if leaks:
                    response = 'Foram encontrados {0} serviços onde suas credenciais possivelmente fora expostas\n{1}\n{2}'.format(len(list_leaks),'-'*35,leaks)
                    self.bot.sendMessage(user_id,response)
                else:
                    self.bot.sendMessage(user_id,'Não foi encontrado nenhum vazamento, porém não utilize senhas compartilhadas, e troque suas senhas periodicamente!')
            else:
                self.bot.sendMessage(user_id,'E-mail inválido!')
