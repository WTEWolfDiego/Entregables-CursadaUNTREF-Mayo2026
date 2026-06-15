### Se importa la librería necesaria para trabajar con peticiones HTTP
import requests


### Inicialización de la URL y obtención de datos de la API
url_1 = "https://pokeapi.co/api/v2/berry/1"
respuesta = requests.get(url_1)
### Convertimos la respuesta del servidor en un formato JSON (diccionario) para poder leer sus datos
data_1 = respuesta.json()


### Verificar que el "size" sea 20
size_caso1 = data_1["size"]
assert size_caso1 == 20, f"Error: Se esperaba un size de 20 pero se obtuvo {size_caso1}"


### Verificar que el "soil_dryness" sea 15
soil_dryness_caso1 = data_1["soil_dryness"]
assert soil_dryness_caso1 == 15, f"Error: Se esperaba un soil_dryness de 15 pero se obtuvo {soil_dryness_caso1}"


### Verificar que en firmness el "name" sea "soft".
firmness_name_caso1 = data_1["firmness"]["name"]
assert firmness_name_caso1 == "soft", f"Error: Se esperaba que la firmeza sea 'soft', pero la API devolvió: {firmness_name_caso1}"


if __name__ == "__main__":     ### Para evitar que el print se ejecute en el Caso 2 también
    if size_caso1 == 20 and soil_dryness_caso1 == 15 and firmness_name_caso1 == "soft":
        print("berry/1 de Poke API validado con éxito")