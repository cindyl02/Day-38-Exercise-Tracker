import requests
import datetime as dt
import os

APP_ID = os.environ["APP_ID"]

API_KEY = os.environ["API_KEY"]

SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

TOKEN = os.environ["TOKEN"]

GENDER = "Female"
WEIGHT_KG = "55"
HEIGHT_CM = "168"
AGE = "30"

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=API_ENDPOINT, json=params, headers=headers)
exercises_list = response.json()["exercises"]
print(exercises_list)

today = dt.datetime.now()
time = today.time().strftime("%H:%M:%S")
today = today.strftime("%d/%m/%y")

bearer_headers = {
    "Authorization": TOKEN
}
for exercise_data in exercises_list:
    exercise = exercise_data["name"].title()
    duration = exercise_data["duration_min"]
    calories = exercise_data["nf_calories"]
    data = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise,
            "duration": str(duration),
            "calories": str(calories),
        }
    }
    response = requests.post(url=SHEET_ENDPOINT, json=data, headers=bearer_headers)
    print(response.json())
