# AntGuardian

AntMiner monitor and auto-restart tool 

Compatible with all AntMiners

Scans the local network for miners. Once connected, restarts any miner when accepted shares do not increase in SECONDS_4_CHECKS seconds, given that there is an active internet connection (checks with google.com).

### Prerequisites

* NMap

Download and install NMap. Link:
https://nmap.org/download.html

* Python

Most Mac and Linux distributions come with Python pre-installed. For windows and other systems, you may need to download and install Python first. Link:
https://www.python.org/downloads/


### Installation

Download the AntGuardian repository and unzip it. Link:
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
Otherwise, you are ready to run the script.

```sh
#SETUP:
#---------SETUP-----------------SETUP-----------------SETUP-----------------SETUP-----------------SETUP-------
USER = 'root'
PASS = 'root' # Replace with your miner's password
SECONDS_4_CHECKS = 95 # you need at least 6 seconds per miner, increase this number if monitoring 16 miners or more
SECONDS_TO_INTERNET = 60
REBOOT_TIME = 300
#--------END-SETUP-------------END-SETUP-------------END-SETUP-------------END-SETUP-------------END-SETUP----
```

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
## Options
You may also change the time intervals (seconds): <br />

* SECONDS_4_CHECKS: 
Time to wait between each check for accepted shares. <br />
* REBOOT_TIME: 
Lead time given to miners to start mining once they are rebooted by AntGuardian. <br />
* SECONDS_TO_INTERNET: 
Lead time given to miners to start mining again when internet connection is lost and recovered.


## Sample pictures (v0.0.1)

![alt text](https://raw.githubusercontent.com/rsolano60/Examples/master/init.jpeg)

![alt text](https://raw.githubusercontent.com/rsolano60/Examples/master/work.jpeg)

## Authors

**Ricardo Solano** - *Initial work* - [RSolano](https://github.com/rsolano60)

See also the list of [contributors](https://github.com/rsolano60/AntGuardian/graphs/contributors) who participated in this project.

## License

This project is licensed under the GNU GPL V3 License - see the [LICENSE](LICENSE) file for details

# Please Donate to the project!:

### BITCOIN (BTC) address:
BITCOIN QR code
```sh
35w2Zmuj9Y83vb8uFvfjxQQfuzVYKwY4Dd
```
![alt text](c)

### ETHEREUM (ETH) address:
```sh
0x98a1B000f7B5f2EdB1ea2A830f0D3B33a2eC4075
```

#### Other cryptocurrency addresses (ticker symbol):
LITECOIN (LTC) <br />
```sh
MJSVm7thYYENdV9zPzAyEv6s2Km4EUWKPy
```
DASH <br />
```sh
Xcs6DN7LXnEtQqLiKVGwZMLpMGJ9tufBcP
```
ZCASH (ZEC)<br />
```sh
t1W8vQte15jatZyzBcYuubzznMTF6LhEWJ9
```
Bitcoin Cash (BCH) <br />
```sh
qqgpy278maqdngqqf7ts232fjnk5kmusw5wag2ykjy
```
STELAR (XLM) <br />
```sh
GBJMCLVHEVBDMT6GYZ7LPAQJJZHAOPD7KO2Y3GSUTH4XZYB3V3MV4BJY
```
Bitcoin Gold (BTG) <br />
```sh
AGuQfFB4mHBCpUmXmGxtiU9vEZGBiu2ZCW
```
