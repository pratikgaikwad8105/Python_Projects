import requests
import datetime

APP_ID = "ff9ea484"
API_KEY = "dda467a2db8502cf48d728d2e80fa279"

USERNAME = "gaikwadpratik8105"
PASSWORD = "pratik@8105"

GENDER = "male"
WEIGHT_KG = 56
HEIGHT_CM = 156
AGE = 21


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# _____________________*******________

sheet_endpoint = "https://api.sheety.co/ba44d205fe9d9838731a7ca45ef9a2cd/myExercise/sheet2"

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet2": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(USERNAME, PASSWORD))
