#!/usr/bin/env python

'''Simple utility package that provides some handy methods'''

import httplib
import os
import subprocess
import sys
import time
import urllib

def thishost(try_iface=None):
    '''Get valid ip from `try_iface', if failed, try all known interfaces
    A tuple containing (host, iface) is returned on success, (None, try_iface)
    otherwise'''
    import netifaces

    host = None
    # Get all interfaces
    ifaces = netifaces.interfaces()
    ifaces.sort()
    # Insert try_iface to the first place
    if try_iface:
        ifaces.insert(0, try_iface)
    for iface in ifaces:
        try:
            if iface != try_iface and not iface.startswith('eth'):
                continue
            addr = netifaces.ifaddresses(iface).get(netifaces.AF_INET)
            if addr:
                host = addr[0]['addr']
                if host:
                    return host, iface
        except:
            host = None
    return None, try_iface


if __name__ == '__main__':
    try:
        import simplejson as json
    except:
        import json

    print thishost()
