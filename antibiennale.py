# antibiennale.py
# an antivirus script to disinfect files contaminated by the virus biennale.py from
# HTTP://WWW.0100101110101101.ORG and [epidemiC] http://www.epidemic.ws
# this is a simple modification of the original biennale.py
# by:
# Camilo Martinez
# cmart@decolector.net || http://decolector.net || http://martinez-zea.info

from dircache import *
from string import *
import os, sys
from stat import *

def interrupt(guest):
    try:
        soul = open(guest, "r")
        body = soul.read()
        soul.close()
        if "[epidemiC]" in body:
            soul = open(guest, "w")
            newbody = body[find(body, '#'*3) + 5:]
            soul.write(newbody)
            soul.close()
            print "cleaning infected file: " + guest
    except IOError: pass

def chat(party, guest):
    if split(guest, ".")[-1] in ("py", "pyw"):
        interrupt(party + guest)

def join(party):
    try:
        if not S_ISLNK(os.stat(party)[ST_MODE]):
            guestbook = listdir(party)
            if party != "/": party = party + "/"
            if not lower(party) in wank and not "__init__.py" in guestbook:
                for guest in guestbook:
                    chat(party, guest)
                    join(party + guest)
    except OSError: pass

if __name__ == '__main__':
        blacklist = replace(split(sys.exec_prefix,":")[-1], "\\", "/")
        if blacklist[-1] != "/": blacklist = blacklist + "/"
        wank = [lower(blacklist), "/proc/", "/dev/"]
        join("/")
        print ">This file was cleaned from biennale.py by antibiennale.py, the world slowest antivirus."
        print "Either Linux or Windows, antibiennale.py is definetely not the first Python antivirus."
        print "Camilo Martinez: "
        print "cmart@decolector.net || http://decolector.net || http://martinez-zea.info"
        print "> ______________________ No Biennale di Venezia at all ____________________ <"
###
