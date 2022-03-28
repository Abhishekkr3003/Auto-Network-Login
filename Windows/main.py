import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from datetime import datetime
from selenium.webdriver.firefox.service import Service
from getpass import getpass
import os
import sys


def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, relative_path)


def network_login(username, pswd):
    times_successfully_logged_in = 0
    while True:
        try:
            print("Working...")

            new_driver_path = resource_path(r'driver/geckodriver.exe')
            new_binary_path = resource_path(r'C:\Program Files\Mozilla Firefox\firefox.exe')
            options = Options()
            options.binary_location = new_binary_path
            serv = Service(new_driver_path)
            options.headless = True
            driver = webdriver.Firefox(service=serv, options=options)
            driver.implicitly_wait(10)
            driver.get("https://172.22.2.6/connect/PortalMain")
            time.sleep(1)
            driver.find_element(By.XPATH,
                                "//*[@id=\"LoginUserPassword_auth_username\"]").send_keys(username)

            driver.find_element(By.XPATH,
                                "//*[@id=\"LoginUserPassword_auth_password\"]").send_keys(
                pswd)
            driver.find_element(By.XPATH,
                                "//*[@id=\"UserCheck_Login_Button\"]").click()
            curTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            times_successfully_logged_in += 1
            if len(driver.find_elements(By.XPATH,
                                        "/html/body/div/table/tbody/tr[1]/td/div[2]/table/tbody/tr[2]/td/div/div/div/table/tbody/tr[1]/td/div[2]/p")) > 0:
                print(f"({times_successfully_logged_in}) Network Logged in Successfully ({curTime})")
                driver.close()
                time.sleep(10800)
            else:
                raise Exception("Check Credentials and Connectivity.")

        except Exception as e:
            print(f"Something went wrong.\nMore Info:")
            print("'''")
            print(e)
            print("'''")
            break


if __name__ == '__main__':
    username = input("Username: ")
    password = getpass()
    network_login(username, password)
    print("Process Ended")
