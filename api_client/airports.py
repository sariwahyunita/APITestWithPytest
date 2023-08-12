from api_client.base import APIClient


class AirportAPI(APIClient):
    def __init__(self):
        super().__init__()
        self.base_url = "https://airportgap.dev-tester.com/api/airports"

    def get_all(self):
        return self.get(self.base_url)

    def get_by_id(self, id):
        return self.get(f"{self.base_url}/{id}")

    def calculate(self, from_airport, to_airport):
        payload = {
            "from": from_airport,
            "to": to_airport
        }
        return self.post(self.base_url+"/distance", data=payload)
