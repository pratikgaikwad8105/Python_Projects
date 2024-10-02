import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/ba44d205fe9d9838731a7ca45ef9a2cd/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.username = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
        self.basic_auth = HTTPBasicAuth(username=self.username, password=self.password)
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=SHEETY_ENDPOINT)
        sheet_response.raise_for_status()
        sheet_data = sheet_response.json()
        self.destination_data = sheet_data["prices"]

        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_city_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city["id"]}", json=new_city_data)
            # print(response.text)

