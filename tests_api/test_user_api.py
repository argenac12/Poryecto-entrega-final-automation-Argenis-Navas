import requests
import pytest

from utils.logger import logger

API_KEY = "reqres_56b9834632bd4d5f84a18597ad5ae4a9"
HEADERS = {"X-API-KEY": API_KEY}

@pytest.mark.api
def test_get_users_page_1():

    logger.info("Obteniendo la lista de usuarios de la página 1 a través de la API")
    url = "https://reqres.in/api/users?page=1"
    r = requests.get(url, headers=HEADERS)

    logger.info("Verificando la respuesta de la API")
    assert r.status_code == 200

    data = r.json()

    logger.info("Verificando el contenido de la respuesta")
    assert data["page"] == 1
    assert len(data["data"]) > 0

    for user in data["data"]:
        logger.info(f"Verificando el usuario con ID: {user['id']}")
        assert user["avatar"].endswith(".jpg")