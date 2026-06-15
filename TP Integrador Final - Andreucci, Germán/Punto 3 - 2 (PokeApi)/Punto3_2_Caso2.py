### Se importan las librerías necesarias para trabajar con peticiones HTTP
import requests
from Punto3_2_Caso1 import size_caso1, soil_dryness_caso1


url_2  = "https://pokeapi.co/api/v2/berry/2"   ### URL de la API
respuesta2 = requests.get(url_2 )   ### Petición GET a la URL
data_2 = respuesta2.json()   ### Conversión de la respuesta a formato JSON 


### Verificar que en firmness, el "name" sea "super-hard".
firmness_name_caso2 = data_2["firmness"]["name"]
assert firmness_name_caso2 == "super-hard", f"Error: Se esperaba que firmness name sea 'super-hard', pero la API devolvió: {firmness_name_caso2}"


### Verificar que el size sea mayor al del punto anterior (Caso 1)
### Se utiliza el size del Caso 1 que se importa al comienzo del script
### Se aplica comparativa lógica (>) contra la variable del Caso 1' size_caso1
size_caso2 = data_2["size"]
assert size_caso2 > size_caso1, f"Error: El size actual ({size_caso2}) no es mayor al del punto anterior ({size_caso1})"


### Verificar que el "soil_dryness" sea igual al del Caso 1
### Se utiliza el soil dryness del Caso 1 que se importa al comienzo del script
### Se aplica comparativa lógica (==) contra la variable del Caso 1' soil_dryness_caso1
soil_dryness_caso2 = data_2["soil_dryness"]
assert soil_dryness_caso2 == soil_dryness_caso1, f"Error: El soil_dryness del caso 2 es distinto al del caso 1"


if firmness_name_caso2 == "super-hard" and size_caso2 > size_caso1 and soil_dryness_caso2 == soil_dryness_caso1:
    print(f"-> Size del caso 2: {size_caso2}")
    print(f"-> Dryness del caso 2: {soil_dryness_caso2}")