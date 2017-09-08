# coding:utf-8
import os
import time
import logging
import unittest
from time import sleep
from selenium import webdriver

__author__ = 'Sterling Su'
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

Your_Account = "15195772731"
Your_Password = "sterling123"


class LoginSmartSpeaker(unittest.TestCase):
    def loginSmartSpeak(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.linglong.android:id/phone_number").send_keys(Your_Account)
        self.driver.find_element_by_id("com.linglong.android:id/user_password").send_keys(Your_Password)
        button_login = self.driver.find_element_by_id("com.linglong.android:id/login_but")
        button_login.click()

    def setUp(self):
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

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.assertTrue(self.driver.find_element_by_id("com.linglong.android:id/base_title").is_displayed())
        print(u"登陆成功")
        sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginSmartSpeaker)
    unittest.TextTestRunner(verbosity=2).run(suite)
