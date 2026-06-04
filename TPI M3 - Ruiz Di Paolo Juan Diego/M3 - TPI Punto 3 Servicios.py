import requests
import pytest

def poke_api_berry(berry):
    r = requests.get(f"https://pokeapi.co/api/v2/berry/{berry}")
    print(f"Escenario: PokeApi - Se ejecuta get /berry/{berry}")
    return r.json()

def poke_api_pokemon(pokemon):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    print(f"Escenario: PokeApi - Se ejecuta get /pokemon/{pokemon}")
    return r.json()
    

def test_poke_api_berry_uno(): 
    datos = poke_api_berry(1)
    size_esperado=20
    soil_dryness_esperado=15
    firmness_name_esperado="soft"
    assert datos["size"]==size_esperado, f"El valor es de size es {datos["size"]} es distinto del esperado {size_esperado}"
    print(f"✅ El size es el esperado {datos["size"]}") 
    assert datos["soil_dryness"]==soil_dryness_esperado, f"El valor es de soil_dryness es {datos["soil_dryness"]} es distinto del esperado {soil_dryness_esperado}"
    print(f"✅ El soil_dryness es el esperado {datos["soil_dryness"]}") 
    assert datos["firmness"]["name"]==firmness_name_esperado, f"El valor es de frimness name es {datos["firmness"]["name"]} es distinto del esperado {firmness_name_esperado}"
    print(f"✅ El frimness name es el esperado {datos["firmness"]["name"]}") 

def test_poke_api_berry_dos(): 
    datos = poke_api_berry(2)
    size_esperado_mayor_a=20
    soil_dryness_esperado=15
    firmness_name_esperado="super-hard"
    assert datos["size"]>size_esperado_mayor_a, f"El valor es de size es {datos["size"]} es menor o igual a {size_esperado_mayor_a}"
    print(f"✅ El size es {datos["size"]} mayor a {size_esperado_mayor_a} por {datos["size"] - size_esperado_mayor_a}") 
    assert datos["soil_dryness"]==soil_dryness_esperado, f"El valor es de soil_dryness es {datos["soil_dryness"]} es distinto del esperado {soil_dryness_esperado}"
    print(f"✅ El soil_dryness es el esperado {datos["soil_dryness"]}") 
    assert datos["firmness"]["name"]==firmness_name_esperado, f"El valor es de frimness name es {datos["firmness"]["name"]} es distinto del esperado {firmness_name_esperado}"
    print(f"✅ El frimness name es el esperado {datos["firmness"]["name"]}") 

def test_poke_api_pokemon_pikachu():
    datos = poke_api_pokemon("pikachu")
    base_experience_esperado_mayor_a=10
    base_experience_esperado_menor_a=1000
    tipo_eperado="electric"
    assert (datos["base_experience"]>base_experience_esperado_mayor_a and datos["base_experience"]<base_experience_esperado_menor_a), f"El valor de base_experience es {datos["base_experience"]} que no se encuentra dentro del rango esperado ({base_experience_esperado_mayor_a};{base_experience_esperado_menor_a})"
    print(f"✅ El valor de base experience es {datos["base_experience"]} y se encuentra dentro del rango esperado ({base_experience_esperado_mayor_a};{base_experience_esperado_menor_a})") 
    assert datos["types"][0]["type"]["name"]==tipo_eperado, f"El tipo es {datos["types"][0]["type"]["name"]} que es distinto del esperado {tipo_eperado}"
    print(f"✅ El tipo es el esperado {datos["types"][0]["type"]["name"]}") 



