#!/usr/bin/env python

from tratto.systems import *
from tratto.connectivity import *

#telnet to a cisco switch

m = SystemProfiles['IOS']
s = Session("192.168.1.1",23,"telnet",m)
s.login("yourusername", "yourpassword")

# if your need to issue an "enable" command
#s.escalateprivileges('yourenablepassword')
show_clock_results = s.sendcommand("show clock")
s.logout()


print show_clock_results
