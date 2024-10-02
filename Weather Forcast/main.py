import requests
import smtplib

MY_API_KEY = "7b61d7dcf5fe3de9d7e92ace72827f8e"
MY_LAT = 16.905162
MY_LONG = 74.385779

MY_EMAIL = "gaikwadpratik8105@gmail.com"
PASSWORD = "frpuekyijsfjwxot"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": MY_API_KEY,
    "cnt": 4
}

response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=parameters)

is_raining = False

weather_data = response.json()

for forcast in weather_data["list"]:
    if forcast["weather"][0]["id"] < 700:
        is_raining = True


if is_raining:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,
                         password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject:Weather Forcast\n\n"
                                "It's Raining Today Bring An Umbrella With You")
