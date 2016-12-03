# -*- coding: utf-8 -*-

from bots.telegram import telegram
from vazou.verifica import vazou
from monitor.cron import cron
from threading import Thread

def bot_telegram(leak):
    telegram(leak=leak).start()

def monitor_start():
    cron().start()
leak = vazou()
print 'Iniciando bot Vazou no Telegram'
t1 = Thread(target=bot_telegram, args=(leak,))
t1.start()
print 'Iniciando Monitor'
t2 = Thread(target=monitor_start)
t2.start()
print 'FIm'
