import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """
    Abre el navegador Chrome antes de cada test y lo cierra al terminar.
    """
    opciones = Options()
    opciones.add_argument("--headless=new")        
    opciones.add_argument("--window-size=1920,1080")

    navegador = webdriver.Chrome(options=opciones)
    navegador.implicitly_wait(10)                  # espera hasta 10 segundos a que aparezcan los elementos

    yield navegador                                # acá se ejecuta el test

    navegador.quit()                               # cierra el navegador al finalizar
