from pydal import DAL, Field
import os
path = 'sqlite://{0}'.format(os.path.abspath(os.path.join('db','storage.db')))
db = DAL(path)
db.define_table('users',
    Field('user_service_id',type='integer'),
    Field('email')
    )
db.define_table('leaks',
    Field('leaksource'),
    Field('user_service_id','reference users')
)

print user
#leaks = ['MegaSena','alandin']
#for leak in leaks:
#    db.leaks.insert(leaksource=leak,user_service_id=user)
#db.commit()
