#SOTO JONATAN DNI N° 41.118.434

import pytest
import requests

BASE_URL = "https://pokeapi.co/api/v2"


# ===========
# CASO 1
# ===========
def test_caso1_berry_uno():
    """Caso 1: GET a berry/1 y validar tamaño, humedad y firmeza soft."""
    url = f"{BASE_URL}/berry/1"
    respuesta = requests.get(url)
    
    assert respuesta.status_code == 200, f"Error: se esperaba estado 200 y se obtuvo {respuesta.status_code}"
    
    datos = respuesta.json()
    
    assert datos["size"] == 20, f"Error: el tamaño esperado era 20 pero se obtuvo {datos['size']}"
    assert datos["soil_dryness"] == 15, f"Error: el soil_dryness esperado era 15 pero se obtuvo {datos['soil_dryness']}"
    assert datos["firmness"]["name"] == "soft", f"Error: la firmeza esperada era 'soft' pero se obtuvo '{datos['firmness']['name']}'"
    
    print("\nCaso 1 API aprobado!!! Los datos de berry/1 coinciden con la documentación oficial.")


# ===========
# CASO 2
# ===========
def test_caso2_berry_dos():
    """Caso 2: GET a berry/2 y validar firmeza super-hard comparando valores con berry/1."""
    datos_baya1 = requests.get(f"{BASE_URL}/berry/1").json()
    size_baya1 = datos_baya1["size"]
    humidity_baya1 = datos_baya1["soil_dryness"]
    
    url = f"{BASE_URL}/berry/2"
    respuesta = requests.get(url)
    assert respuesta.status_code == 200, f"Error: se esperaba estado 200 y se obtuvo {respuesta.status_code}"
    
    datos_baya2 = respuesta.json()
    
    assert datos_baya2["firmness"]["name"] == "super-hard", f"Error: la firmeza esperada era 'super-hard' pero se obtuvo '{datos_baya2['firmness']['name']}'"
    assert datos_baya2["size"] > size_baya1, f"Error: el tamaño de baya 2 ({datos_baya2['size']}) NO es mayor al de baya 1 ({size_baya1})"
    assert datos_baya2["soil_dryness"] == humidity_baya1, f"Error: el soil_dryness de baya 2 ({datos_baya2['soil_dryness']}) no es igual al de baya 1 ({humidity_baya1})"
    
    print("\nCaso 2 API aprobado!!!! Los análisis comparativos entre ambas bayas dieron OK.")


# ============
# CASO 3
# ============
def test_caso3_pikachu():
    """Caso 3: GET a pokemon/pikachu y validar rangos de experiencia y tipo eléctrico."""
    url = f"{BASE_URL}/pokemon/pikachu"
    respuesta = requests.get(url)
    assert respuesta.status_code == 200, f"Error: se esperaba estado 200 y se obtuvo {respuesta.status_code}"
    
    datos_pokemon = respuesta.json()
    
    exp_base = datos_pokemon["base_experience"]
    assert 10 < exp_base < 1000, f"Error: la experiencia base ({exp_base}) está fuera del rango permitido (10 a 1000)"
    
    
    lista_tipos = [t["type"]["name"] for t in datos_pokemon["types"]]
    assert "electric" in lista_tipos, f"Error: el pokémon no cuenta con el tipo 'electric'. Tipos encontrados: {lista_tipos}"
    
    print("\nCaso 3 API aprobado!!!! Pikachu cuenta con la experiencia en regla y el tipo 'electric' asignado.")