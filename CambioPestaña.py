import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class using_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def test_cambiar_venta(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open("");")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://www.youtube.com")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

    def test_pag_next_or_back(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.get("http://www.gmail.com")
        time.sleep(3)
        driver.get("http://www.youtube.com")
        time.sleep(3)
        driver.back()#Retorna a pagina anterior
        time.sleep(3)
        driver.back()#Retorna a pagina anterior
        time.sleep(3)
        driver.forward()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()

"""Cap 8 min 10:00"""