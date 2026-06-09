import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_berry1():
    respuesta = requests.get(f"{BASE_URL}/berry/1")
    assert respuesta.status_code == 200
    datos = respuesta.json()
    assert datos["size"] == 20
    assert datos["soil_dryness"] == 15
    assert datos["firmness"]["name"] == "soft"

def test_berry2():
    ref = requests.get(f"{BASE_URL}/berry/1").json()
    size_ref = ref["size"]
    dryness_ref = ref["soil_dryness"]

    resp = requests.get(f"{BASE_URL}/berry/2")
    assert resp.status_code == 200
    datos = resp.json()
    assert datos["firmness"]["name"] == "super-hard"
    assert datos["size"] > size_ref
    assert datos["soil_dryness"] == dryness_ref

def test_pikachu():
    resp = requests.get(f"{BASE_URL}/pokemon/pikachu")
    assert resp.status_code == 200
    datos = resp.json()
    exp = datos["base_experience"]
    assert 10 < exp < 1000
    tipos = [t["type"]["name"] for t in datos["types"]]
    assert "electric" in tipos