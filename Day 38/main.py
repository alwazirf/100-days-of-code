import requests
from datetime import date, datetime
import json

API_KEY = '886946032a03331787cfa3c6e42df5ec'
APP_ID = '345c799c'
URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHETTY_URL = 'https://api.sheety.co/5a9a2b313e30429a0176a49230dd8714/workouts/workouts'
WEIGHT_KG = 63
HEIGHT_CM = 166
AGE = 25


headers = {
    'x-app-key' : API_KEY,
    'x-app-id': APP_ID
}

user_input = input('Tell me which exercise you did: ')

parameters = {
    "query": user_input,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

today_date = datetime.now().strftime('%d/%m/%Y')
time_now = datetime.now().strftime('%H:%M:%S')

response = requests.post(url=URL, headers=headers, json=parameters)
response.raise_for_status()
data = response.json()

shetty_headers = {
    "Content-Type": "application/json"
}

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    shetty_res = requests.post(url=SHETTY_URL, headers=shetty_headers, json=sheet_inputs)

# sheet_response = requests.post(SHETTY_URL, json=sheet_inputs)
# print(sheet_response.text)