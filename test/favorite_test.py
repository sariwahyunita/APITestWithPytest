import pytest
from assertpy import assert_that
from faker import Faker

from api_client.favorite import FavoriteAPI


@pytest.fixture(scope="session")
def favorite_api():
    api = FavoriteAPI(email="naruto@mailinator.com", password="shuriken")
    api.login()
    return api


def test_get_favorite(favorite_api):
    response = favorite_api.get_all()
    data = response.json().get("data")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(len(data)).is_greater_than_or_equal_to(1)


def test_update_favorite_note(favorite_api):
    before_add = favorite_api.get_all()
    data_before = before_add.json().get("data")
    assert_that(len(data_before)).is_greater_than(0)
    id_airport_to_modify = data_before[0]["id"]
    # Add dynamic note
    fake = Faker()
    new_note = {
        "note": fake.sentence()
    }

    response = favorite_api.update_favorite_note(id_airport_to_modify, new_note)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.text).contains(new_note["note"])

    after_add = favorite_api.get_all()
    data_after = after_add.json().get("data")
    for airport_data in data_after:
        if airport_data["id"] == id_airport_to_modify:
            print(f"Found the modified airport {id_airport_to_modify}")
            print("\nHere is the check for specific airport in an array data")
            assert_that(airport_data["attributes"]["note"]).is_equal_to(new_note["note"])
