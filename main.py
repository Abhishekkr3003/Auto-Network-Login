import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from datetime import datetime
from getpass import getpass


def network_login(username, pswd):
    times_successfully_logged_in = 0
    while True:
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
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
