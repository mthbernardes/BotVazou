import os
from pydal import DAL, Field

class banco(object):
    def __init__(self,):
        pass
    def __new__(self,):
        path = 'sqlite://{0}'.format(os.path.abspath(os.path.join('db','storage.db')))
        db = DAL(path)
        db.define_table('users',
            Field('user_service_id',type='integer'),
            Field('email')
            )
        db.define_table('leaks',
            Field('leaksource'),
            Field('user_id','reference users')
        )
        return db
