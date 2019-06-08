#AntGuardian - A simple AntMiner monitor and auto-restart tool
#By RSolano
#License: GNU General Public license Version 3
#Version 0.0.2
#Run command:
#Python3 AntGuardian.py
#--------SETUP-------------SETUP-------------SETUP-------------SETUP-------------SETUP-------------SETUP-----
ipList = ('192.168....','192.168....','192.168....')
USER = 'root'
PASS = 'root'
#--------END-SETUP-------------END-SETUP-------------END-SETUP-------------END-SETUP-------------END-SETUP---
import sys
import paramiko
import re
import time
import datetime
def getAccShares(ip):
	stdin, stdout, stderr = clientList[ip].exec_command('/usr/bin/bmminer-api')	 # call to BMminer API to get miner data
	for line in stdout:
		if  re.search("\[Accepted", line): # Search for Accepted Shares line
			return line[17:-2]	# Return accepted shares value 
	print(' Could not connect to:' + str(ip))
def restartMiner(ip):
	print(str(ip) + ' not mining!!! Rebooting...')
	try:
		stdin, stdout, stderr = clientList[ip].exec_command('/sbin/reboot')
	except:
		print(' Could not connect to:' + str(ip))
	else:
		print(' Succsess!!!  ' + str(ip) + ' rebooting now!' )		
def connectMiner(ip):
	try:
		clientList[ip].connect(ip, username=USER, password=PASS) # Connect to host in case restar failed
	except:
		print(' Could not connect to:' + str(ip))
		pass
	else:
		clientList[ip].lastRestarted = datetime.datetime.now()
		print(str(ip) + ' Connected: {:%Y-%m-%d %H:%M:%S}'.format(clientList[ip].lastRestarted))
clientList = {} # Initialization
for ip in ipList:	# Open all cnnections
	clientList[ip] = paramiko.SSHClient()
	clientList[ip].set_missing_host_key_policy(paramiko.AutoAddPolicy()) 	# Set auto add host key policy
	connectMiner(ip) 	# Connect to host
	clientList[ip].acceptedShares = 0
	clientList[ip].prevAccShares = 0
while True:		# Main program loop
	for ip in ipList:
		secondsSinceRestart = (datetime.datetime.now() - clientList[ip].lastRestarted).seconds
		try:
			clientList[ip].acceptedShares = getAccShares(ip)
		except:
			print(str(ip) + ' Reconnecting... ---  Rebooted: ' + str(secondsSinceRestart)+ ' s ago.')
			connectMiner(ip)
		else:
			print(str(ip) + ' Shares:' + str(clientList[ip].prevAccShares) + '>' + str(clientList[ip].acceptedShares)+ '  ---  Rebooted: ' + str(secondsSinceRestart)+ ' s ago.')
		if clientList[ip].acceptedShares == clientList[ip].prevAccShares and secondsSinceRestart > 300: 
			restartMiner(ip)
			clientList[ip].lastRestarted = datetime.datetime.now()
		clientList[ip].prevAccShares = clientList[ip].acceptedShares
		time.sleep(95 / len(ipList))
client.close()
