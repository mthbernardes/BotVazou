import re

class checkemail(object):
    def __init__(self,):
        pass
    def __new__(self,email):
        return re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
