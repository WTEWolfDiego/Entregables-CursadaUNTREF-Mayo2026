#SOTO JONATAN DNI N° 41.118.434

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    """Fixture que gestiona el ciclo de vida del navegador anulando carteles de Chrome."""
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
    """Función para iniciar sesión."""
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
   
    boton_login = driver.find_element(By.ID, "login-button")
    driver.execute_script("arguments[0].click();", boton_login)


# ============
# CASO 1
# ============

def test_caso1_ordenar_precios(driver):
    """Caso 1: loguearse, ordenar de menor a mayor el precio y verificar que los productos estén ordenados."""
    login_usuario(driver)
    
    menu_orden = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container"))
    )
    menu_orden.click()
    
    driver.find_element(By.CSS_SELECTOR, "option[value='lohi']").click()
    time.sleep(1)
    
    elementos_precio = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precios_en_pantalla = [float(p.text.replace("$", "")) for p in elementos_precio]
    precios_ordenados_esperados = sorted(precios_en_pantalla)
    
    assert precios_en_pantalla == precios_ordenados_esperados, "Error: los precios no quedaron bien ordenados!!!"
    print("\nCaso 1 aprobado!!! Los productos se ordenaron de menor a mayor muy bien")



# ==========
# CASO 2
# ==========

def test_caso2_validar_checkout(driver):
    """Caso 2: agregar todo, ir al checkout y validar errores dinámicos de campos vacíos."""
    login_usuario(driver)
    
    botones_agregar = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//button[text()='Add to cart']"))
    )
    for boton in botones_agregar:
        driver.execute_script("arguments[0].click();", boton)
        
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    badge_carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    ).text
    assert badge_carrito == "6", f" Error: Se esperaban 6 productos y hay {badge_carrito}."
    
    boton_checkout = driver.find_element(By.ID, "checkout")
    driver.execute_script("arguments[0].click();", boton_checkout)
    
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Jona")
    
    boton_continue = driver.find_element(By.ID, "continue")
    driver.execute_script("arguments[0].click();", boton_continue)
    
   
    elemento_error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert "Error: Last Name is required" in elemento_error.text, "No se validó correctamente la falta de Apellido."
    
   
    driver.find_element(By.ID, "last-name").send_keys("Soto")
    
    boton_continue2 = driver.find_element(By.ID, "continue")
    driver.execute_script("arguments[0].click();", boton_continue2)
    
    
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h3[data-test='error']"), "Error: Postal Code is required")
    )
    
    elemento_error_final = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "Error: Postal Code is required" in elemento_error_final.text, "No se validó correctamente la falta de Código Postal."
    
    print("\nCaso 2 aprobado!!! Las reglas del checkout bloquean el paso y lanzan los errores correctos.")


# ===========
# CASO 3
# ===========
def test_caso3_flujo_compra_y_eliminacion(driver):
    """Caso 3: circuito completo de agregar, eliminar, reabastecer y finalizar compra."""
    login_usuario(driver)
    
    
    btn_backpack = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    driver.execute_script("arguments[0].click();", btn_backpack)
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    btn_remove = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "remove-sauce-labs-backpack"))
    )
    driver.execute_script("arguments[0].click();", btn_remove)
    
    badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(badges) == 0, "Error: el carrito debería estar vacío despues de la eliminación."
    
    btn_continue_shopping = driver.find_element(By.ID, "continue-shopping")
    driver.execute_script("arguments[0].click();", btn_continue_shopping)
    
    btn_light = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-bike-light"))
    )
    driver.execute_script("arguments[0].click();", btn_light)
    
    btn_bolt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    driver.execute_script("arguments[0].click();", btn_bolt)
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge_carrito == "2", f"Error: se esperaban 2 artículos y figuran {badge_carrito}."
    
    btn_checkout_final = driver.find_element(By.ID, "checkout")
    driver.execute_script("arguments[0].click();", btn_checkout_final)
    
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Jonatan")
    driver.find_element(By.ID, "last-name").send_keys("Soto")
    driver.find_element(By.ID, "postal-code").send_keys("1425")
    
    btn_continue_checkout = driver.find_element(By.ID, "continue")
    driver.execute_script("arguments[0].click();", btn_continue_checkout)
    
    
    boton_finish = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "finish"))
    )
    driver.execute_script("arguments[0].click();", boton_finish)
    
    texto_confirmacion = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text
    assert "Thank you for your order!" in texto_confirmacion, "Error: no se detectó la pantalla final de éxito de compra."
    
    print("\nCaso 3 aprobado!!! Flujo completo operado con éxito.")