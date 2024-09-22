from dotenv import load_dotenv
import os
import requests

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.__api_key = os.getenv("FLIGHT_API_KEY")
        self.__api_secret = os.getenv("FLIGHT_API_SECRET")
        self.__url = os.getenv("FLIGHT_URL")
        self.__token = self._get_new_token()
    
    def _get_new_token(self):
        header = {
            'Content-type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.__api_key,
            'client_secret': self.__api_secret
        }
        
        response = requests.post(url=self.__url, headers=header, data=body)
        print(response.text)
        
        # Tambahkan pengecekan status kode
        if response.status_code == 200:
            try:
                print(f"Token Anda adalah {response.json()['access_token']}")
            except KeyError:
                print("Kunci 'access_token' tidak ditemukan dalam respons.")
                print("Isi respons:", response.json())
        else:
            print(f"Gagal mendapatkan token. Kode status: {response.status_code}")
            print("Isi respons:", response.text)
        
        return response.json()['access_token']
    
    def get_destination_code(self, city_name):
        headers = {
            'Authorization': f"Bearer {self.__token}"
        }
        
        query = {
            'keyword': city_name,
            'max': 2,
            'include': "AIRPORTS"
        }
        
        response = requests.get(
            url=os.getenv("IATA_ENDPOINT"),
            headers=headers,
            params=query
        )
        
        print(f"status code {response.status_code}, Airport IATA {response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        
        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "Authorization": f"Bearer {self.__token}"
        }
        
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }
        
        response = requests.get(url=self.__url, headers=headers, params=query)
        
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None
        
        return response.json()