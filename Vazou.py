# -*- coding: utf-8 -*-

from bots.telegram import telegram
from vazou.verifica import vazou

def bot_telegram(api,leak):
    telegram(api,leak)

leak = vazou()
telegram_api = 'YOUR-TELEGRAM-API-HERE'
bot_telegram(telegram_api,leak)
