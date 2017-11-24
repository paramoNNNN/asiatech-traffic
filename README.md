# asiatech-traffic
get asiatech remaining traffic

## Installation
* you need selenium and pyvirtualdisplay

```
pip install -u selenium
pip insstall pyvirtualdisplay
```

* and you need to download geckodriver and copy it to /usr/local/bin/ with this command:
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-arm7hf.tar.gz && tar -xf geckodriver-v0.19.1-arm7hf.tar.gz && rm geckodriver-v0.19.1-arm7hf.tar.gz && sudo mv geckodriver /usr/local/bin/
```
* open 1544.py with any text editor
* place your username and password
* you ready to go

## Usage

run command below:
```
python 1544.py
```

## alias
you can add alias in bashrc to run this script from anywhere with your custom command:

* open ~/.bashrc with any text editor like vim or gedit
* add this line into bashrc
```
alias GetTraffic='YOUR_PATH_TO_1544.py_FILE/1544.py'
```
* then type this command to reload bashrc
```
source ~/.bashrc
```
* when you enter GetTraffic into terminal script will run


