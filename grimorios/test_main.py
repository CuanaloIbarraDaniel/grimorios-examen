from fastapi.testclient import TestClient
from unittest import TestCase
from piccolo.table import create_db_tables_sync, drop_db_tables_sync
from piccolo.conf.apps import Finder
from piccolo.utils.sync import run_sync
from .app import app

client = TestClient(app) 
TABLES = Finder().get_table_classes()

class TestApp(TestCase):
    def setUp(self):
        create_db_tables_sync(*TABLES)

    def tearDown(self):
        drop_db_tables_sync(*TABLES)

    def test_app(self):
        pass


def test_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ["Dev Screen"]

def test_post_error_empty_model():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={})
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "missing"

def test_post_error_nombre_string_too_long():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Danielsssssssssssssssssssssssssssssss",
        "apellido": "Cuanalo",
        "identificacion": "F514JDH",
        "edad": 24,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_too_long"


def test_post_error_nombre_string_too_short():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "",
        "apellido": "Cuanalo",
        "identificacion": "F514JDH",
        "edad": 24,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_too_short"


def test_post_error_nombre_string_pattern_mismatch():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Armando Dani3l",
        "apellido": "Cuanalo",
        "identificacion": "F514JDH",
        "edad": 24,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_pattern_mismatch"

def test_post_error_apellido_string_too_long():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Daniel",
        "apellido": "Cuanalosssssssssssssssssssssssssssssssssssss",
        "identificacion": "F514JDH",
        "edad": 24,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_too_long"


def test_post_error_apellido_string_too_short():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Daniel",
        "apellido": "",
        "identificacion": "F514JDH",
        "edad": 24,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_too_short"


def test_post_error_apellido_string_pattern_mismatch():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Armando Daniel",
        "apellido": "Cuanal0",
        "identificacion": "F514JDH",
        "edad": 24,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_pattern_mismatch"

def test_post_error_identificacion_string_too_long():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Daniel",
        "apellido": "Cuanalos",
        "identificacion": "F514JDHj9gji0qighbiwrhi",
        "edad": 24,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_too_long"


def test_post_error_identificacion_string_too_short():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Daniel",
        "apellido": "Cuanalo",
        "identificacion": "",
        "edad": 24,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_too_short"


def test_post_error_identificacion_string_pattern_mismatch():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Armando Daniel",
        "apellido": "Cuanal0",
        "identificacion": "F514$JDH",
        "edad": 24,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_pattern_mismatch"


def test_post_error_edad_string_too_long():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Daniel",
        "apellido": "Cuanalos",
        "identificacion": "F514JDH",
        "edad": 0,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "greater_than"


def test_post_error_edad_string_too_short():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Daniel",
        "apellido": "Cuanalo",
        "identificacion": "F514JDH",
        "edad": 100,
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "less_than"


def test_post_error_edad_string_pattern_mismatch():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Armando Daniel",
        "apellido": "Cuanal0",
        "identificacion": "F514JDH",
        "edad": "44",
        "afinidad_magica": "Luz"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_pattern_mismatch"

def test_post_error_afinidad_string_pattern_mismatch():
    response = client.post("/solicitud", headers={"X-Token": "coneofsilence"}, json={
        "id": 0,
        "nombre": "Armando Daniel",
        "apellido": "Cuanal0",
        "identificacion": "F514JDH",
        "edad": 44,
        "afinidad_magica": "Metal"
    })
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "string_pattern_mismatch"

def test_put_empty_body():
    response = client.put("/solicitud/5", headers={"X-Token": "coneofsilence"}, json={})
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "missing"

def test_patch_empty_body():
    response = client.patch("/solicitud/1/estatus?SolicitudEstatus=", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 400
    assert response.json()["detalles"][0]["type"] == "int_parsing"

def test_delete_empty_body():
    response = client.delete("/solicitud/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 400
    assert response.json() == {'detalles': '405: Method Not Allowed'}