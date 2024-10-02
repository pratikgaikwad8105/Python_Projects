import requests
import datetime
import smtplib

MY_MAIL = "gaikwadpratik8105@gmail.com"
PASSWORD = "frpuekyijsfjwxot"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

MY_API_KEY_STOCKS = "PY3IGVHM5IMCLPYC"
MY_API_KEY_NEWS = "3e1e8b37dc554c688b1f447bd50e3290"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": MY_API_KEY_STOCKS
}


now = datetime.datetime.now()

# STOCKS Rate
stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday_close = float(stock_data["Time Series (Daily)"][str(now.date()-datetime.timedelta(days=1))]["4. close"])
db_yesterday_close = float(stock_data["Time Series (Daily)"][str(now.date()-datetime.timedelta(days=2))]["4. close"])


greater_value: float

if yesterday_close > db_yesterday_close:
    greater_value = yesterday_close
else:
    greater_value = db_yesterday_close


news_parameters = {
    "q": COMPANY_NAME,
    "apikey": MY_API_KEY_NEWS,
    "language": "en"
}
news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

print(news_data)


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=MY_MAIL,
                     password=PASSWORD)
    if db_yesterday_close > yesterday_close:
        message = ""
        for news in range(3):
            news_title = news_data["articles"][news]["title"]
            news_description = news_data["articles"][news]["description"]

            message = message + (f"Subject:{COMPANY_NAME} :"
                                 f"🔻{(db_yesterday_close - yesterday_close) * 100/greater_value}%\n\n"
                                 f"Title :\n{news_title}\n\nDescription :\n{news_description}\n\n\n\n")

        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=MY_MAIL,
                            msg=message.encode("utf-8"))
    else:
        message = ""
        for news in range(3):
            news_title = news_data["articles"][news]["title"]
            news_description = news_data["articles"][news]["description"]

            message = message + (f"Subject:{COMPANY_NAME} :"
                                 f"▲{(db_yesterday_close - yesterday_close) * 100 / greater_value}%\n\n"
                                 f"Title :\n{news_title}\n\nDescription :\n{news_description}\n\n\n\n")

        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=MY_MAIL,
                            msg=message.encode("utf-8"))


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
  coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
"""
