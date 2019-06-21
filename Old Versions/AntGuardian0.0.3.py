#AntGuardian - A simple AntMiner monitor and auto-restart tool
#By RSolano
#License: GNU General Public license Version 3
#Version 0.0.3
#Run command:
#Python3 AntGuardian.py
#---------SETUP-----------------SETUP-----------------SETUP-----------------SETUP-----------------SETUP-------
ipList = ('192.168....','192.168....','192.168....')
USER = 'root'
PASS = 'root'
SECONDS_TO_WAIT = 95
#--------END-SETUP-------------END-SETUP-------------END-SETUP-------------END-SETUP-------------END-SETUP----
import sys
import paramiko
import re
import time
import datetime
import socket
def getAccShares(ip):
	stdin, stdout, stderr = clientList[ip].exec_command('/usr/bin/bmminer-api')	 # call to BMminer API to get miner data
	for line in stdout:
		if  re.search("\[Accepted", line): # Search for Accepted Shares line
			return line[17:-2]	# Return accepted shares value 
def restartMiner(ip):
	print(str(ip) + 'Rebooting...')
	try:
		stdin, stdout, stderr = clientList[ip].exec_command('/sbin/reboot')
	except Exception as ex:
		print(' Could not reboot:' + str(ip))
		print(ex)
	else:
		print(' Succsess. ' + str(ip) + ' is rebooting now!' )		
def connectMiner(ip):
	try:
		clientList[ip].connect(ip, username=USER, password=PASS) # Connect to host in case restar failed
	except Exception as ex:
		print(' Could not connect to: ' + str(ip))
		print(ex)
		pass
	else:
		clientList[ip].lastRestarted = datetime.datetime.now()
		print(str(ip) + ' Connected.')
def internet(host="8.8.8.8", port=53, timeout=3): #Host: 8.8.8.8 (google-public-dns-a.google.com) - OpenPort: 53/tcp -
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except Exception as ex:
		print(ex)
		return False
clientList = {} # Initialization
for ip in ipList:	# Open all cnnections
	clientList[ip] = paramiko.SSHClient()
	clientList[ip].set_missing_host_key_policy(paramiko.AutoAddPolicy()) 	# Set auto add host key policy
	connectMiner(ip) 	# Connect to host
	clientList[ip].acceptedShares = 0
	clientList[ip].prevAccShares = 0
	clientList[ip].lastRestarted = datetime.datetime.now()
while True:		# Main program loop
	for ip in ipList:
		secondsSinceRestart = (datetime.datetime.now() - clientList[ip].lastRestarted).seconds
		try:
			clientList[ip].acceptedShares = getAccShares(ip)
		except Exception as ex:
			print(ex)
			print(str(ip) + ' Reconnecting... ---  Rebooted: ' + str(secondsSinceRestart)+ ' s ago.')
			connectMiner(ip)
		else:
			print(str(ip) + ' Shares:' + str(clientList[ip].prevAccShares) + '>' + str(clientList[ip].acceptedShares))
		if clientList[ip].acceptedShares == clientList[ip].prevAccShares and secondsSinceRestart > 300: 
			print( str(ip) + 'Not mining---  Rebooted: ' + str(secondsSinceRestart)+ ' s ago.' )
			if internet():
				restartMiner(ip)
				clientList[ip].lastRestarted = datetime.datetime.now()
			else:
				print('No internet connection, waiting ' +  SECONDS_TO_WAIT + ' seconds.' )
				time.sleep(SECONDS_TO_WAIT)
		clientList[ip].prevAccShares = clientList[ip].acceptedShares
		time.sleep(SECONDS_TO_WAIT / len(ipList))
