import pytest
from assertpy import assert_that

from api_client.airports import AirportAPI


@pytest.fixture()
def airport_api():
    return AirportAPI()


def test_get_all_airports(airport_api):
    response = airport_api.get_all()
    assert_that(response.status_code).is_equal_to(200)
    total_airports = len(response.json().get("data"))
    assert_that(total_airports).is_greater_than(5)


def test_get_one_airport(airport_api):
    airport_id = "LAE"
    response = airport_api.get_by_id(airport_id)
    data = response.json().get('data')
    data_airport = data["attributes"]
    assert_that(response.status_code).is_equal_to(200)
    assert_that(data_airport["name"]).is_equal_to("Nadzab Airport")


def test_get_not_found_airport(airport_api):
    airport_id = "NOTFOUND"
    response = airport_api.get_by_id(airport_id)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.json()).contains_key("errors")
    assert_that(response.text).contains("The page you requested could not be found")


def test_calculate_distance(airport_api):
    response = airport_api.calculate(from_airport="LAE", to_airport="NRT")
    data = response.json().get("data")
    assert_that(data["type"]).is_equal_to("airport_distance")
    assert_that(data["attributes"]).is_not_empty()
    assert_that(data).has_id("LAE-NRT")
    assert_that(data["attributes"]["kilometers"]).is_equal_to(4753.834755437252)
