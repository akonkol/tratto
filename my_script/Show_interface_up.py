#!/usr/bin/env python
import Connectivity
import Systems
#telnet to a cisco switch
m = Systems.OperatingSystems['IOS']
s = Connectivity.Session("173.10.251.253",23,"telnet",m)
s.login("admin", "passwords")
f = open("interface.up.txt","r")

command_line=[]
# if your need to issue an "enable" command
#s.escalateprivileges('yourenablepassword')
s.sendcommand("show clock")
while True:
	line = f.readline()
# for reset the format of the sendcommand
	line = line.strip('\n')
	line = line.rstrip()
	if line:
		command_line.append(line)	
		s.sendcommand("show run interface " + line)
	else:
		break
#print(command_line)
for i in command_line:
	print i
	i=i+1


#s.sendcommand("show run interface g1/8")
s.logout()
f.close()

