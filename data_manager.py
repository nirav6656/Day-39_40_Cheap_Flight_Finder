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
        self.get_sheet_data()
        self.update_iataCode()

    def get_sheet_data(self):
        sheet_data_response = requests.get(
            url=f"{SHEETY_API_ENDPOINT}",
            headers=header
        )
        sheet_data = sheet_data_response.json()
        self.destination_data = sheet_data["prices"]
        print(self.destination_data)
    def update_iataCode(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": "hejo"
                }
            }
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city['id']}",
                headers=header,
                json=new_data
            )
            print(response.content)
