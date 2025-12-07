import pytest
import requests
from datetime import datetime

from utils.logger import logger

CREATE_URL = "https://reqres.in/api/users"
API_KEY = "reqres_56b9834632bd4d5f84a18597ad5ae4a9"
HEADERS = {"X-API-KEY": API_KEY}

@pytest.mark.api
def test_create_user():
    logger.info("Creando un nuevo usuario a través de la API")
    payload = {'name': 'Axel QA', 'job': 'Automation Tester'}
    r = requests.post(CREATE_URL, json=payload, headers=HEADERS)

    logger.info("Verificando la respuesta de la API")
    assert r.status_code == 201
    body = r.json()

    logger.info("Verificando la información del nuevo usuario")
    assert body["name"] == "Axel QA"
    assert "id" in body
    assert "createdAt" in body

    logger.info("Verificando que la fecha de creación sea la actual")
    assert str(datetime.now().year) in body["createdAt"]