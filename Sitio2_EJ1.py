import requests

def test_caso1_api():

    response = requests.get(  "https://pokeapi.co/api/v2/berry/1")
      
    assert response.status_code == 200, \
        "La API no respondió correctamente"

    print("Respuesta exitosa de la API")

    datos = response.json()

    assert datos["size"] == 20, \
        "El tamaño de la berry debería ser 20"

    print("Validación correcta: size = 20")

    assert datos["soil_dryness"] == 15, \
        "El soil_dryness debería ser 15"

    print("Validación correcta: soil_dryness = 15")

    assert datos["firmness"]["name"] == "soft", \
        "La firmeza debería ser soft"

    print("Validación correcta: firmness.name = soft")
    
    #Para correr este test usar este comando en terminal: pytest Sitio2_EJ1.py -v -s
    #Para correrlo con reporte html: pytest Sitio2_EJ1.py -v -s --html=reportes/caso1_ej1.html --self-contained-html