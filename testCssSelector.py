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

    def test_using_css_selector(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/")
        accep=driver.find_element(By.XPATH, "//*[@id='accept-choices']")
        accep.click()
        encontrarElement = driver.find_element(By.CSS_SELECTOR, "a.tut-button")#Busca tal cual como escribimos con mayus y espacios.
        encontrarElement.click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
        
"""//a[contains(text(), 'Learn HTML')]""" # Para pegarle por texto.