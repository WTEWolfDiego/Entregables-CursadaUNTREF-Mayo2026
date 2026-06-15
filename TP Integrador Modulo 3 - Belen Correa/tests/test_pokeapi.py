import pytest
import requests


BASE_URL = "https://pokeapi.co/api/v2"


class TestPokeAPI:
    """Tests de API para https://pokeapi.co/api/v2"""

    # Guardamos datos de berry/1 para reutilizar en el Caso 2
    _berry1_size = None
    _berry1_soil_dryness = None

    def test_caso1_berry_1(self):
        """
        Caso 1:
        - GET a /berry/1
        - Verificar size == 20
        - Verificar soil_dryness == 15
        - Verificar firmness.name == "soft"
        """
        response = requests.get(f"{BASE_URL}/berry/1")

        assert response.status_code == 200, (
            f"Se esperaba status 200, se obtuvo {response.status_code}"
        )

        data = response.json()

        # Guardamos para usar en caso 2
        TestPokeAPI._berry1_size = data["size"]
        TestPokeAPI._berry1_soil_dryness = data["soil_dryness"]

        assert data["size"] == 20, (
            f"Se esperaba size=20, se obtuvo size={data['size']}"
        )
        assert data["soil_dryness"] == 15, (
            f"Se esperaba soil_dryness=15, se obtuvo soil_dryness={data['soil_dryness']}"
        )
        assert data["firmness"]["name"] == "soft", (
            f"Se esperaba firmness.name='soft', se obtuvo '{data['firmness']['name']}'"
        )

    def test_caso2_berry_2(self):
        """
        Caso 2:
        - GET a /berry/2
        - Verificar firmness.name == "super-hard"
        - Verificar size > size de berry/1
        - Verificar soil_dryness == soil_dryness de berry/1
        """
        # Si el test anterior no corrió, obtenemos berry/1 igual
        if TestPokeAPI._berry1_size is None:
            r1 = requests.get(f"{BASE_URL}/berry/1")
            data1 = r1.json()
            TestPokeAPI._berry1_size = data1["size"]
            TestPokeAPI._berry1_soil_dryness = data1["soil_dryness"]

        response = requests.get(f"{BASE_URL}/berry/2")

        assert response.status_code == 200, (
            f"Se esperaba status 200, se obtuvo {response.status_code}"
        )

        data = response.json()

        assert data["firmness"]["name"] == "super-hard", (
            f"Se esperaba firmness.name='super-hard', se obtuvo '{data['firmness']['name']}'"
        )
        assert data["size"] > TestPokeAPI._berry1_size, (
            f"Se esperaba que el size de berry/2 ({data['size']}) "
            f"fuera mayor al de berry/1 ({TestPokeAPI._berry1_size})"
        )
        assert data["soil_dryness"] == TestPokeAPI._berry1_soil_dryness, (
            f"Se esperaba soil_dryness={TestPokeAPI._berry1_soil_dryness} "
            f"(igual al de berry/1), se obtuvo {data['soil_dryness']}"
        )

    def test_caso3_pikachu(self):
        """
        Caso 3:
        - GET a /pokemon/pikachu
        - Verificar base_experience > 10 y < 1000
        - Verificar que su tipo es "electric"
        """
        response = requests.get(f"{BASE_URL}/pokemon/pikachu/")

        assert response.status_code == 200, (
            f"Se esperaba status 200, se obtuvo {response.status_code}"
        )

        data = response.json()

        base_exp = data["base_experience"]
        assert 10 < base_exp < 1000, (
            f"Se esperaba 10 < base_experience < 1000, se obtuvo {base_exp}"
        )

        types = [t["type"]["name"] for t in data["types"]]
        assert "electric" in types, (
            f"Se esperaba que Pikachu tuviera tipo 'electric', tipos obtenidos: {types}"
        )
