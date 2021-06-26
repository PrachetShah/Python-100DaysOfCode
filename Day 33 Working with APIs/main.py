import requests
from datetime import datetime
import smtplib
import time

# Mumbai Latitude and Longitude
MY_LAT = 19.101803
MY_LONG = 72.890353
EMAIL = "testpythondays@gmail.com"
PASS = "Python123"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True

def is_night():
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
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        # For gmail it is smtp.gmail.com it is different for diff servers
        # smtplib.SMTP("smtp.gmail.com"), we use port if only host does not work
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:

            # This line makes the connection secure by encrypting the message
            connection.starttls()
            connection.login(user=EMAIL, password=PASS)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs="testpython_days@yahoo.com",
                                msg="Subject:Look Up\n\nThe ISS is above you in the sky")
            # U can use "with" keyword here as well to close the file once used




