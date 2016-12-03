# -*- coding: utf-8 -*-

import os
import sys
from hashids import Hashids
from random import randint
from sendemail import sendemail

sys.path.append('../')
from plugins.checkemail import checkemail
from config.parser import config
from db.db import banco
textos = config().textos()


class notify():
    def __init__(self,):
        conf = config().token()
        self.hash_id = Hashids(salt=conf['hash'], min_length=int(conf['tamanho_token']))

    def generate(self,user_id,email_monitor):
        self.key = randint(1000,9999)
        filename = '{0}'.format(str(user_id))
        pathname = os.path.abspath(os.path.join('tokens',filename))
        save = '{0}:{1}:{2}'.format(str(self.key),str(user_id),email_monitor)
        f = open(os.path.abspath(os.path.join('tokens',filename)),'w').write(save)
        key_hash = self.hash_id.encrypt(self.key)
        result_send = sendemail(email_monitor,key_hash)
        return result_send

    def verify(self,user_id,msg,leaks):
        db = banco()
        response = textos['monitor_ativado_err']
        if len(msg.split(' ')) == 3:
            cmd,email1,key_hash = msg.split(' ')
            filename = '{0}'.format(str(user_id))
            pathname_token = os.path.abspath(os.path.join('tokens',filename))
            if os.path.exists(pathname_token):
                if checkemail(email1) != None:
                    for code in open(pathname_token):
                        key,user,email = code.split(':')#QUERY BANCO
                        result_key_hash = self.hash_id.decrypt(key_hash)
                        if result_key_hash:
                            if user_id == int (user) and result_key_hash[0] == int(key) and email1 == email.strip():
                                response =  textos['monitor_ativado']
                                db.users.insert(user_service_id=user_id,email=email1)
                                user = db(db.users.user_service_id == user_id).select().first()
                                for leak in leaks.check(email1):
                                    db.leaks.insert(leaksource=leak,user_id=user)
                                db.commit()
                                os.remove(pathname_token)
                                break
                            else:
                                response = textos['codigo_invalido']
                else:
                    response = textos['email_invalido']
            else:
                response = textos['codigo_invalido']
        return response

    def delete(self,user_id,msg):
        db = banco()
        cmd,email = msg.split(' ')
        query = db((db.users.user_service_id == user_id) & (db.users.email == email))
        user = query.select()
        if user:
            query.delete()
            response = textos['delete_ok']
            db.commit()
        else:
            response = textos['delete_err']
        return response

    def monitor(self,user_id,msg):
        db = banco()
        monitor = msg.split(' ')
        if len(monitor) == 2:
            email_monitor = monitor[1]
            check_email = checkemail(email_monitor)
            if check_email != None:
                user = db((db.users.user_service_id == user_id) & (db.users.email == email_monitor)).select().first()
                if not user:
                    email_result = self.generate(user_id,email_monitor)
                    if email_result:
                        response = textos['email_monitor_ativado'].format(email_monitor)
                    else:
                        response = textos['email_monitor_err'].format(email_monitor)
                else:
                    response = textos['email_ja_cadastrado']
            else:
                response = textos['email_invalido']
        return response
