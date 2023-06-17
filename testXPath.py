import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def test_buscar_xpath(self):
        driver= self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        test_buscar_xpath=driver.find_element(By.XPATH,"//*[@id="APjFqb"]")
        """Cap 7 min 8.04"""