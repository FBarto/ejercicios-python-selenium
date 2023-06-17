import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from HomePage import HomePage

class TestAddRemove(unittest.TestCase):
    
    def __init__(self, driver):
        self.driver =driver

    def testAddRemove(self):
        driver =self.driver
        i=0
        clickButtonAdd=driver.find_element(By.XPATH,"//button[contains(@onclick,'addElement()')]")
        i=3
        clickButtonAdd.click(i)
        if i>0:
            for i>0 in i-1:"Ver!!"
                clickButtonDelete=driver.find_element(By.XPATH,"(//button[@onclick='deleteElement()'])[%i]")




        