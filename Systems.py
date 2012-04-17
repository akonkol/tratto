#!/usr/bin/env python

class OperatingSystem(object):
	ESCALATE_COMMAND=''
	PAGINATES	=False
	VERSION		=''
	PROMPTLINE	=''



class CiscoIOS(OperatingSystem):
	'''cisco ios'''
	PROMPTLINE      = r'[-\w]+[>#]'
	GET_CONFIG	='show running-config'
	PAGINATES	=True
	VERSION		='show version'
	DISABLE_PAGINATION = 'terminal length 0'
	ESCALATE_COMMAND='enable'

class CiscoWebNS(OperatingSystem):
	'''cisco webns css 11500'''
	PROMPTLINE      ="#"
	GET_CONFIG	='show running config'
	PAGINATES	=True
	DISABLE_PAGINATION = 'terminal length 65000'

class AppleOSX(OperatingSystem):
	'''apple OSX defaults'''
	PROMPTLINE      = r'[-\w]+[$#]'
	GET_CONFIG = "df -h"
	VERSION		="uname -a"
	PRIVILEGE	="sudo su"

class OpenBSD(OperatingSystem):
	'''OpenBSD defaults'''
	PROMPTLINE      = r'[$#]'
	GET_CONFIG = "df -h"
	VERSION		="uname -a"
	PRIVILEGE	="sudo su"


class SecureComputingSidewinder(OperatingSystem):
	'''sidewinder configs'''
	PROMPTLINE	='{}'
	PRIVILEGE	='srole'
	GET_CONFIG	="cf acl query"

class ArubaOS(OperatingSystem):
	'''aruba configs'''
	PROMPTLINE	='#'
	PAGINATES 	=True
	DISABLE_PAGINATION = 'terminal length 0'
	GET_CONFIG	="show run"

OperatingSystems = {
	'IOS': CiscoIOS,
	'WebNS': CiscoWebNS,
	'OSX': AppleOSX,
	'SOS': SecureComputingSidewinder,
	'AOS': ArubaOS,
	'OBSD': OpenBSD,
	}


