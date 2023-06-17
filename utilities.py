from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buscar_elemento(driver, by, value, timeout=10):
    """
    Busca un elemento web utilizando el criterio de búsqueda especificado y espera implícitamente hasta que esté presente.

    Args:
        driver (WebDriver): Instancia del controlador del navegador.
        by (str): Criterio de búsqueda (por ejemplo, "id", "xpath", "css_selector").
        value (str): Valor del criterio de búsqueda.
        timeout (int): Tiempo de espera máximo en segundos (predeterminado: 10).

    Returns:
        WebElement: El elemento web encontrado.

    Raises:
        TimeoutException: Si el elemento no está presente después de esperar el tiempo máximo.
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, value)))


def buscar_elemento_interactable(driver, by, value, timeout=10):
    """
    Busca un elemento web utilizando el criterio de búsqueda especificado y espera implícitamente hasta que sea interactuable.

    Args:
        driver (WebDriver): Instancia del controlador del navegador.
        by (str): Criterio de búsqueda (por ejemplo, "id", "xpath", "css_selector").
        value (str): Valor del criterio de búsqueda.
        timeout (int): Tiempo de espera máximo en segundos (predeterminado: 10).

    Returns:
        WebElement: El elemento web encontrado y interactuable.

    Raises:
        TimeoutException: Si el elemento no es interactuable después de esperar el tiempo máximo.
    """
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable((by, value)))