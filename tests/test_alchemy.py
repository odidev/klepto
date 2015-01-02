#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2013-2015 California Institute of Technology.
# License: 3-clause BSD.  The full license text is available at:
#  - http://trac.mystic.cacr.caltech.edu/project/pathos/browser/klepto/LICENSE

from klepto.archives import sqltable_archive as sql_archive
#from klepto.archives import sql_archive
#d = sql_archive('postgresql://user:pass@localhost/defaultdb', cached=False)
#d = sql_archive('mysql://user:pass@localhost/defaultdb', cached=False)
d = sql_archive(cached=False)

try:
    import sqlalchemy
    __alchemy = True
except ImportError:
    __alchemy = False

d['a'] = 1
d['b'] = '1'
assert d['a'] == 1
assert d['b'] == '1'

if __alchemy:
    d['c'] = min
    squared = lambda x:x**2
    d['d'] = squared
    assert d['c'] == min
    assert d['d'](2) == squared(2)
else:
    print("for greater capabilities, install sqlalchemy")


# EOF
