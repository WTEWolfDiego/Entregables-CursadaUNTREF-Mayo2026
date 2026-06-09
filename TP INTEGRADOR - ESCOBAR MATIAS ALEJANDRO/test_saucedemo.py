import pytest
import time
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()


def login_usuario(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.ID, "login-button")
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

# CASO 1

def test_caso1_ordenar_precios(driver):
    """Caso 1: login, ordenar productos de menor a mayor precio y verificar el orden."""
    login_usuario(driver)

    menu_orden = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )
    menu_orden.click()
    driver.find_element(By.CSS_SELECTOR, "option[value='lohi']").click()
    time.sleep(1)

    elementos_precio = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precios_actuales = [float(p.text.replace("$", "")) for p in elementos_precio]

    assert precios_actuales == sorted(precios_actuales), \
        "Error: los precios no están ordenados de menor a mayor."

    print("\nCaso 1 aprobado: productos ordenados correctamente de menor a mayor precio.")

# CASO 2

def test_caso2_validar_errores_checkout(driver):
    """Caso 2: agregar todos los productos, ir al checkout y validar mensajes de error por campos vacíos."""
    login_usuario(driver)

    botones = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Add to cart']"))
    )
    for boton in botones:
        driver.execute_script("arguments[0].click();", boton)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    ).text
    assert badge == "6", f"Error: se esperaban 6 productos en el carrito, hay {badge}."

    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.ID, "checkout")
    )

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Matias")

    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.ID, "continue")
    )

    error1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert "Last Name is required" in error1.text, \
        "Error: no se detectó el mensaje de apellido requerido."

    driver.find_element(By.ID, "last-name").send_keys("Escobar")

    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.ID, "continue")
    )

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "h3[data-test='error']"),
            "Postal Code is required"
        )
    )
    error2 = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "Postal Code is required" in error2.text, \
        "Error: no se detectó el mensaje de código postal requerido."

    print("\nCaso 2 aprobado: los errores de validación del checkout funcionan correctamente.")

# CASO 3

def test_caso3_flujo_completo_compra(driver):
    """Caso 3: agregar producto, eliminarlo, volver, agregar dos nuevos y completar la compra."""
    login_usuario(driver)

    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
    )

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "remove-sauce-labs-backpack"))
        )
    )

    badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badges) == 0, "Error: el carrito debería estar vacío tras eliminar el producto."

    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.ID, "continue-shopping")
    )

    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light"))
        )
    )

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "2", f"Error: se esperaban 2 productos en el carrito, hay {badge}."

    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.ID, "checkout")
    )

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Matias")
    driver.find_element(By.ID, "last-name").send_keys("Escobar")
    driver.find_element(By.ID, "postal-code").send_keys("2000")

    driver.execute_script(
        "arguments[0].click();",
        driver.find_element(By.ID, "continue")
    )

    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "finish"))
        )
    )

    confirmacion = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text
    assert "Thank you for your order!" in confirmacion, \
        "Error: no se detectó la pantalla de confirmación de compra."

    print("\nCaso 3 aprobado: flujo completo de compra ejecutado con éxito.")