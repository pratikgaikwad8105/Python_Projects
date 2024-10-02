import smtplib
import datetime as dt
import random

# Today's Day
now = dt.datetime.now()
day_of_week = now.weekday()

# Quote read
with open("quotes.txt", "r") as file:
    data = file.readlines()
quote = random.choice(data)

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Email Send
EMAIL = "gaikwadpratik8105@gmail.com"
PASSWORD = "blqvfmtrmhugveno"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=EMAIL,
                     password=PASSWORD)
    connection.sendmail(from_addr=EMAIL,
                        to_addrs=EMAIL,
                        msg=f"Subject:{week[day_of_week]}'s Motivation\n\n{quote}")