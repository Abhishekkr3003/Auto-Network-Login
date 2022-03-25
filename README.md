# Auto-Network-Login
This app will log you in after every 3 hours automatically. And don't worry, it's not CPU intensive.

## Pre-Requisite
- Python3
- PIP 
  
  Command to install (For Ubuntu-based systems) 
  
  `sudo apt install python3-pip`
  
- GECKODRIVER 
  
  Installation
  
  <strong>Linux</strong>
  ```
  wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
  sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.30.0-linux64.tar.gz -O > /usr/bin/geckodriver'
  sudo chmod +x /usr/bin/geckodriver
  rm geckodriver-v0.30.0-linux64.tar.gz
  ```
  
  <strong>Windows</strong>
  
  Download geckodriver from `https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-win64.zip` and extract it in a folder say `C:\driver` then copy this path and follow the following steps: 
    ```
    - Right-click on My Computer or This PC.
    - Select Properties.
    - Select Advanced system settings.
    - Click on the Environment Variables button.
    - From System Variables, select PATH.
    - Click on the Edit button.
    - Click the New button.
    - Paste the path of the GeckoDriver file (For example, your path will be something like C:\driver)
    ```
  
 - Selenium (Install it using `pip install selenium`)
  
## Installation
Just download and unzip or clone this repository. Open your terminal and navigate to that directory and run `python3 main.py`; enter your username and password, and that's it. It will keep you logged in till you are connected to the LNMIIT network and have credentials.

PS: you can build on top of it and define username and password in the python script.
