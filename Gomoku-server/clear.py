#!/usr/bin/env python
# -*- coding: utf-8 -*-

def endWith(s, *endstring):
    arr = map(s.endswith, endstring)
    if True in arr:
        return True
    else:
        return False

if __name__ == '__main__':
    import os
    files = os.listdir('.')

    for item in files:
        if os.path.isdir(item):
            for subitem in os.listdir(item):
                if not os.path.isdir(subitem) and endWith(subitem, 'pyc'):
                    print 'del: ' + str(subitem)
                    os.remove(os.path.join(item, subitem))
        elif endWith(item, 'pyc'):
            os.remove(os.path.join(item))
            
