import unittest
from utilities import buscar_elemento, buscar_elemento_interactable
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

    def test_using_hyperlink(self):
        driver = self.driver
        driver.get("https://www.youtube.com/")
        accept = buscar_elemento(
            driver, 
            By.XPATH, 
            "//*[@id='content']/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]",    
        )
        #accep=driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
        accept.click()
        #time.sleep(3)
        encontrarElement = buscar_elemento(
            driver,
            By.CSS_SELECTOR,
            "input#search"
        )
        #encontrarElement = driver.find_element(By.CSS_SELECTOR, "input#search") #Busca tal cual como escribimos con mayus y espacios.
        encontrarElement.send_keys("paren la mano")
        encontrarElement.send_keys(Keys.ENTER)
        #time.sleep(3)

if __name__ == '__main__':
    unittest.main()
        