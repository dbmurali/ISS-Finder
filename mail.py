import requests
import datetime as dt
import smtplib
import time
my_lat=-45.804565
my_lon=119.202873
parameters={
    "lat":22.804565,
    "lng":86.202873,
    "formatted":0
}
formate=False
response_sun_timing=requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_sun_timing.raise_for_status()
data=response_sun_timing.json()
sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])


response_iss=requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()
actual_data=response_iss.json()

iss_lat=float(actual_data["iss_position"]["latitude"])
iss_lon=float(actual_data["iss_position"]["longitude"])

today= dt.datetime.now()
current_time=today.time().hour




connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()

user_id="areadb15@gmail.com"
password="dpjxxhxyogevcicl"


def is_top():
    if my_lat-5<= iss_lat <= my_lat+5 and my_lon-5 <= iss_lon <=my_lon+5:

        return  True

def is_dark():
    if current_time>=sunset or current_time<=sunrise:
        return True

while True:
    time.sleep(60)
    if is_top() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user_id,password=password)
            connection.sendmail(from_addr=user_id,to_addrs="dbmurali1507@gmail.com",msg="Subject:LOOK UP FOR ISS\n\n ISS ia above you in the sky" )
