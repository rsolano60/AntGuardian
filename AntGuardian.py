#AntGuardian - A simple AntMiner monitor and auto-restart tool
#By RSolano
#License: GNU General Public license Version 3
#Version 0.1.5
#    https://github.com/rsolano60/AntGuardian
#SETUP-----------------SETUP-----------------SETUP-----------------SETUP----------------
USER = 'root'
PASS = 'root' # Replace with your miner's password
SECONDS_4_CHECKS = 95 # you need at least 6 seconds per miner, increase this number if monitoring 16 miners or more
SECONDS_TO_INTERNET = 60
REBOOT_TIME = 300
#END-SETUP-------------END-SETUP-------------END-SETUP-------------END-SETUP-----------

import time
import datetime
import socket
import requests
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup
import html5lib
import nmap
from os.path import abspath, exists
from colorama import Fore, Style 

class Miner(object):
#This class represents a Bitmain Antminer
	def __init__(self,ip):
		self.__ip=ip
		self.__acceptedShares=0
		self.__lastRebooted = datetime.datetime.now() - datetime.timedelta(seconds=REBOOT_TIME)
		try:
			with requests.get('http://'+ip+'/cgi-bin/get_system_info.cgi', auth=HTTPDigestAuth(USER, PASS)) as r:
				cont = str(r.content)
				cont= cont[cont.find('Antminer'):]
				cont= cont[:cont.find('"')]
				self.__minerType = cont	
				self.__alive=True
				if not cont:
					self.__alive=False
		except:
			self.__alive=False
			#print("[{0}]: Could not initialize".format(self.__ip))
	def Miner(self):
		return self
	def update(self):
		try:
			with requests.get('http://'+self.__ip+'/cgi-bin/minerStatus.cgi', auth=HTTPDigestAuth(USER, PASS)) as r:
				soup = BeautifulSoup(r.content, "html5lib")
				out = - self.__acceptedShares
				self.__acceptedShares = int(soup.find_all_next('div', id='cbi-table-1-accepted')[-2].string.replace(',',''))
				out += self.__acceptedShares
			self.__alive=True
			return out
		except Exception as e:
			self.__alive=False
			#print("[{0}]: Could not update".format(self.__ip))
			#print(e)
			return 0
	def reboot(self):
		try:
			requests.get('http://'+self.__ip+'//cgi-bin/reboot.cgi', auth=HTTPDigestAuth(USER, PASS))
			self.__lastRebooted = datetime.datetime.now()
			self.__alive=True
		except:
			self.__alive=False
			print("[{0}]: Could not reboot{1}".format(self.__ip,self.__minerType))
			#print(e)			
		return 0	
	def getIp(self):
		return self.__ip
	def getAccShares(self):
		return float(self.__acceptedShares.replace(',',''))
	def getAlive(self):
		return self.__alive
	def getLastRebooted(self):
		return self.__lastRebooted
	def __str__(self):
		info= "{0} shares by [{1} @ {2}]-Last reboot {3}".format(self.__acceptedShares,self.__minerType,self.__ip,self.__lastRebooted.strftime('%Y-%m-%d %H:%M:%S.%f')[:-7])
		return info
def internet(host="8.8.8.8", port=53, timeout=3): #Host: 8.8.8.8 (google-public-dns-a.google.com) - OpenPort: 53/tcp -
	time.sleep(0.1)
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except Exception as ex:
		print(ex)
		return False
f_path = abspath("logo.txt") ## Start of the program - Print Logo
if exists(f_path):
	with open(f_path) as f:
		print(Fore.GREEN + Style.BRIGHT + f.read())
		print(Style.RESET_ALL)
print('Initializing: Connecting to internet.') 
while not internet(): ## Check for internet connection
	print('Waiting for internet connection checking www.google.com..' )
print('Getting local network I.P. list..')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Get list of IPs from local network
s.connect(('8.8.8.8', 80))
myIP = s.getsockname()[0]
s.close()
ipRange = myIP[:-3] + '0/24'
nm = nmap.PortScanner()
nm.scan(hosts=ipRange, arguments='-sn')
ipList = nm.all_hosts()
print('Attempting to connect to miners...')
if len(ipList) == 0:
	print('There are no discoverable hosts on the network... Make sure this computer is on the same network as your AntMiner(s)')
	exit()
minerList = []
for ip in ipList:	# Create miner objects
	m = Miner(ip)
	if m.getAlive():
		minerList.append(m)
		m.update()
		print('Connected! Now monitoring this AntMiner: \n'+str(m))
if len(minerList) == 0:
	print('Could not connect to any of the IPs:{0} with the password provided... Check: \n1)The PASS variable in file Antguardian.py is set to your actual miner(s) password. \n2)Your miner is connected to the same local network as this computer.'.format(ipList))
	print('')
	exit()
secondsPerMiner = abs((SECONDS_4_CHECKS / len(minerList)) - (6*len(minerList)))
print('Initialization complete: Found '+str(len(minerList))+' AntMiners')
print('AntGuardian ACTIVE. Stop by closing this window or pressing Ctrl+C')
time.sleep(SECONDS_4_CHECKS - (6*len(minerList)))
while True:		# Main program loop
	for miner in minerList:
		newShares = miner.update()
		print(miner)		
		secondsSinceRestart = (datetime.datetime.now() - miner.getLastRebooted()).seconds
		if newShares == 0 and secondsSinceRestart > REBOOT_TIME:
			print( str(miner.getIp()) + ' Not mining...  ---  Rebooted: ' + str(secondsSinceRestart)+ ' s ago.' )
			if internet():
				print('Rebooting ' +  miner.getIp())
				miner.reboot()
			else:
				while not internet():
					print('Waiting for internet connection checking www.google.com...' )
				print('Internet is back, waiting ' +  str(SECONDS_TO_INTERNET) + ' seconds for miners to reconnect.' )
				time.sleep(SECONDS_TO_INTERNET)
				print('AntGuardian ACTIVE. Stop by closing this window or pressing Ctrl+C')
		time.sleep(secondsPerMiner)	
