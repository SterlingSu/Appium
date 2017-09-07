import os
import time
import logging
from selenium import webdriver

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

Your_Account = "15195772731"
Your_Password = "sterling4e"


class SmartSpeak():
    def __init__(self):
        # Returns abs path relative to this file and not cwd
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        desired_caps = {}
        desired_caps['deviceName'] = 'AMAX on BullHead'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0   '
        desired_caps['app'] = PATH('E:\Appium\TestAPK\Vbox_Phone_3.2.4.335_xianwang.apk')
        desired_caps['appPackage'] = 'com.linglong.android'
        desired_caps['appActivity'] = 'com.linglong.android.StartActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(4)
        self.loginSmartSpeak()

    def loginSmartSpeak(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.linglong.android:id/phone_number").send_keys(Your_Account)
        self.driver.find_element_by_id("com.linglong.android:id/user_password").send_keys(Your_Password)
        button_login = self.driver.find_element_by_id("com.linglong.android:id/login_but")
        button_login.click()
        self.getall()

    def getall(self):
        self.driver.quit()


if __name__ == '__main__':
    SmartSpeak().__init__()
