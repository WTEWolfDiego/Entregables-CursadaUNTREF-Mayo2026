### Se importan las librerías necesarias para trabajar con selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


### Inicialización del navegador
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(1)


### Encontramos los campos y nos logueamos en la web. Visto en la clase 13.
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element(By.ID, "login-button").click()
time.sleep(1)


### Localización del filtro selección de la opción de menor a mayor 
filtro_elemento = driver.find_element(By.CLASS_NAME, "product_sort_container")
filtro_dropdown = Select(filtro_elemento)
filtro_dropdown.select_by_visible_text("Price (low to high)") #Visto en la clase 14
time.sleep(2)


### Capturamos todos los elementos de texto que tienen los precios
elementos_precio = driver.find_elements(By.CLASS_NAME, "inventory_item_price")


### Armamos una lista de números (floats) quitando el signo "$" para poder compararlos
precios = [float(elem.text.replace("$", "")) for elem in elementos_precio]


### Validamos que la lista esté igual a su versión ordenada de menor a mayor 
assert precios == sorted(precios), "Los precios no quedaron ordenados de menor a mayor"


print("Los productos en SauceDemo se ordenaron correctamente de menor a mayor.")


### Cierra el navegador al finalizar
driver.quit()