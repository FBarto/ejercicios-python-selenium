import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import cv2
import time

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def test_using_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        time.sleep(1)
        cookiesAcepted = driver.find_element(By.XPATH,"//*[@id='accept-choices']")
        cookiesAcepted.click()
        select = driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/select")
        option= select.find_elements(By.TAG_NAME, "option")
        time.sleep(1)
        for opciones in option:
            print("Los valores son: %s" % opciones.get_attribute("value"))
            opciones.click()
        seleccionar=Select(driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()
        