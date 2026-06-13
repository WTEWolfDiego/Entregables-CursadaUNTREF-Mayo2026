import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import base64
import time

def inicializar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1450")
    driver = webdriver.Chrome(options=options)
    return driver

def eliminar_popup_seguridad(driver):
    url = driver.current_url
    driver.execute_script(f"window.open('{url}', '_blank');")
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def obtener_elemento(driver,selector):
    try:
        web_element=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
        return web_element
    except:
        print(f"No se encontro el elemento con el selector {selector}")
        driver.quit()
        raise

def elemento_no_visible(driver,selector):
    try:
         WebDriverWait(driver, 10).until_not(EC.visibility_of_element_located((By.ID, selector)))
    except:
        print(f"El elemento continua visible")
        driver.quit()
        raise

def imagen(driver,nombre,extras):
    driver.save_screenshot(nombre)
    with open(nombre, "rb") as img:
        encoded = base64.b64encode(img.read()).decode("utf-8")
    extras.append(pytest_html.extras.image(f"data:image/png;base64,{encoded}"))

def test_caso_uno(extras):
    driver=inicializar_driver()
    driver.get("https://www.saucedemo.com/")
    obtener_elemento(driver,"//input[@data-test='username']").send_keys("standard_user")
    obtener_elemento(driver,"//input[@data-test='password']").send_keys("secret_sauce")
    obtener_elemento(driver,"//input[@data-test='login-button']").click()
    orden=Select(obtener_elemento(driver,"//select[@data-test='product-sort-container']"))
    print("Se ingreso con éxito")
    orden.select_by_value("lohi")
    precios_desde_elemento=driver.find_elements(By.XPATH,"//div[@data-test='inventory-item-price']")
    precios=[]
    for precio in precios_desde_elemento:
        precios.append(float(precio.text.replace("$","")))
    aux=precios[0]
    for precio in precios:
        if aux<=precio:
            aux=precio
        else:
            raise AssertionError(f"El precio {precio} fue menor que {aux} por lo que no esta ordenado de mayor a menor")
    print("Se encuentra ordenado por precios de menor a mayor")
    imagen(driver,"caso1",extras)

def test_caso_dos(extras):
    driver=inicializar_driver()
    driver.get("https://www.saucedemo.com/")
    obtener_elemento(driver,"//input[@data-test='username']").send_keys("standard_user")
    obtener_elemento(driver,"//input[@data-test='password']").send_keys("secret_sauce")
    obtener_elemento(driver,"//input[@data-test='login-button']").click()
    obtener_elemento(driver,"//span[@data-test='title']")
    time.sleep(3)
    eliminar_popup_seguridad(driver)
    obtener_elemento(driver,"//span[@data-test='title']")
    elementos_carrito=driver.find_elements(By.XPATH,"//div[@class='pricebar']//button")
    cantidad_items=len(elementos_carrito)
    for elemento in elementos_carrito:
        elemento.click()
    obtener_elemento(driver,"//a[@data-test='shopping-cart-link']").click()
    cantidad_items_carrito=len(driver.find_elements(By.XPATH,"//div[@data-test='inventory-item']"))
    assert cantidad_items==cantidad_items_carrito, "La cantidad de productos del catalogo no es la misma que en el carrito"
    print("Se agregaron los productos del catalogo")
    imagen(driver,"caso2_carrito",extras)
    obtener_elemento(driver,"//button[@data-test='checkout']").click()
    obtener_elemento(driver,"//input[@data-test='firstName']").send_keys("Giuliana")
    obtener_elemento(driver,"//input[@id='continue']").click()
    error_falta_lastname=obtener_elemento(driver,"//h3[@data-test='error']").text
    assert error_falta_lastname == "Error: Last Name is required" , "No se visualiza el error esperado"
    print(f"Se visualiza el error {error_falta_lastname}")
    imagen(driver,"caso2_error_falta_apellido",extras)
    obtener_elemento(driver,"//input[@data-test='lastName']").send_keys("Torrico")
    obtener_elemento(driver,"//input[@id='continue']").click()
    time.sleep(2)
    error_falta_cp=obtener_elemento(driver,"//h3[@data-test='error']").text
    assert error_falta_cp == "Error: Postal Code is required" , "No se visualiza el error esperado"
    print(f"Se visualiza el error {error_falta_cp}")
    imagen(driver,"caso2_error_falta_cod_postal",extras)

def test_caso_tres(extras):
    driver=inicializar_driver()
    driver.get("https://www.saucedemo.com/")
    obtener_elemento(driver,"//input[@data-test='username']").send_keys("standard_user")
    obtener_elemento(driver,"//input[@data-test='password']").send_keys("secret_sauce")
    obtener_elemento(driver,"//input[@data-test='login-button']").click()
    obtener_elemento(driver,"//span[@data-test='title']")  
    eliminar_popup_seguridad(driver)
    obtener_elemento(driver,"//span[@data-test='title']")
    elementos_carrito=driver.find_elements(By.XPATH,"//div[@class='pricebar']//button")
    elementos_carrito[0].click()
    obtener_elemento(driver,"//a[@data-test='shopping-cart-link']").click()
    cantidad_items_carrito=len(driver.find_elements(By.XPATH,"//div[@data-test='inventory-item']"))
    assert cantidad_items_carrito==1, "El producto se añadio al carrito"
    imagen(driver,"caso3_producto_en_carrito",extras)
    obtener_elemento(driver,"//div[@class='item_pricebar']//button").click()
    elemento_no_visible(driver,"//div[@class='pricebar']//button")
    print("Se elimino el producto agregado")
    imagen(driver,"caso3_carrito_vacio",extras)
    obtener_elemento(driver,"//button[@data-test='continue-shopping']").click()
    obtener_elemento(driver,"//span[@data-test='title']")  
    elementos_carrito=driver.find_elements(By.XPATH,"//div[@class='pricebar']//button")
    elementos_carrito[0].click()
    elementos_carrito[1].click()
    obtener_elemento(driver,"//a[@data-test='shopping-cart-link']").click()
    time.sleep(3)
    cantidad_items_carrito=len(driver.find_elements(By.XPATH,"//div[@data-test='inventory-item']"))
    assert cantidad_items_carrito==2, "El producto se añadio al carrito"
    imagen(driver,"caso3_producto_en_carrito_2",extras)
    obtener_elemento(driver,"//button[@data-test='checkout']").click()
    obtener_elemento(driver,"//input[@data-test='firstName']").send_keys("Giuliana")
    obtener_elemento(driver,"//input[@data-test='lastName']").send_keys("Torrico")
    obtener_elemento(driver,"//input[@data-test='postalCode']").send_keys("1419")
    obtener_elemento(driver,"//input[@id='continue']").click()
    imagen(driver,"caso3_confirmacion",extras)
    obtener_elemento(driver,"//button[@data-test='finish']").click()
    mensaje_compra = obtener_elemento(driver,"//h2[@data-test='complete-header']").text
    assert mensaje_compra == "Thank you for your order!", "No se logro concretar la orden de compra"
    print(f"Se realizo la orden correctamente, se visualiza {mensaje_compra}")



       