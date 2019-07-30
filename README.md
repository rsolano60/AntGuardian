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
```sh
35w2Zmuj9Y83vb8uFvfjxQQfuzVYKwY4Dd
```
![alt text](c)

### ETHEREUM (ETH) address:
```sh
0x98a1B000f7B5f2EdB1ea2A830f0D3B33a2eC4075
```
![alt text](data:image/png;base64,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)

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
