#!/usr/bin/python
import tratto.systems import *
import tratto.connectivity import * 

import argparse
import getpass
import re


parser = argparse.ArgumentParser(description='Grabs L3 interface information over ssh/telnet')

parser.add_argument('-u','--username' , help='username', required=True)
parser.add_argument('-p','--password', help='password', required=False)
parser.add_argument('-d','--device', help='IP address or FQDN', required=True)
parser.add_argument('-t','--telnet', help='use telnet (ssh is default)', required=False)
parser.add_argument('-H','--HOSTNAME', help='specify hostname of the device', required=False)
parser.add_argument('-dn','--domainname', help='specify domain name of the device', required=False)
parser.add_argument('-s','--schema', help='define dns format string. \
                                       Fields available: interface_name, interface_number,\
                                       and hostname. \r\n \
                                       example: \
                                        -s \"interface_name+interface_number.hostname.network.mycompany.com\"', required=False)
args = vars(parser.parse_args())

device = args['device']
username = args['username']
os_type = SystemsProfiles['IOS']

if args['password']:
	password = args['password']

if not args['password']:
	password = getpass.getpass()

if args['telnet']:
	transport ="telnet"
 	port = 23 
else:
	transport = "ssh"
	port = 22



session = Session(device,port,transport,os_type)
session.login(username, password)

if args['HOSTNAME']:
   hostname = args['HOSTNAME']
else:
   hostname = session.sendcommand("show run | i hostname")[9:]

if args['domainname']:
   domainname = "." +  args['domainname']
else:
   found_domainname = session.sendcommand("show ip domain")

   if found_domainname:
      domainname = "." +  found_domainname
   else:
      domainname = ""

ip_ints = session.sendcommand("sho ip int br")
session.logout()


#for each line of sho ip int brief

for line in ip_ints.split('\r\n'):
   contains_ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
   if contains_ip:
        line_chunks = line.split()

        #[0]= gigabitethernet1/2
        int_name = line_chunks[0]

        #[1] = 10.a.b.c
        int_ip = line_chunks[1]

        if "GigabitEthernet" in int_name:
           prefix = "GE"
           suffix = int_name[15:]

        if "FastEthernet" in int_name:
           prefix = "FE"
           suffix = int_name[12:]

        if "Loopback" in int_name:
           prefix ="LO"
           suffix = int_name[8:]

        if "Vlan" in int_name:
           prefix="VL"
           suffix=int_name[4:]

        if "Tunnel" in int_name:
           prefix="TU"
           suffix= int_name[6:]

        #ignore NVIs
        if "NVI" in int_name:
          break

        #replace interface number slash with hyphen
        clean_suffix = re.sub('\/','-',suffix)

	if args['schema']:
	   schema = args['schema']
	   dns_line = schema.replace('interface_name',prefix)
	   dns_line = dns_line.replace('interface_number',clean_suffix)
	   dns_line = dns_line.replace('hostname',hostname)
	   dns_line = dns_line.replace('ip_address',int_ip)
	   print dns_line 
	else:
           print prefix + clean_suffix  + "." + hostname +  domainname + "," +  int_ip
