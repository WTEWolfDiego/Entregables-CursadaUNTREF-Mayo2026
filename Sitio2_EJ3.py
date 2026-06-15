import requests

def test_caso3_api():

    response = requests.get(
        "https://pokeapi.co/api/v2/pokemon/pikachu/"
    )

    assert response.status_code == 200, \
        "La API no respondió correctamente"

    print("Si es pikachu :D")
#convertimos la respuesta a JSON para validar los datos y buscar la información que necesitamos
    Pikachu = response.json()

    # Validar experiencia base , usamos >< para validar datos 
    assert Pikachu["base_experience"] > 10, \
        "La experiencia base debería ser mayor a 10"

    assert Pikachu["base_experience"] < 1000, \
        "La experiencia base debería ser menor a 1000"

    print(f"Experiencia base validada: {Pikachu['base_experience']}")

    # Validar tipo
    assert Pikachu["types"][0]["type"]["name"] == "electric", \
        "El tipo de Pikachu debería ser electric"

    print("Tipo: electric")

#Para correr este test usar este comando en terminal: pytest Sitio2_EJ3.py -v -s
#Para correrlo con reporte html: pytest Sitio2_EJ3.py -v -s --html=reportes/caso1_ej3.html --self-contained-html