# -*- coding: utf-8 -*-

import sys
import logging
from apscheduler.schedulers.blocking import BlockingScheduler

sys.path.append('../')
from db.db import banco
from vazou.verifica import vazou
from bots.telegram import telegram

sched = BlockingScheduler()
logging.basicConfig()

class cron():
    @sched.scheduled_job('interval', seconds=20)
    def monitor():
        db = banco()
        leaks = list()
        telegram_bot = telegram()
        news = vazou()
        for user in db(db.users).select():
            for leak in db(db.leaks.user_id == user.id).select():
                leaks.append(leak.leaksource)
            for new in news:
                if new not in leaks:
                    telegram_bot.notify(new,user.user_service_id)
                    db.leaks.insert(leaksource=new,user_id=user)
                    db.commit()
    def start(self,):
        sched.start()
