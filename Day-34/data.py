import requests
#  update the ui inorder to get selective questions     
parms = {
    "amount":10,
    "type": "boolean",
    "category":18,
}

respons = requests.get(url="https://opentdb.com/api.php",params=parms)
respons.raise_for_status()
data = respons.json()
question_data = data['results']
