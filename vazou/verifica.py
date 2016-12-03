# -*- coding: utf-8 -*-

from plugins.haveibeenpwned import haveibeenpwned
from plugins.leakedsource import leakedsource
from plugins.isleaked import isleaked
from plugins.hackedemails import hackedemails

class vazou():
    def check(self,email):
        leaks = set()
        result_haveibeenpwned = haveibeenpwned().check(email)
        result_leakedsource = leakedsource().check(email)
        result_hackedemails = hackedemails().check(email)
        #result_isleaked = isleaked().check(email)
        if result_haveibeenpwned:
            leaks.update(result_haveibeenpwned)
        if result_leakedsource:
            leaks.update(result_leakedsource)
        if result_hackedemails:
            leaks.update(result_hackedemails)

        return set('*'.join(leaks).replace('.com','').lower().split('*'))
