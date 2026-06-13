import requests

def test_caso_uno():
    response = requests.get("https://pokeapi.co/api/v2/berry/1").json()  
    assert response["size"]==20, "El tamaño es distinto de 20"
    print(f"El response tiene tamaño {response["size"]}")
    assert response["soil_dryness"]==15, "El soil_dryness es distinto de 15"
    print(f"El response tiene soil_dryness con valor {response["soil_dryness"]}")
    assert response["firmness"]["name"]=="soft", "El firmness.name es distinto de soft"
    print(f"El response tiene firmness.name con valor {response["firmness"]["name"]}")

def test_caso_dos():
    response = requests.get("https://pokeapi.co/api/v2/berry/2").json()  
    assert response["size"]>20, "El tamaño es menor o igual a 20"
    print(f"El response tiene tamaño {response["size"]}")
    assert response["soil_dryness"]==15, "El soil_dryness es distinto de 15"
    print(f"El response tiene soil_dryness con valor {response["soil_dryness"]}")
    assert response["firmness"]["name"]=="super-hard", "El firmness.name es distinto de super-hard"
    print(f"El response tiene firmness.name con valor {response["firmness"]["name"]}")

def test_caso_tres():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()  
    assert response["base_experience"]>10 and response["base_experience"]<1000, "La base_experience se encuentra entre (10,1000)"
    print(f"El response contiene base_experience con valor {response["base_experience"]}")
    assert response["types"][0]["type"]["name"]=="electric", "Es de tipo electric"
    print(f"El response contiene types.type.name con valor {response["types"][0]["type"]["name"]}")

