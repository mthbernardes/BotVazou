import ConfigParser
import os

class config(object):
    def __init__(self,):
        self.Config = ConfigParser.ConfigParser()
        self.Config.read(os.path.abspath(os.path.join('config',"vazou.conf")))

    def telegram(self,):
        return dict(self.Config.items('telegram'))

    def email(self,):
        return dict(self.Config.items('email'))

    def token(self,):
        return dict(self.Config.items('token'))

    def textos(self,):
        return dict(self.Config.items('textos_bot'))
