f = open("interface.up.txt","r")
while True:
	line = f.readline()
	if line:
		print line
	else:
		break
f.close()

