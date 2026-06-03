import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    option = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    option.add_experimental_option("prefs", prefs)
    option.add_argument("--disable-save-password-bubble")
    
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
def login_usuario(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
def test_ordenar_productos(driver):
    login_usuario(driver)
    driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    driver.find_element(By.CSS_SELECTOR, "option[value='lohi']").click()
    precio = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precios = [float(p.text.replace("$", "")) for p in precio]
    assert precios == sorted(precios)
    print(f"(Caso 1)Los elementos se encuentran ordenados por precio de menor a mayor")
def test_agregar_productos(driver):
    login_usuario(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "6" 
    print(f"(Caso 2)Los 6 productos se encuentran en el carrito de compras")
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Jonatan")
    driver.find_element(By.ID, "continue").click()
    mensaje_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert mensaje_error == "Error: Last Name is required"
    print(f"(Caso 2)Se muestra el mensaje de error al no ingresar el apellido")
    driver.find_element(By.ID, "last-name").send_keys("Castillo")
    driver.find_element(By.ID, "continue").click()
    mensaje_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert mensaje_error == "Error: Postal Code is required"
    print(f"(Caso 2)Se muestra el mensaje de error al no ingresar el código postal")
def test_flujo_completo(driver):
    login_usuario(driver)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    assert " " in driver.page_source
    print(f"(Caso 3)No hay productos en el carrito de compras")
    driver.find_element(By.ID, "continue-shopping").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "2" 
    print(f"(Caso 3)Los 2 productos se encuentran en el carrito de compras")
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Jonatan")
    driver.find_element(By.ID, "last-name").send_keys("Castillo")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    assert "Checkout: Overview" in driver.page_source
    print(f"(Caso 3)Se muestra la página de resumen de la compra")
    driver.find_element(By.ID, "finish").click()
    msj_compraexitosa = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert "Thank you for your order!" in msj_compraexitosa
    print(f"(Caso 3)Se muestra el mensaje de compra exitosa")