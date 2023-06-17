import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import time


class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\dcrhome\chromedriver_win32\chromedriver.exe")

    def test_using_opencv(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.save_screenshot('img2.png')  # guarda una captura de pantalla de la página
        time.sleep(3)

    def test_comparate_screen(self):
        img1 = cv2.imread("C:/Users/franc/curso selenium/img1.png")  # variable para guardar la imagen a comparar
        img2 = cv2.imread('img2.png')
        if img1 is None or img2 is None:
            print("Error al cargar las imágenes")
            return
        #no estan cargando las imagenes
        dif = cv2.absdiff(img1, img2)  # hacemos la comparación de imágenes
        imagen_gris = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)  # convertir a escala de grises para comparar mejor
        contours, _ = cv2.findContours(imagen_gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Hacemos una colección de datos

        for c in contours:
            if cv2.contourArea(c) >= 20:  # entre menos rango, más propenso a errores
                posicion_x, posicion_y, ancho, alto = cv2.boundingRect(c)  # Con esta línea encontramos la diferencia
                cv2.rectangle(img1, (posicion_x, posicion_y), (posicion_x + ancho, posicion_y + alto), (0, 0, 255), 2)
                # Con esta línea dibujamos la diferencia

        while True:
            cv2.imshow('imagen 1', img1)
            cv2.imshow('imagen 2', img2)
            cv2.imshow('Diferencias detectadas', dif)
            teclado = cv2.waitKey(5) & 0xFF #Salimos del programa con tecla ESC
            if teclado == 27:
                break
        cv2.destroyAllWindows()


if __name__ == "__main__":
    unittest.main()





