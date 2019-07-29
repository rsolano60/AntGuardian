# Ant Guardian

Antminer monitor and auto-restart tool 

Compatible with all AntMiners

Scans local IP Range for miners. Once connected, restarts any miner when accepted shares do not increase in SECONDS_4_CHECKS seconds, and there is an active internet connection (checks with google.com).

### Prerequisites

* A computer with NMap and Python 2 or 3

Download and install NMap. Link:
https://nmap.org/download.html

Most Mac and Linux distributions come with Python pre-installed. For windows and other systems, you may need o download and install Python first. Link:
https://www.python.org/downloads/


### Installation

Download the Antguardian repository and unzip it. Link:
https://github.com/rsolano60/AntGuardian

* Install Python requirements

Using the command prompt, navigate to directory Downloads/AntGuardian and run the command:


(Mac and Linux) COMMAND:
```sh
pip install -r requirements.txt
```

(Windows) COMMAND:
```sh
py -m pip install -r requirements.txt
```


### Setup

If you have changed the password of your miners from the default "root", you must change the PASS varieble in the  script file AntGuardian.py
Otherwise, you are ready to run the script. It will automatically scan the local network and try to connect to miners.

```sh
#SETUP:
#---------SETUP-----------------SETUP-----------------SETUP-----------------SETUP-----------------SETUP-------
USER = 'root'
PASS = 'root' # Replace with your miner's password
SECONDS_4_CHECKS = 95 # you need at least 6 seconds per miner to check the hashrate on a single thread, increase this number if monitoring 16 miners or more
SECONDS_TO_INTERNET = 60
REBOOT_TIME = 300
#--------END-SETUP-------------END-SETUP-------------END-SETUP-------------END-SETUP-------------END-SETUP----
```
you may also change the interval to wait between each check for shares, by changing SECONDS_4_CHECKS. 
REBOOT_TIME lts you set the time you want to wait for your miners to reboot when the script reboots them.
Also you can adjust the lead time to give to your miners to restart when internet connection is lost and recovered by changing SECONDS_TO_INTERNET.

### Running
Using the command prompt, while in the directory Downloads/AntGuardian, run the program by entering the command:

(Mac & Linux) RUN COMMAND: 
```sh 
python3 AntGuardian.py
```
(Windows) RUN COMMAND:
```sh
py AntGuardian.py

```

![alt text](https://raw.githubusercontent.com/rsolano60/Examples/master/init.jpeg)

### Example: One miner restarting (out of 3)

![alt text](https://raw.githubusercontent.com/rsolano60/Examples/master/work.jpeg)

## Authors

**Ricardo Solano** - *Initial work* - [RSolano](https://github.com/rsolano60)

See also the list of [contributors](https://github.com/rsolano60/AntGuardian/graphs/contributors) who participated in this project.

## License

This project is licensed under the GNU GPL V3 License - see the [LICENSE](LICENSE) file for details

# Please Donate some satoshis BTC, BITCOIN
```sh
35w2Zmuj9Y83vb8uFvfjxQQfuzVYKwY4Dd
```
![alt text](https://blockchain.info/qr?data=35w2Zmuj9Y83vb8uFvfjxQQfuzVYKwY4Dd&size=200)

#### or some LTC, LITECOIN
```sh
MJSVm7thYYENdV9zPzAyEv6s2Km4EUWKPy
```
#### or some DASH
```sh
Xcs6DN7LXnEtQqLiKVGwZMLpMGJ9tufBcP
```
#### or some ZCASH
```sh
t1W8vQte15jatZyzBcYuubzznMTF6LhEWJ9
```
#### or some BCH, Bitcoin Cash
```sh
qqgpy278maqdngqqf7ts232fjnk5kmusw5wag2ykjy
```
#### or some XLM, STELAR
```sh
GBJMCLVHEVBDMT6GYZ7LPAQJJZHAOPD7KO2Y3GSUTH4XZYB3V3MV4BJY
```
#### or some BTG, Bitcoin Gold
```sh
AGuQfFB4mHBCpUmXmGxtiU9vEZGBiu2ZCW
```
