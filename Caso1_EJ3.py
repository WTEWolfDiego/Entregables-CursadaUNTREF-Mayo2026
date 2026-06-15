import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
import time

@pytest.fixture() 
def driver():

    opciones = webdriver.ChromeOptions()

    opciones.add_argument("--incognito")
    opciones.add_argument("--disable-notifications")
    opciones.add_argument("--disable-save-password-bubble")

    driver = webdriver.Chrome(options=opciones)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    yield driver

    driver.quit()

def test_caso1(driver):

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    print("Login realizado correctamente")

    # Seleccionar precio menor a mayor
    lista = driver.find_element(By.CLASS_NAME, "product_sort_container")
    Select(lista).select_by_value("lohi")

    print("Los precios se ordenaron de menor a mayor")

    # Obtener precios de los productos
    elementos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    precios = []

    for e in elementos:
        numero = float(e.text.replace("$", ""))
        precios.append(numero)

    print("Precios:", precios)

    # Validar orden de precios
    assert precios == sorted(precios), \
        "Los productos no están ordenados de menor a mayor precio"

    print("los productos están ordenados correctamente")
    
    #Para correr este test usar este comando en terminar: pytest Caso1_EJ3.py -v -s 
    #Para correrlo con reporte html: pytest Caso1_EJ3.py -v -s --html=reportes/caso1_ej3.html --self-contained-html