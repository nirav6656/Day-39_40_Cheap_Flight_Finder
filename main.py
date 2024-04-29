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

running_parameters = {
        "price":{
            "IATA Code": "PRS"
        }
    }
trial = requests.put(url="https://api.sheety.co/ce03a24dd7107449001e616b7fe7ac4c/flightDeals/prices/2",headers=header,json=running_parameters)
print(trial.content)
