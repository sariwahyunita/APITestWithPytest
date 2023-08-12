from assertpy import assert_that

from api_client.base import APIClient


class FavoriteAPI(APIClient):
    def __init__(self, email, password):
        super(FavoriteAPI, self).__init__()
        self.base_url = "https://airportgap.dev-tester.com/api/favorites"
        self.token = ""
        self.email = email
        self.password = password

    def login(self):
        token = self.post("https://airportgap.dev-tester.com/api/tokens", data={
            "email": self.email,
            "password": self.password
        })
        assert_that(token.status_code).is_equal_to(200)
        assert_that(token.json()).contains_key("token")
        token_value = token.json().get("token")
        assert_that(token_value).is_not_empty()
        self.headers["Authorization"] = f"Token {token_value}"
        return token.json().get("token")

    def get_all(self):
        return self.get(self.base_url)

    def update_favorite_note(self, id_airport_to_modify, new_note):
        return self.patch(f"{self.base_url}/{id_airport_to_modify}", data=new_note)
