# Ant Guardian

Antminer SSH monitor and auto-restart tool 

Compatible with all AntMiners that use BMMiner and have SSH enabled (Like antminer S9

Restarts miner when accepted shares do not increase in SECONDS_TO_WAIT seconds, and there is an active internet connection (checks with google.com).

### Prerequisites

* A computer with Python

All Mac and Linux computers come with Python pre-installed

* Install Python requirements using the command:

(Windows) COMMAND:
```sh
py -m pip install -r requirements.txt
```
(Mac and Linux) COMMAND:
```sh
pip install -r requirements.txt
```
### Setup
Input these 3 variables in script file AntGuardian.py: ipList, USER and PASS 

by replacing the examples inside quotes with the real values. (username and password is root by default)

Real values should match the IP address, Username and Password of all the miners you want to monitor and control.

You can add or remove miners from ipList as you need
```sh
#SETUP:
ipList = ('192.168....','192.168....','192.168....') #your miners, must have the same root password
USER = 'root' #your username
PASS = 'root' #your password
SECONDS_TO_WAIT = 95
```
you may also change the interval to wait between each check for shares, by changing SECONDS_TO_WAIT. 

This variable also indicates the time to wait for a new internet connection

### Running
(Mac & Linux) RUN COMMAND: 
```sh 
python3 AntGuardian.py
```
(Windows) RUN COMMAND:
```sh
py AntGuardian.py

```
run command while in the directory of the script file. May vary with Python versions.

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

