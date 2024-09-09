import requests
import re
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = "dummy"
NEWS_KEY = "dummy"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY
}

stock_req = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_req.raise_for_status()
data = stock_req.json()["Time Series (Daily)"]
print(data)
yesterday_closing_price = [value for key, value in data.items()][1]["4. close"]
the_day_closing_price = [value for key, value in data.items()][0]["4. close"]
percentage_close_price = float(yesterday_closing_price) * 0.05
diff = abs(float(yesterday_closing_price) - float(the_day_closing_price))
diff_percent = (diff/float(yesterday_closing_price)) * 100

if diff_percent > 5:
    news_params = {
        "q": COMPANY_NAME,
        "apikey": NEWS_KEY
    }
    response_news = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response_news.json()["articles"]
    three_articles = articles[:3]
