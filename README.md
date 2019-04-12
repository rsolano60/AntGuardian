# Ant Guardian

Antminer SSH monitor and auto-restart tool 

Compatible with all antminers that use BMMiner

Restarts miner when accepted shares do not increase in 95 seconds

### Prerequisites

A computer with Python

All Mac and Linux computers come with Python pre-installed

You also might need to install Python paramiko module for SSH comunication using the command:
(Windows)
```sh
py -m pip install paramiko
```
Mac and Linux (you may not need to do this, but it does not hurt)
```sh
pip install paramiko
```
### Installing
SETUP: input these 3 variables in script file AntGuardian.py
```sh
#SETUP:
ipList = ('192.168....','192.168....','192.168....') #your miners, must have the same root password
USER = 'root' #your username
PASS = 'root' #your password
```

### Running
RUN COMMAND (Mac & Linux): 
```sh 
python3 AntGuardian.py
```
RUN COMMAND (Windows):
```sh
py AntGuardian.py

```

run command while in the directory of the script file. May vary with Python versions.

![alt text](https://raw.githubusercontent.com/rsolano60/Examples/master/init.jpeg)

### Example: One miner restarting (out of 3)

![alt text](https://raw.githubusercontent.com/rsolano60/Examples/master/work.jpeg)

## Authors

* **Ricardo Solano** - *Initial work* - [RSolano](https://github.com/rsolano60)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GNU GPL V3 License - see the [LICENSE.md](LICENSE.md) file for details

## Please Donate some satoshis BTC, BITCOIN
```sh
35w2Zmuj9Y83vb8uFvfjxQQfuzVYKwY4Dd
```
![alt text](https://blockchain.info/qr?data=35w2Zmuj9Y83vb8uFvfjxQQfuzVYKwY4Dd&size=200)

## or some LTC, LITECOIN
```sh
MJSVm7thYYENdV9zPzAyEv6s2Km4EUWKPy
```
## or some DASH
```sh
Xcs6DN7LXnEtQqLiKVGwZMLpMGJ9tufBcP
```
## or some ZCASH
```sh
t1W8vQte15jatZyzBcYuubzznMTF6LhEWJ9
```
## or some BCH, Bitcoin Cash (BCash)
```sh
qqgpy278maqdngqqf7ts232fjnk5kmusw5wag2ykjy
```
## or some XLM, STELAR
```sh
GBJMCLVHEVBDMT6GYZ7LPAQJJZHAOPD7KO2Y3GSUTH4XZYB3V3MV4BJY
```
## or some BTG, Bitcoin Gold
```sh
AGuQfFB4mHBCpUmXmGxtiU9vEZGBiu2ZCW
```
