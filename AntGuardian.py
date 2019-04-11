#AntGuardian
#By RSolano
#License: GNU General Public license Version 3
#Version 0.1.2
#Run command: Python3 AntGuardian.py

#SETUP: input these 3 variables
ipList = ('192.168....','192.168....','192.168....') #your miners
USER = 'root' #your username
PASS = 'root' #your password



import sys
import paramiko
import re
import time
import datetime
def getAccShares(ip):
	try:
		stdin, stdout, stderr = clientList[ip].exec_command('/usr/bin/bmminer-api')	 # call to BMminer API to get miner data
		for line in stdout:
			if  re.search("\[Accepted", line): # Search for Accepted Shares line
				return line[17:-2]	# Return accepted shares value 
	except:
		print(' Could not connect to:' + str(ip))
def restartMiner(ip):
	#stdin, stdout, stderr = clientList[ip].exec_command('/usr/bin/bmminer-api')
	#for line in stdout:
	#	print(line.strip())
	print(str(ip) + ' not mining!!! Rebooting...')
	try:
		stdin, stdout, stderr = clientList[ip].exec_command('/sbin/reboot')
	except:
		print(' Could not connect to:' + str(ip))
	else:
		print(' Succsess!!!  ' + str(ip) + 'rebooting now!' )	
# Main program Loop
accShares = {}
prevAccShares = {}
lastRestart = {}
clientList = {}
for ip in ipList:
	try:
		lastRestart[ip] = datetime.datetime.now()
		prevAccShares[ip] = 0
		clientList[ip] = paramiko.SSHClient()
		clientList[ip].set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Auto add host key
		clientList[ip].connect(ip, username=USER, password=PASS) # Connect to host
		lastRestart[ip] = datetime.datetime.now()
		prevAccShares[ip] = 0
	except:
		print(' Could not connect to:' + str(ip))
	else:
		print(str(ip) + ' Connected: {:%Y-%m-%d %H:%M:%S}'.format(lastRestart[ip]))
while True:
	for ip in ipList:
		secondsSinceRestart = (datetime.datetime.now() - lastRestart[ip]).seconds
		accShares[ip] = getAccShares(ip)
		print(str(ip) + ' Shares:' + str(prevAccShares[ip]) + '>' + str(accShares[ip])+ '  ---  Rebooted: ' + str(secondsSinceRestart)+ ' s ago')
		if accShares[ip] == prevAccShares[ip] and secondsSinceRestart > 300: 
			restartMiner(ip)
			lastRestart[ip] = datetime.datetime.now()
			try:
				clientList[ip].connect(ip, username=USER, password=PASS) # Connect to host in case restar failed
			except:
				print(' Could not connect to:' + str(ip))
				pass
			else:
				print(str(ip) + ' Connected: {:%Y-%m-%d %H:%M:%S}'.format(lastRestart[ip]))
		prevAccShares[ip] = accShares[ip]
		tSleep = 85 / len(ipList)
		time.sleep(tSleep)
client.close()
