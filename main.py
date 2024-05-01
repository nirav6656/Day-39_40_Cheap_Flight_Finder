#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import os
from flight_search import FlightSearch
from pprint import pprint


# header = {
#     "Authorization": AUTHORIZATION
# }

# response = requests.get(url="https://api.sheety.co/ce03a24dd7107449001e616b7fe7ac4c/flightDeals/prices",headers=header)
# sheety_response = response.json()
#
# sheet_data = sheety_response["prices"]
# print(sheet_data)



# url = 'https://api.sheety.co/ce03a24dd7107449001e616b7fe7ac4c/flightDeals/prices'
# body = {
#     "price": {
#         "City": "hello"
#     }
# }



# for city in sheet_data:
#             new_data = {
#                 "price": {
#                     "iataCode": "hello"
#                 }
#             }
#             response = requests.put(
#                 url=f"{url}/{city['id']}",
#                 headers=header,
#                 json=new_data
#             )
#             print(response.content)


flight_search = FlightSearch()