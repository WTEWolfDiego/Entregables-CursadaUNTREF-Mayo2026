# Se importan las librerías necesarias para trabajar con selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


### Inicialización del navegador
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(1)


### El usuario se loguea al sitio como usuario standard_user
### Encontramos los campos y nos logueamos en la web. Visto en la clase 13.
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element(By.ID, "login-button").click()
time.sleep(1)


### Incorporar al carrito todos los elementos
### Buscamos todos los botones que tengan la clase 'btn_inventory' (los 6 productos)
### Se incorpora en cada selección del producto una espera de 5ms para que la página pueda procesar 
### los cambios al agregar cada producto al carrito
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(1)


### Ir al carrito; se busca por CLASS NAME en este caso
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(3)


### Se verifica que esten los 6 productos en el carrito
contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
assert contador_carrito == "6", f"Error: Se esperaban 6 productos, pero se ven: {contador_carrito}"
time.sleep(1)


### Ir al checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(1)


### Ingresar nombre, y clickear "Continue"
driver.find_element(By.ID, "first-name").send_keys("Peperino")
time.sleep(1)
driver.find_element(By.ID, "continue").click()
time.sleep(1)


###  Verificar que aparece el error “Error: Last Name is required”
### Se asigna el .text a una variable usando el XPATH del elemento
mensaje = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
### Validación estricta con mensaje opcional por si falla
assert "Error: Last Name is required" in mensaje, "El mensaje de error de apellido no coincide o no apareció"
time.sleep(1)


### Ingresar un apellido y clickear “Continue”
driver.find_element(By.ID, "last-name").send_keys("Pómoro")
time.sleep(1)
driver.find_element(By.ID, "continue").click()
time.sleep(1)


### Verificación del error “Error: Postal Code is required”
### Reutilizamos la variable 'mensaje' re-escaneando el elemento h3 de error actualizado
mensaje = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
assert "Error: Postal Code is required" in mensaje, "El mensaje de error de código postal no coincide o no apareció"
time.sleep(1)


### Ingreso del código postal faltante y clickear “Continue”
driver.find_element(By.ID, "postal-code").send_keys("8238")
time.sleep(1)
driver.find_element(By.ID, "continue").click()
time.sleep(1)  


### Cierra el navegador al finalizar
driver.quit()