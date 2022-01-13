import requests
from datetime import datetime

APP_ID = "YOUR APP_ID"
API_KEY = "API_KEY"
UID= "ugrgwe7whgfuyhggiu"
AUTH =  "Your Auth"


GENDER = "male"
WEIGHT_KG = 68
HEIGHT_CM = 177.5
AGE = 20
date = datetime.now()
today_date = date.strftime("%d/%m/%Y")
today_time = date.strftime("%X")

# FOOD="https://trackapi.nutritionix.com/v2/natural/nutrients"

EXERCISE="https://trackapi.nutritionix.com/v2/natural/exercise"
Google_sheet = "https://api.sheety.co/aaf08ad8b427ddd2ff059a068f2952f7/myWorkouts/workouts"

# FOOD_INPUT= input("What did you had?")
EXERCISE_INPUT= input("Your Workout?")
header = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id":UID,
}

# food_parameter = {
#     "query":FOOD_INPUT,
#     }
    
# food_response = requests.post(url=FOOD,json=food_parameter,headers= header)
# food_item = food_response.json()
# food_details = food_item["foods"][0]
# food_details["nf_calories"]

exercise_parameter = {
    "query":EXERCISE_INPUT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
    }

exercise_response = requests.post(url=EXERCISE, json=exercise_parameter, headers=header)
data = exercise_response.json()

bearer_headers = {
    "Authorization":AUTH,
}


for exercise in data["exercises"]:
    workout_input= {
        "workout": {
            "date" : today_date,
            "time" : today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

work_response = requests.post(url=Google_sheet,json=workout_input,headers=bearer_headers)
print(work_response.text)

