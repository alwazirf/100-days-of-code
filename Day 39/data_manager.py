from pprint import pprint
import requests
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.__authorization = os.getenv("AUTHORIZATION")
        self.__shettyurl = os.getenv("SHETTY_URL")
        self.headers = {
            "Authorization": self.__authorization
        }
        self.destination_data = {}
        
    def get_detination_data(self) -> None:
        response = requests.get(url=self.__shettyurl, headers=self.headers)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data
    
    def update_destination_codes(self) -> None:
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode" : city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.__shettyurl}/{city['id']}",
                headers=self.headers,
                json=new_data
                )
            print(response.text)
