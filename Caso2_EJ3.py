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

def test_caso2(driver):

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    botones = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    time.sleep(2)
    for boton in botones:
        boton.click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    productos_carrito = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(productos_carrito) == 6
    print("Se agregaron 6 productos al carrito")

    driver.find_element(By.ID, "checkout").click()
   

    driver.find_element(By.ID, "first-name").send_keys("Miguelito")
    time.sleep(2)

    driver.find_element(By.ID, "continue").click()

    mensaje_error = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text

    assert "Error: Last Name is required" in mensaje_error
    print("Error apellido necesario")

    driver.find_element(By.ID, "last-name").send_keys("Gonzalez")
    time.sleep(2)
    
    driver.find_element(By.ID, "continue").click()

    mensaje_error = driver.find_element(By.CSS_SELECTOR, "[data-test=error]").text

    assert "Error: Postal Code is required" in mensaje_error
    print("Error codigo postal necesario")

    #Para correr este test usar este comando en terminar: pytest Caso2_EJ3.py -v -s
    #Para correrlo con reporte html: pytest Caso2_EJ3.py -v -s --html=reportes/caso2_ej3.html --self-contained-html