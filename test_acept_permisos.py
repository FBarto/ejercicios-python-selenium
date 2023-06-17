import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import cv2
import time

class UsingUnittest(unittest.TestCase):

    #def setUp(self):
     #   self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def test_permisos(self):
        opc = Options()# enviar argunmentos(1 permitiendo la noti, 2 bloqueando la noti)
        opc.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 1})#En este caso son Noti, pero se pueden aplicar para todos los permisos
        driver = webdriver.Chrome(chrome_options=opc,executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe" )        
        driver.get("https://developer.mozilla.org/es/docs/Web/API/notification")

if __name__ == '__main__':
    unittest.main()