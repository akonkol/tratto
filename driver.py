#!/usr/bin/env python

import Connectivity
import Systems 

#telnet to a cisco switch

m = Systems.OperatingSystems['IOS']
s = Connectivity.Session("192.168.1.1",23,"telnet",m)
s.login("yourusername", "yourpassword")
s.escalateprivileges('yourenablepassword')
#s.sendcommand("show ver")
s.sendcommand("show clock")
s.sendcommand("show run")
s.logout()
