import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class using_unittest(unittest.TestCase):

    def setUp(self):
        configuracion = configparser.ConfigParser()
        configuracion.read('configuracion.ini')
        configuracion.sections()
        obtenerexplorer = configuracion['General']['chrome']
        self.page = configuracion['Paginas']['page']#self es un valor de retorno para póder utilizar este elemento en otra funcion
        self.driver = webdriver.Chrome(executable_path=obtenerexplorer)

    def test_using_impicit_wait(self):# impicit espera el tiempo que nosotros le indiquemos y luego continua
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(self.page)
        myDinamicElement=driver.find_element(By.NAME, "q")


if __name__ == '__main__':
    unittest.main()        