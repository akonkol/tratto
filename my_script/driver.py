#!/usr/bin/env python
import Connectivity
import Systems
#telnet to a cisco switch
m = Systems.OperatingSystems['IOS']
s = Connectivity.Session("173.10.251.70",23,"telnet",m)
s.login("husuisheng", "Hss428hss")
# if your need to issue an "enable" command
#s.escalateprivileges('yourenablepassword')
s.sendcommand("show clock")
s.sendcommand("show ip inter brief")
s.logout()
