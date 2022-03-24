# Auto-Network-Login
This app will log you in every 3 hours automatically. And don't worry, it's not CPU intensive.

# Pre-Requisite
- Python3
- pip 
  
  Command to install (For ubuntu based systems) 
  
  `sudo apt install python3-pip`
  
- geckodriver 
  
  Commands to install (For ubuntu based systems)
  ```
  wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
  sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.30.0-linux64.tar.gz -O > /usr/bin/geckodriver'
  sudo chmod +x /usr/bin/geckodriver
  rm geckodriver-v0.30.0-linux64.tar.gz
  ```
 - Selenium (Install it using `pip install selenium`)

# Installation
Just download and unzip or clone this repository. Open your terminal and navigate to `Auto-Network-Login` directory and run `python3 main.py`; enter your username and password, and that's it. It will keep you logged in till you are connected to the LNMIIT network and have credentials.

Moreover, you can build on top of it and define username and password in the python script itself.
