from selenium import webdriver
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def test_simple_alert(self):
        driver = self.driver
        driver.get("C:/Users/franc/curso selenium/AlertSimple.html")
        alerta_simple=driver.find_element(By.NAME,"alert").click()
        time.sleep(2)
        alerta_simple=driver.switch_to.alert#Cambia al contexto de la alerta
        alerta_simple.dismiss()#se utiliza para rechazar o aceptar la alerta
        confirm_alert=driver.find_element(By.NAME,"alertconfirm").click()
        confirm_alert = driver.switch_to.alert
        time.sleep(2)
        #confirm_alert.dismiss()#en este caso se utliza para CANCELAR la alerta
        confirm_alert.accept()#En este es para aceptar
        time.sleep(2)
        alert_prompt = driver.find_element(By.NAME, "promptconfirm").click()
        alert_prompt = driver.switch_to.alert
        alert_prompt.accept()



if __name__ == '__main__':
    unittest.main()
        