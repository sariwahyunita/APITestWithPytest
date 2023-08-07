import requests

def test_get_all_airports():
    response = requests.get('https://airportgap.dev-tester.com/api/airports')
    assert response.status_code == 200
    assert len(response.json().get("data")) == 35

def test_get_one_airport():
    airport_id = "MAG"
    response = requests.get(f'https://airportgap.dev-tester.com/api/airports/{airport_id}')
    assert response.status_code == 200
    data = response.json().get("data")
    assert data["id"] == "MAG"
    assert data["attributes"]["latitude"] == "-5.20708"


def test_get_one_airport_not_found():
    airport_id = "xxx"
    response = requests.get(f'https://airportgap.dev-tester.com/api/airports/{airport_id}')
    assert response.status_code == 404
    assert "The page you requested could not be found" in response.text


