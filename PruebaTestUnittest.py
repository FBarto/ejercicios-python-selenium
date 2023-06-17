import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def test_buscar(self):    
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)
        element=driver.find_element(By.NAME,"q")
        element.send_keys("selenium")
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        assert"No se encontro el Element" not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()