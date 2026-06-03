import requests
import pytest

base_url = "https://pokeapi.co/api/v2"
def test_get_berr1():
    response = requests.get(f"{base_url}/berry/1")
    assert response.status_code == 200, f"Status esperado 200, pero fue {response.status_code}"
    print("[Caso 1 OK] Status code es 200, prueba exitosa")
    json_data = response.json()
    assert json_data["size"] == 20, f"Clave 'size': 20 no encontrada en la respuesta JSON"
    print("[Caso 1 OK] Size = a 20 en la respuesta")
    assert json_data["soil_dryness"] == 15, f"Clave 'soil_dryness': 15 no encontrada en la respuesta JSON"
    print("[Caso 1 OK] 'soil_dryness' contiene valor 15 en la respuesta")
    assert json_data["firmness"]["name"] == "soft", f"Clave 'firmness' con valor 'soft' no encontrada en la respuesta JSON"
    print("[Caso 1 OK] 'firmness' contiene valor 'soft' en la respuesta")

def test_get_berry2():
    response = requests.get(f"{base_url}/berry/2")
    assert response.status_code == 200, f"Status esperado 200, pero fue {response.status_code}"
    print("[Caso 2 OK] Status code es 200, prueba exitosa")
    json_data = response.json()
    assert json_data["firmness"]["name"] == "super-hard", f"Clave 'firmness' con valor 'super-hard' no encontrada en la respuesta JSON"
    print("[Caso 2 OK] 'firmness' contiene valor 'super-hard' en la respuesta")
    assert json_data["size"] > 20, f"Clave 'size' con valor mayor a 20 no encontrada en la respuesta JSON"
    print("[Caso 2 OK] 'size' contiene valor mayor a 20 en la respuesta")
    assert json_data["soil_dryness"] == 15, f"Clave 'soil_dryness': 15 no encontrada en la respuesta JSON"
    print("[Caso 2 OK] 'soil_dryness' contiene valor 15 en la respuesta")

def test_get_pikachu():
    response = requests.get(f"{base_url}/pokemon/pikachu")
    assert response.status_code == 200, f"Status esperado 200, pero fue {response.status_code}"
    print("[Caso 3 OK] Status code es 200, prueba exitosa")
    json_data = response.json()
    b_exp = json_data.get("base_experience")
    assert 10 < b_exp < 1000, f"Clave 'base_experience' con valor entre 10 y 1000 no encontrada en la respuesta JSON"
    print("[Caso 3 OK] 'base_experience' contiene valor mayor a 10 y menor a 1000 en la respuesta")
    pok_types = [t["type"]["name"] for t in json_data["types"]]
    assert "electric" in pok_types, f"Clave 'types' con valor 'electric' no encontrada en la respuesta JSON"
    print("[Caso 3 OK] 'types' contiene valor 'electric' en la respuesta")