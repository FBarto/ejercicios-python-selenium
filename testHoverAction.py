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

    def test_using_hover(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        time.sleep(1)
        accep=driver.find_element(By.XPATH, "//*[@id='L2AGLb']/div")
        accep.click()
        time.sleep(1)
        elem=driver.find_element(By.LINK_TEXT,"Accedi")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        hover.click()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()
        