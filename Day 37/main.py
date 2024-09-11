import requests
from datetime import datetime
import random

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "alwazirf"
TOKEN = "hijkhijkhijk4hijk5hijk6hijk7"
GRAPH_ID = "graph1"
GRAPH_NAME = "Cyling Graph"


user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThisIsThanksCode"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers_token = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, headers=headers_token, json=graph_config)
# print(response.text)
today = datetime(year=2024, month=9, day=9)

data_post = {
    "date": today.strftime("%Y%m%d"),
    "quantity": f"{random.randint(5,30)}"
}

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# response = requests.post(url=pixel_creation_endpoint, headers=headers_token, json=data_post)
# print(response.text)

update_color_graph = {
    "name": GRAPH_NAME,
    "color": "ajisai"
}

# response_put = requests.put(url=pixel_creation_endpoint, headers=headers_token, json=update_color_graph)
# print(response_put.text)

# print(datetime_now)

response_del = requests.delete(url=f"{pixel_creation_endpoint}/{data_post['date']}", headers=headers_token)
print(response_del.text)