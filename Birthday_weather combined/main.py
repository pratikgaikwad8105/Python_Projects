import datetime as dt
import pandas
import random
import os
import smtplib
import requests

# MY EMAIL and PASSWORD
MY_MAIL = "gaikwadpratik8105@gmail.com"
PASSWORD = "frpuekyijsfjwxot"

# Check if today matches a birthday in the birthdays.csv

data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
date = now.day
month = now.month

# Get a Today's Birthday
birthday = data.query(f'day == {date}' and f"month == {month}")
today_birthday = birthday.to_dict(orient="records")


# Pick the random Template
templates_path = os.listdir("letter_templates")
random_template = random.choice(templates_path)
file_path = os.path.join("letter_templates", random_template)

with open(file_path, "r") as file:
    lines = file.read()

for peoples in today_birthday:
    message = lines.replace("[NAME]", peoples["name"])
    # Send the letter
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL,
                         password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=peoples["email"],
                            msg=f"Subject:Happy Birthday!\n\n{message}")


# ____________________________________RAIN_ALERT______________________________#

MY_API_KEY = "7b61d7dcf5fe3de9d7e92ace72827f8e"
MY_LAT = 16.905162
MY_LONG = 74.385779


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
        connection.login(user=MY_MAIL,
                         password=PASSWORD)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=MY_MAIL,
                            msg="Subject:Weather Forcast\n\n"
                                "It's Raining Today Bring An Umbrella With You")


# _____________________________ISS_Alert___________________________________#

def is_iss_visible(sun_rise, sun_set, _now):
    response1 = requests.get("http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    data1 = response1.json()

    iss_latitude = float(data1["iss_position"]["latitude"])
    iss_longitude = float(data1["iss_position"]["longitude"])

    if ((sun_rise > _now > sun_set) and (MY_LAT + 5 > iss_latitude > MY_LAT - 5) and
            (MY_LAT + 5 > iss_longitude > MY_LAT + 5)):
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Indian/Chagos"
}
sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sunrise_sunset.raise_for_status()
time_data = sunrise_sunset.json()

sunrise = int(time_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(time_data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = dt.datetime.now()
_now = time_now.hour

found = False

while not found:
    if is_iss_visible(sunrise, sunset, _now):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg="Subject:Look Up!\n\nThe position of the ISS is"
                                                                         " above your head please look up to see the ISS")
            found = True
