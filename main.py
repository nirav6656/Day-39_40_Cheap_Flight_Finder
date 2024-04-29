#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from flight_search import FlightSearch
from pprint import pprint

AUTHORIZATION = os.environ["AUTHORIZATION"]
header = {
    "Authorization": AUTHORIZATION
}

response = requests.get(url="https://api.sheety.co/ce03a24dd7107449001e616b7fe7ac4c/flightDeals/prices",headers=header)
sheety_response = response.json()

sheet_data = sheety_response["prices"]
print(sheet_data)
# for items_in_sheet_data in sheet_data:
#     iatadata = items_in_sheet_data["iataCode"]
#     flight_search_data = FlightSearch(iatadata)
#     items_in_sheet_data["iataCode"] = flight_search_data.iatadata
#     running_parameters = {
#         "Flight Deals":{
#             "City": items_in_sheet_data["city"],
#             "IATA Code": items_in_sheet_data["iataCode"],
#             "Lowest Price": items_in_sheet_data["lowestPrice"]
#         }
#     }
#     trial = requests.put(url="https://api.sheety.co/ce03a24dd7107449001e616b7fe7ac4c/flightDeals/prices/1",headers=header,params=running_parameters)
#     print(trial.content)



url = 'https://api.sheety.co/ce03a24dd7107449001e616b7fe7ac4c/flightDeals/prices'
body = {
    "price": {
        "City": "hello"
    }
}

# response = requests.put(url, json=body,headers=header)
#
# if response.status_code == 200:
#     json_data = response.json()
#     # Do something with the JSON object
#     print(json_data['price'])
#     print(response.text)
# else:
#     print("Error:", response.status_code)

for city in sheet_data:
            new_data = {
                "price": {
                    "iataCode": "hello"
                }
            }
            response = requests.put(
                url=f"{url}/{city['id']}",
                headers=header,
                json=new_data
            )
            print(response.content)