import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class HomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def ingresarPaginaPrincipal(self):
        driver= self.driver
        driver.get("http://the-internet.herokuapp.com/")
        time.sleep(3)

    def aBTesting(self):
        driver=self.driver
        buscar_xpath=driver.find_element(By.XPATH,"//a[@href='/abtest']")
        buscar_xpath.click()    

    def addRemoveTest(self):
        driver=self.driver
        buscar_xpath=driver.find_element(By.XPATH,"//a[contains(@href,'elements/')]")
        buscar_xpath.click()
        
    def basicAuthTest(self):
        driver=self.driver
        buscar_xpath=driver.find_element(By.XPATH,"//a[@href='/basic_auth']")
        buscar_xpath.click()

    def brokenImagesTest(self):
        driver=self.driver
        buscar_xpath=driver.find_element(By.XPATH,"//a[@href='/broken_images']")
        buscar_xpath.click()

    def challenginDOMTest(self):
        driver=self.driver
        buscar_xpath=driver.find_element(By.XPATH,"//a[@href='/challenging_dom']")
        buscar_xpath.click()

    def checkBoxesTest(self):
        driver=self.driver
        buscar_xpath=driver.find_element(By.XPATH,"//a[@href='/checkboxes']")
        buscar_xpath.click()

    def contextMenuTest(self):
        driver=self.driver
        buscar_xpath=driver.find_element(By.XPATH,"//a[@href='/context_menu']")
        buscar_xpath.click()



