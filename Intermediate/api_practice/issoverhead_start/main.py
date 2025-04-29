import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 53.4808 # Your latitude
MY_LONG = -2.2426 # Your longitude
EMAIL = "" #insert email here
PASSWORD = "" #insert app password here

def iss_above():
  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  data = response.json()

  iss_latitude = float(data["iss_position"]["latitude"])
  iss_longitude = float(data["iss_position"]["longitude"])
  return iss_latitude >= MY_LAT -5 and iss_latitude <= MY_LAT +5 and iss_longitude >= MY_LONG -5 and iss_longitude <= MY_LONG +5
  
def is_dark():
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
  time_now = datetime.now()
  return time_now.hour >= sunset or time_now.hour <= sunrise

while True:
  time.sleep(60)
  print("checking")
  if is_dark() and iss_above():
    with smtplib.SMTP("smtp.server.com") as connection: #correct the SMTP server.
      connection.starttls()
      connection.login(user=EMAIL, password=PASSWORD)
      connection.sendmail(
        from_addr=EMAIL, 
        to_addrs=EMAIL, 
        msg=f"Subject:ISS IS ABOVE!\n\nGo outside and look!"          
      )

