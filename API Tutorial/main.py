import requests
import datetime
import smtplib

MY_LAT = 16.906602
MY_LNG = 74.382626

MY_MAIL = "gaikwadpratik8105@gmail.com"
PASSWORD = "frpuekyijsfjwxot"


def is_iss_visible(sun_rise, sun_set, _now):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if ((sun_rise > _now > sun_set) and (MY_LAT + 5 > iss_latitude > MY_LAT - 5) and
            (MY_LAT + 5 > iss_longitude > MY_LAT + 5)):
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
    "tzid": "Indian/Chagos"
}
sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sunrise_sunset.raise_for_status()
time_data = sunrise_sunset.json()

sunrise = int(time_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(time_data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.datetime.now()
now = time_now.hour

found = False

while not found:
    if is_iss_visible(sunrise, sunset, now):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg="Subject:Look Up!\n\nThe position of the ISS is"
                                                                         " above your head please look up to see the ISS")
            found = True

