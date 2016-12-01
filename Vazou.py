# -*- coding: utf-8 -*-
import re
import time
import telepot
from vazou.verifica import vazou

leak = vazou()
api = ''

def handle_message(msg):
    user_id = msg['from']['id']
    msg = msg['text'].lower()
    if msg == '/start' or msg == '/help':
        bot.sendMessage(user_id,open('response/help.txt').read())
    else:
        check_email = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', msg)
        if check_email != None:
            response = 'AVISO!!\nUtilize esse serviço somente para buscar informações referentes ao seu e-mail.Caso seu e-mail tenha vazado em alguma vez, você recebera uma msg informando em quais serviçoes ocorreram o vazamento.'
            bot.sendMessage(user_id,response)
            list_leaks = leak.check(msg)
            leaks = '\n'.join(list_leaks)
            if leaks:
                response = 'Foram encontrados %d serviços onde suas credenciais possivelmente fora expostas\n%s' % (len(list_leaks),leaks)
                bot.sendMessage(user_id,response)
            else:
                bot.sendMessage(user_id,'Não foi encontrado nenhum vazamento, porém não utilize senhas compartilhadas, e troque suas senhas periodicamente!')
        else:
            bot.sendMessage(user_id,'E-mail inválido!')
def main():
    bot.message_loop(handle_message,run_forever=True)
    while 1:
        time.sleep(10)

bot = telepot.Bot(api)
main()
