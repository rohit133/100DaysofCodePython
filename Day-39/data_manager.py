from pprint import pprint
import requests

GOOGLE_SHEET_ENPOINT = "https://api.sheety.co/aaf08ad8b427ddd2ff059a068f2952f7/flightDeals/prices/"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    
    def get_destination_data(self):
        response = requests.get(url=GOOGLE_SHEET_ENPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            print(city)
            new_data= {
                "price":{
                    "iataCode": city["iataCode"]
                }
            }
            response_update = requests.put(url=f"{GOOGLE_SHEET_ENPOINT}/{city['id']}",json=new_data)
            print(response_update.text)