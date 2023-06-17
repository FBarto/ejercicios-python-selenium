import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def test_using_Explicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")
        body = driver.find_element(By.TAG_NAME,"body").send_keys(Keys.END)
        try: # intenta
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"L2AGLb")))
        #cargame en elemento lo que tengas en google intentalo hasta 10 veces, hasta que el elemento Q este presente t lo carga en EC
        finally:
            driver.quit()

    def test_using_implicit_wait(self):#le damos un rango de espera
        driver = self.driver 
        driver.implicitly_wait(5)#espera 5 seg
        driver.get("http://www.google.com")
        myDynamicElement = driver.find_element(By.NAME,"q")# componente dinamico, cambia su nombre o id, cuando se carga/consulta/mandamos a llamar.



if __name__ == "__main__":
    unittest.main()