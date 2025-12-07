import pytest
import requests

from utils.logger import logger

API_KEY = "reqres_56b9834632bd4d5f84a18597ad5ae4a9"
HEADERS = {"X-API-KEY": API_KEY}
LOGIN_URL = "https://reqres.in/api/login"

LOGIN_CASES = [
    ("eve.holt@reqres.in", "cityslicka", 200),
    ("eve.holt@reqres.in", "", 400)
]

@pytest.mark.api
@pytest.mark.parametrize("email,password,expected_status", LOGIN_CASES)
def test_login_api(email, password, expected_status):
    
    logger.info(f"Probando login API con email: {email} y password: {'<empty>' if not password else password}")
    payload = {"email": email}
    if password:
        payload["password"] = password

    resp = requests.post(LOGIN_URL, json=payload, headers=HEADERS)

    logger.info(f"Verificando que el status code sea {expected_status}")
    assert resp.status_code == expected_status

    if expected_status == 200:
        logger.info("Verificando que el token esté presente en la respuesta")
        assert "token" in resp.json()