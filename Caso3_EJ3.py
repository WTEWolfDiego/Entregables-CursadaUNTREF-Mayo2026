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
def test_caso3(driver):

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    print("Login exitoso")

    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.CLASS_NAME, "cart_button").click()

    productos = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(productos) == 0, "El carrito no esta vacio"
    print("Carrito vacio")

    driver.find_element(By.ID, "continue-shopping").click()

    botones = driver.find_elements(By.CLASS_NAME, "btn_inventory")

    botones[0].click()
    botones[1].click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    productos = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(productos) == 2, "El carrito tiene que tener dos productos"
    print("Carrito con dos productos")

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Miguel")
    driver.find_element(By.ID, "last-name").send_keys("Gonzalez")
    driver.find_element(By.ID, "postal-code").send_keys("1000")

    driver.find_element(By.ID, "continue").click()

    driver.find_element(By.ID, "finish").click()

    mensaje = driver.find_element(By.CLASS_NAME,"complete-header").text
        
    assert mensaje == "Thank you for your order!"
    print("Compra exitosa")
    
    #Para correr este test usar este comando en terminar: pytest Caso3_EJ3.py -v -s
    #Para correrlo con reporte html: pytest Caso3_EJ3.py -v -