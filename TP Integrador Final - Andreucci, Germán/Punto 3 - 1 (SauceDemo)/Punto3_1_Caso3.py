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


### Se agrega un elemento al carrito
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)


### Ir al carrito
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)


### Se elimina el artículo del carrito
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
time.sleep(1)


### Verificar que el sitio no tiene artículos agregados 
### Usamos 'find_elements' (en plural) para verificar que la lista esté vacía sin que se rompa el script.
items_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
assert len(items_badge) == 0, "Error: El carrito debería estar vacío, pero aún registra elementos"
time.sleep(1)


### Ir a “Continue Shopping”
driver.find_element(By.ID, "continue-shopping").click()
time.sleep(1)


### Se agregan 2 elementos
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(1)
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
time.sleep(1)


### Ir al carrito por 2da vez
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)


### Se verifica que esten los 2 productos en el carrito
contador_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
assert contador_carrito == "2", f"Error: Se esperaban 6 productos, pero se ven: {contador_carrito}"
time.sleep(1)


### Ir al checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(1)


### Ingresar nombre, y clickear "Continue"
driver.find_element(By.ID, "first-name").send_keys("Peperino")
time.sleep(1)
driver.find_element(By.ID, "last-name").send_keys("Pómoro")
time.sleep(1)
driver.find_element(By.ID, "postal-code").send_keys("8238")
time.sleep(1)
driver.find_element(By.ID, "continue").click()
time.sleep(1)


### Finalización de la compra
driver.find_element(By.ID, "finish").click()
time.sleep(2)


### Verificar que la compra fue realizada
### Al finalizar la compra con éxito, SauceDemo muestra el texto "Thank you for your order!" dentro de la clase 'complete-header
mensaje_final = driver.find_element(By.CLASS_NAME, "complete-header").text
assert "Thank you for your order!" in mensaje_final, "Error: La orden de compra no pudo ser procesada o verificada"
time.sleep(1)


if "Thank you for your order!" in mensaje_final:
    print("¡Compra de los 2 productos realizada con éxito!")


### Cierra el navegador al finalizar
driver.quit()