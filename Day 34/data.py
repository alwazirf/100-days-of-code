question_data = []

import requests

req = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
req.raise_for_status()
question_data = req.json()["results"]