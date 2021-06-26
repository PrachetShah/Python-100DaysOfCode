import requests
from datetime import datetime
# Need to create parameters for this API Which should match its parameters
MY_LAT = 19.075983
MY_LNG = 72.877655

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

resonse = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
resonse.raise_for_status()
data = resonse.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
# print(time_now)
