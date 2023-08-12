from pprint import pprint

import curlify
import requests


def print_console(first, second):
    print("{:>7} : {}".format(first, second))


class APIClient(requests.Session):
    base_url: str = ""

    def __init__(self):
        super(APIClient, self).__init__()
        self.hooks["response"].append(self._logging)

    @staticmethod
    def _logging(response: requests.Response, *args, **kwargs):
        """Function to handle logging in hook['response'] """
        print("\n----------- Request ----------->")
        print_console(response.request.method, response.request.url)
        print_console("HEADERS", response.request.headers)
        print_console("DEBUG", curlify.to_curl(response.request))
        if response.request.body is not None:
            print_console("BODY", response.request.body)

        print("<----------- Response -----------")
        print_console("STATUS", f"{response.status_code}, elapsed: {response.elapsed.total_seconds()}s",)

        print_console("HEADER", response.headers)
        if response.text != "":
            print_console("BODY", "")
            pprint(response.json())
