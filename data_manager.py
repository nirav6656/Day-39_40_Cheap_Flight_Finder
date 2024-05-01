import requests
import os
SHEETY_API_ENDPOINT = os.environ["SHEETY_API_ENDPOINT"]
AUTHORIZATION = os.environ["AUTHORIZATION"]
header = {
    "Authorization": AUTHORIZATION
}
class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.update_iataCode()

    def get_sheet_data(self):
        sheet_data_response = requests.get(
            url=f"{SHEETY_API_ENDPOINT}",
            headers=header
        )
        sheet_data = sheet_data_response.json()
        print()
    def update_iataCode(self):

        response = requests.put(
            url=f"{SHEETY_API_ENDPOINT}",
            headers=header
        )

