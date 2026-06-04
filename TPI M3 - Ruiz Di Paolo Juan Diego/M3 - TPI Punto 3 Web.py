import pytest
import pytest_html
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import re
import base64

def espera_elemento(driver,tipo_selector,selector,timeout=10):
    try:
        web_element=WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((tipo_selector, selector)))
        return web_element
    except:
        print(f"❌ Fallo al buscar el elemento con el selector {selector}")
        driver.quit()
        raise

def espera_elementos(driver,tipo_selector,selector,timeout=10):
    try:
        web_elements=WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located((tipo_selector, selector)))
        return web_elements
    except:
        print(f"❌ Fallo al buscar los elementos con el selector {selector}")
        driver.quit()
        raise
    
def scroll_elemento(driver,elemento):
    driver.execute_script("arguments[0].scrollIntoView();", elemento)

def scroll_inicio(driver):
    driver.execute_script("window.scrollTo(0, 0);")

def scroll_fin(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def espera_explicita(tiempo):
    time.sleep(tiempo)

def capturar_imagen_reporte(driver,nombre,extras):
    driver.save_screenshot(nombre)
    #extras.append(pytest_html.extras.image(nombre))
    with open(nombre, "rb") as img: #Esto es para embeber la imagen y evitar que este ligado a un archivo
        encoded = base64.b64encode(img.read()).decode("utf-8")
    extras.append(pytest_html.extras.image(f"data:image/png;base64,{encoded}"))

def inicializar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    return driver

def saucedemo_login_standard_user(driver):
    input_username = espera_elemento(driver,By.ID,"user-name") 
    input_username.send_keys("standard_user")
    input_password = espera_elemento(driver,By.ID,"password") 
    input_password.send_keys("secret_sauce")
    btn_login = espera_elemento(driver,By.ID,"login-button")
    btn_login.click()
    espera_explicita(3)
    #Se genera nueva pestaña para pasar el pop up usando redireccionamiento. No me funcionaron los argumentos, ni los experimentales.
    url_actual = driver.current_url
    driver.execute_script(f"window.open('{url_actual}', '_blank');")
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])




def test_saucedemo_verificar_ordenamiento_caso_uno(extras):
    driver = inicializar_driver()
    saucedemo_login_standard_user(driver)
    selector_ordenamiento=Select(espera_elemento(driver,By.XPATH,"//select[@data-test='product-sort-container']"))
    print(f"✅ El Login se realizo de forma exitosa")
    selector_ordenamiento.select_by_value("lohi")
    lista_precio_productos = espera_elementos(driver,By.XPATH,"//div[@data-test='inventory-item-price']")
    precio_inicial=float(lista_precio_productos[0].text.replace("$",""))
    lista_precio_productos.pop(0)
    for precio in lista_precio_productos:
        precio_siguiente=float(precio.text.replace("$",""))
        if precio_inicial<=precio_siguiente:
            precio_inicial=precio_siguiente
        else:
            print(f"❌ No se cumple el ordenamiento de menor a mayor, siendo el previo {precio_inicial} y el posterior {precio_siguiente} ")
            raise
    print(f"✅ Se cumple el ordenamiento de menor a mayor según el precio de los productos")
    capturar_imagen_reporte(driver,"caso_uno.png",extras)

def test_saucedemo_verificar_errores_caso_dos(extras):
    driver = inicializar_driver()
    saucedemo_login_standard_user(driver)
    productos_nombre = espera_elementos(driver,By.XPATH,"//div[@data-test='inventory-item-name']")
    listado_nombre_productos = []
    for producto in productos_nombre:
        listado_nombre_productos.append(producto.text)
    productos_a_agregar=espera_elementos(driver,By.XPATH,"//button[text()='Add to cart']")
    for producto in productos_a_agregar:
        producto.click()
    capturar_imagen_reporte(driver,"caso_dos_productos.png",extras)
    espera_elemento(driver,By.XPATH,"//a[@data-test='shopping-cart-link']").click()
    scroll_inicio(driver)
    espera_elemento(driver,By.XPATH,"//span[text()='Your Cart']")
    productos_nombre_en_carrito=espera_elementos(driver,By.XPATH,"//div[@data-test='inventory-item-name']")
    capturar_imagen_reporte(driver,"caso_dos_carrito.png",extras)
    for i in range (0,len(listado_nombre_productos)):
        if (listado_nombre_productos[i] == productos_nombre_en_carrito[i].text):
            print(f"✅ El producto {listado_nombre_productos[i]} se agrego correctamente")
        else:
            print(f"❌ El producto {listado_nombre_productos[i]} que se encontraba en el listado no se añadio al carrito")
            raise
    scroll_fin(driver)
    espera_elemento(driver,By.XPATH,"//button[@data-test='checkout']").click()
    espera_elemento(driver,By.XPATH,"//input[@data-test='firstName']").send_keys("Juan")
    espera_elemento(driver,By.XPATH,"//input[@id='continue']").click()
    mensaje_error_falta_apellido=espera_elemento(driver,By.XPATH,"//h3[@data-test='error']").text
    capturar_imagen_reporte(driver,"caso_dos_falta_apellido.png",extras)
    if (mensaje_error_falta_apellido == "Error: Last Name is required"):
        print(f"✅ El mensaje de error es correcto: Error: Last Name is required ")
    else:
        print(mensaje_error_falta_apellido)
        print(f"❌ El mensaje no de Error: Last Name is required no esta, o tiene otro valor")
        raise
    espera_elemento(driver,By.XPATH,"//input[@data-test='lastName']").send_keys("Ruiz")
    espera_elemento(driver,By.XPATH,"//input[@id='continue']").click()
    mensaje_error_falta_cp=espera_elemento(driver,By.XPATH,"//h3[@data-test='error']").text
    capturar_imagen_reporte(driver,"caso_dos_falta_cp.png",extras)
    if (mensaje_error_falta_cp == "Error: Postal Code is required"):
        print(f"✅ El mensaje de error es correcto: Error: Postal Code is required ")
    else:
        print(mensaje_error_falta_cp)
        print(f"❌ El mensaje no de Error: Postal Code is required no esta, o tiene otro valor")
        raise

def test_saucedemo_verificar_compra_caso_tres(extras):
    p1=0 #Se añade como variable para que sea mas simple de ajustar de ser necesario
    p2=1
    p3=2
    driver = inicializar_driver()
    saucedemo_login_standard_user(driver)
    productos_nombre = espera_elementos(driver,By.XPATH,"//div[@data-test='inventory-item-name']")
    listado_nombre_productos = []
    for producto in productos_nombre:
        listado_nombre_productos.append(producto.text)
    productos_a_agregar=espera_elementos(driver,By.XPATH,"//button[text()='Add to cart']")
    productos_a_agregar[p1].click()
    espera_elemento(driver,By.XPATH,"//a[@data-test='shopping-cart-link']").click()
    scroll_inicio(driver)
    espera_elemento(driver,By.XPATH,"//span[text()='Your Cart']")
    productos_nombre_en_carrito=espera_elementos(driver,By.XPATH,"//div[@data-test='inventory-item-name']")
    capturar_imagen_reporte(driver,"caso_tres_carrito_con_producto.png",extras)
    assert productos_nombre_en_carrito[p1].text == listado_nombre_productos[p1], f"❌ El producto no se agrego correctamente"
    print(f"✅ El producto {productos_nombre_en_carrito[p1].text} se agrego correctamente ")
    espera_elemento(driver,By.XPATH,"//button[text()='Remove']").click()
    espera_explicita(2)
    try:
        driver.find_element(By.XPATH,"//div[@class='inventory_item_name']//parent::a")
        print("❌ Siguen existiendo productos en el carrito")
        raise
    except:
        print(f"✅ Se elimino el producto y el carrito se encuentra vacio ")
        capturar_imagen_reporte(driver,"caso_tres_carrito_vacio.png",extras)
    espera_elemento(driver,By.XPATH,"//button[@data-test='continue-shopping']").click()
    productos_a_agregar=espera_elementos(driver,By.XPATH,"//button[text()='Add to cart']")
    productos_a_agregar[p2].click()
    productos_a_agregar[p3].click()
    espera_elemento(driver,By.XPATH,"//a[@data-test='shopping-cart-link']").click()
    scroll_inicio(driver)
    espera_elemento(driver,By.XPATH,"//span[text()='Your Cart']")
    espera_elemento(driver,By.XPATH,"//button[@data-test='checkout']").click()
    espera_elemento(driver,By.XPATH,"//input[@data-test='firstName']").send_keys("Juan")
    espera_elemento(driver,By.XPATH,"//input[@data-test='lastName']").send_keys("Ruiz")
    espera_elemento(driver,By.XPATH,"//input[@data-test='postalCode']").send_keys("2900")
    espera_elemento(driver,By.XPATH,"//input[@data-test='continue']").click()
    productos_nombre_en_carrito=espera_elementos(driver,By.XPATH,"//div[@data-test='inventory-item-name']")
    if (productos_nombre_en_carrito[0].text == listado_nombre_productos[p2] and productos_nombre_en_carrito[1].text == listado_nombre_productos[p3]):
        print(f"✅ Los dos productos se encuentran en el carrito")
    else:
        print(productos_nombre_en_carrito[0].text+ "gtes2")
        print(listado_nombre_productos[p2] + "gtes")
        print(productos_nombre_en_carrito[1].text)
        print(f"❌ Los productos {listado_nombre_productos[p2]} y {listado_nombre_productos[p3]} no se encuentran en el carrito ")
        raise
    items_precios = espera_elementos(driver,By.XPATH,"//div[@data-test='inventory-item-price']")
    precio = 0
    for item in items_precios:
        precio += float(item.text.replace("$",""))
    precio_calculado=float(re.findall(r"\d+\.\d+",espera_elemento(driver,By.XPATH,"//div[@data-test='subtotal-label']").text)[0])
    if(precio==precio_calculado):
        print(f"✅ El precio calculado es correcto ${precio_calculado}")
    else:
        print(f"❌ El precio calculado {precio_calculado} no es igual a la sumatoria {precio} ")
        raise
    capturar_imagen_reporte(driver,"caso_tres_checkout.png",extras)
    espera_elemento(driver,By.XPATH,"//button[@data-test='finish']").click()
    rta_final=espera_elemento(driver,By.XPATH,"//h2[@data-test='complete-header']").text
    if rta_final == "Thank you for your order!":
        print(f"✅ Éxito en la compra")
    else:
        print(f"❌ Falló en la compra ")
        raise
    capturar_imagen_reporte(driver,"caso_tres_msg_final.png",extras)


    

    


