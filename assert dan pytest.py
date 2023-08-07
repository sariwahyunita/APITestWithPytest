import requests
from assertpy import assert_that


class TestAirports:
    def test_get_all_airports(self):
        response = requests.get('https://airportgap.dev-tester.com/api/airports')
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json().get("data")).is_not_empty()

    def test_get_airport_detail(self):
        airport_id = "MAG"
        response = requests.get(f'https://airportgap.dev-tester.com/api/airports/{airport_id}')
        assert_that(response.status_code).is_equal_to(200)
        data = response.json().get("data")
        assert_that(data.get("attributes").get("name")).is_equal_to("Madang Airport")
        assert_that(data["attributes"]["country"]).is_equal_to("Papua New Guinea")

    def test_get_airport_not_found(self):
        airport_id = "JKT"
        response = requests.get(f'https://airportgap.dev-tester.com/api/airports/{airport_id}')
        assert_that(response.status_code).is_equal_to(404)
        assert_that(response.json()).contains_key("errors")
        assert_that(response.text).contains("The page you requested could not be found")


class TestAirportDistance:
    def test_calculate_distance(self):
        airports = {
            "from": "LAE",
            "to": "GKA"
        }
        response = requests.post('https://airportgap.dev-tester.com/api/airports/distance', data=airports)
        assert_that(response.status_code).is_equal_to(200)
        data = response.json().get("data")
        assert_that(data).is_not_empty()
        assert_that(data["id"]).is_equal_to("LAE-GKA")
        assert_that(data["attributes"]["kilometers"]).is_equal_to(157.10152842469589)

    def test_calculate_invalid(self):
        airports = {
            "from": "JKT",
            "to": "GKA"
        }
        response = requests.post('https://airportgap.dev-tester.com/api/airports/distance', data=airports)
        assert_that(response.status_code).is_equal_to(422)
        assert_that(response.json()).contains_key("errors")
        assert_that(response.text).contains("Please enter valid 'from' and 'to' airports.")
