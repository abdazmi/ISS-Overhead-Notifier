import requests
from datetime import datetime
import smtplib
import time

# to find your Latitude and Longitude  use this link below
# https://www.latlong.net/

MY_LAT = "PUT YOUR LAT HERE"
MY_LONG = "PUT YOUR LONG HERE"

my_email = "YOUR EMAIl"
password = "YOUR PASSWORD"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
x=1
while True:
    if iss_latitude in range(int(MY_LAT)-5,int(MY_LAT)+5 ) and \
            iss_longitude in range(int(MY_LONG)-5,int(MY_LONG)+5 ) and \
            time_now >= sunset:

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="abdullah.mustafa11221@gmail.com",
                                msg="Subject: International space station is near Mousl home\n\n Go watch it babe")
    else:
        print(f"attemt number: {x} didn't reached yet")
        time.sleep(44)
        x += 1

