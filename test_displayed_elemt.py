import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import cv2
import time

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def test_using_displayed(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        accep=driver.find_element(By.XPATH, "//*[@id='L2AGLb']/div")
        accep.click()
        displalyElemt = driver.find_element(By.NAME, "btnI")
        print(displalyElemt.is_displayed()) #Regresa true o falce si ya cargo el elemt
        print(displalyElemt.is_enabled())#Regresa T o F si el elemt esta disponible para darle clik.


if __name__ == '__main__':
    unittest.main()
        