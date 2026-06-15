import requests


def test_caso2_api():

    # Obtener berry 1
    response_berry1 = requests.get(
        "https://pokeapi.co/api/v2/berry/1"
    )

    # Obtener berry 2
    response_berry2 = requests.get(
        "https://pokeapi.co/api/v2/berry/2"
    )

    # Convertir respuestas a JSON
    berry1 = response_berry1.json()
    berry2 = response_berry2.json()

    print("Consultas realizadas correctamente")

    # Validar firmness
    assert berry2["firmness"]["name"] == "super-hard", \
        "La firmeza de berry/2 debería ser super-hard"

    print("Correcto, firmness = super-hard")

    # Validar tamaño mayor
    assert berry2["size"] > berry1["size"], \
        "El tamaño de berry/2 es mayor al de berry/1"
    print(f"Correcto, size = {berry2['size']} es mayor que {berry1['size']}")
        
    
    # Validar soil_dryness igual
    assert berry2["soil_dryness"] == berry1["soil_dryness"], \
        "El soil_dryness debería ser igual al de berry/1"

    print(f"Correcto, soil_dryness = {berry2['soil_dryness']}")

    #Para correr este test usar este comando en terminal: pytest Sitio2_EJ2.py -v -s
    #Para correrlo con reporte html: pytest Sitio2_EJ2.py -v -s --html=reportes/caso1_ej2.html --self-contained-html