import requests
from twilio.rest import Client
account_sid= "AC51395c37ec339ec819bbb2f3b8d251c1"
auth_token= ["Use your AUTH KEY"]


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "P04SLGUD4UM3KLL1"
NEWS_API_KEY = "67a6c3b0bc0744d393391b310c033790"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,
}

news_parameters = {
    "apiKey":NEWS_API_KEY,
    "qInTitle":COMPANY_NAME
}



r = requests.get(STOCK_ENDPOINT,stock_parameters)
data = r.json()
daily_updates = data["Time Series (Daily)"]
data_list = [ value for (key, value) in daily_updates.items()]

#TODO 1. - Get yesterday's closing stock price.
yesterday_closing_price =float(data_list[0]["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price
daybefore_yesterda_closing_price = float(data_list[1]["4. close"])

#TODO 3. - Find the positive difference between 1 and 2
price_difference = yesterday_closing_price - daybefore_yesterda_closing_price
price_difference = price_difference
up_down = None
if price_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = round((price_difference / yesterday_closing_price) * 100)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percentage) >= 2:
    news_respons = requests.get(NEWS_ENDPOINT,news_parameters)
    articles = news_respons.json()["articles"]

    first_3 = articles[:3]
    formatted_articles = [f"{STOCK_NAME} : {up_down} {diff_percentage}%\nHeadline: {news_content['title']}. \nBrief: {news_content['description']}" for news_content in first_3]
    print(formatted_articles)
   
client = Client(account_sid, auth_token) 
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_='+18646893080', 
        to='+918250948396'
                )
    print(message.status)