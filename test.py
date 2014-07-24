#!/usr/bin/env python

from tratto.systems import *
from tratto.connectivity imoprt *

#telnet to a cisco switch

m = SystemProfiles['IOS']
s = Session("192.168.1.1",23,"telnet",m)
s.login("yourusername", "yourpassword")

# if your need to issue an "enable" command
s.escalateprivileges('yourenablepassword')
s.sendcommand("show clock")
s.sendcommand("show run")
s.logout()
