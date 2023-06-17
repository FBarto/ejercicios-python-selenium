import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import time


class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def test_using_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(1)
        button = driver.find_element(By.XPATH,"//*[@id='accept-choices']")
        button.click()
        toggle = driver.find_element(By.XPATH,"//*[@id='main']/label[3]/div")
        toggle.click()
        time.sleep(1)
        toggle.click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()