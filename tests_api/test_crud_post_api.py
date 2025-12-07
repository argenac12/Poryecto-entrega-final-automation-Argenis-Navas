import requests
from faker import Faker
import pytest

from utils.logger import logger

fake = Faker()

BASE = "https://jsonplaceholder.typicode.com/posts"

@pytest.fixture(scope="module")
def created_post():
    logger.info("Creando un nuevo post a través de la API")
    payload = {
        "title": fake.sentence(),
        "body": fake.paragraph(),
        "userId": 1
    }
    r = requests.post(BASE, json=payload)

    logger.info("Verificando la respuesta de la API")
    assert r.status_code == 201
    return r.json()

@pytest.mark.api
@pytest.mark.e2e
def test_patch_created_post(created_post):

    logger.info("Actualizando el post creado a través de la API")
    post_id = created_post["id"]
    patch_payload = {"title": "Updated Title QA Automation"}

    r = requests.patch(f"{BASE}/{post_id}", json=patch_payload)

    logger.info("Verificando la respuesta de la API después del patch")
    assert r.status_code == 200
    assert r.json()["title"] == "Updated Title QA Automation"

@pytest.mark.api
@pytest.mark.e2e
def test_delete_created_post(created_post):
    logger.info("Eliminando el post creado a través de la API")
    post_id = created_post["id"]

    r = requests.delete(f"{BASE}/{post_id}")
    logger.info("Verificando la respuesta de la API después del delete")
    assert r.status_code == 200

    logger.info("Verificando que el post haya sido eliminado")
    assert r.json() == {} or "id" not in r.json()