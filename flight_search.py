import requests
import os
KIWI_API_ENDPOINT = os.environ["KIWI_API_ENDPOINT"]
KIWI_API_KEY = os.environ["KIWI_API_KEY"]
kiwi_header = {
    "apikey" : KIWI_API_KEY
}
kiwi_api = KIWI_API_ENDPOINT
inputs = {
    "term":"Paris",
    "accept": "application/json",
    "active_only":"true",
    "location_types":"airport"
}
class FlightSearch:
    def __init__(self):
        self.get_iata_code()

    def get_iata_code(self):
        kiwi_response = requests.get(url=kiwi_api, headers=kiwi_header, params=inputs).json()
        print(kiwi_response["locations"][0]["id"])

