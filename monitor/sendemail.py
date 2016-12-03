# -*- coding: utf-8 -*-

import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

sys.path.append('../')
from config.parser import config

conf = config().email()

class sendemail(object):
    def __init__(self,):
        pass

    def __new__(self,toaddr,hashcode):
        fromaddr = conf['conta']
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = conf['assunto_email']

        body = hashcode
        msg.attach(MIMEText(body, 'plain'))
        try:
            response = False
            server = smtplib.SMTP(conf['smtp'], int(conf['smtp_port']))
            server.starttls()
            server.login(fromaddr, conf['senha'])
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
            response = True
        except Exception as e:
            print e
        return response
