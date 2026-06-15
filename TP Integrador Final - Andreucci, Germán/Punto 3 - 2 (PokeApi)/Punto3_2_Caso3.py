### Se importa las librería necesaria para trabajar la petición HTTP
import requests


### Inicialización de la URL y obtención de datos de la API
url_3 = "https://pokeapi.co/api/v2/pokemon/pikachu/"
respuesta3 = requests.get(url_3)
### Convertimos la respuesta del servidor en un formato JSON (diccionario) para poder leer sus datos
data_pikachu = respuesta3.json()


### Se accede a la base experience y se la compara para ver si es mayor a 10 y menos a 1000 usando método assert
exp_base = data_pikachu["base_experience"]
assert exp_base > 10, f"Error: Experiencia base debía ser mayor a 10, pero se obtuvo: {exp_base}"
assert exp_base < 1000, f"Error: Experiencia base debía ser menor a 1000, pero se obtuvo: {exp_base}"


### Se verifica el tipo de "personaje" que es Pikachu
tipo_pikachu = data_pikachu["types"][0]["type"]["name"]
assert tipo_pikachu == "electric", f"Error: Se esperaba el tipo 'electric', pero la API devolvió: {tipo_pikachu}"


if exp_base > 10 and exp_base < 1000 and tipo_pikachu == "electric":
    print(f"-> Experiencia base de Pilachu en el caso 3: {exp_base}")
    print(f"-> Tipo de Pikachu en el caso 3: {tipo_pikachu}")