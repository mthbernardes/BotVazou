from pprint import pprint
from plugins.haveibeenpwned import haveibeenpwned
from plugins.leakedsource import leakedsource
from plugins.isleaked import isleaked

class vazou():
    def check(self,email):
        leaks = set()
        result_haveibeenpwned = haveibeenpwned().check(email)
        result_leakedsource = leakedsource().check(email)
        if result_haveibeenpwned:
            leaks.update(result_haveibeenpwned)
        if result_leakedsource:
            leaks.update(result_leakedsource)
        #print 'isleaked'
        #pprint(isleaked().check(email))
        return set('*'.join(leaks).replace('.com','').lower().split('*'))
