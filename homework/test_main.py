from fastapi.testclient import TestClient

from main import app

#import pytest

client = TestClient(app)

def test_hello_world():
	response = client.get('/')
	assert response.status_code == 200
	assert response.json() == {"message": "Hello World during the coronavirus pandemic!"}


def test_name_method_1():
	response = client.post('/method')
	assert response.status_code == 200
	assert response.json() == {"method": "POST"}


def test_name_method_2():
	response = client.get('/method/')
	assert response.status_code == 200
	assert response.json() == {"method": "GET"}


def test_name_method_3():
	response = client.delete('/method')
	assert response.status_code == 200
	assert response.json() == {"method": "DELETE"}

def test_name_method_4():
	response = client.put('/method')
	assert response.status_code == 200
	assert response.json() == {"method": "PUT"}


def test_name_method_5():
	response = client.options('/method/')
	assert response.status_code == 200
	assert response.json() == {"method": "OPTIONS"}


def test_patient_name():
	response = client.post("/patient", json={'name': 'IMIE',"surename": "NAZWISKO"})
	assert response.status_code == 200
	assert response.json() == {"id": 1, "patient": {"name": "IMIE", "surename": "NAZWISKO"}}
	response = client.post("/patient", json={'name': 'IMIE',"surename": "NAZWISKO"})
	assert response.status_code == 200
	assert response.json() == {"id": 2, "patient": {"name": "IMIE", "surename": "NAZWISKO"}}
