import requests
from twilio.rest import Client
MY_LAT = 26.724397 # Your latitude
MY_LONG = 88.436662 # Your longitude

API_KEY = "5df1e3afa19894752fe6a66c33a5e0fb"
account_sid= "AC51395c37ec339ec819bbb2f3b8d251c1"
auth_token = "200fcd92e50a9a1f27995d50795f9ae6" 



parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "exclude":"current,minutely,daily",
    "appid":API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?",params=parameters)
response.raise_for_status()
weather_data = response.json()

data = weather_data["hourly"][:12]
for i in data:
    weather_id = i["weather"][0]["id"]
    if weather_id <= 700:
        is_raining = True
    else:
        is_raining = False

if is_raining:
    client = Client(account_sid, auth_token) 
    message = client.messages \
                .create(
                     body="It's going to rain today.Remember to bring an Umberlla☔",
                     from_='+18646893080', 
                     to='+918250948396'
                )
    print(message.status)
