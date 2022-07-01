import requests
from datetime import datetime
import smtplib
import time

starttime = time.time()

MY_LAT = 52.160114
MY_LONG = 4.497010

MY_EMAIL = "Enter your dummy email here"
MY_PASSWORD = "Enter your dummy password here"


def main():

    def is_iss_overhead():
        # ISS API
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        # iss_position = (iss_latitude, iss_longitude)
        # home_position = (MY_LAT, MY_LONG)

        # Position within +5 or -5 degree of the ISS position.

        if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True

    def is_dark():
        # Sunset and Sunrise API
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        time_now = datetime.utcnow()

        if time_now.hour >= sunset or time_now.hour <= sunrise:
            return True
        else:
            return False

    def iss_overhead_and_dark():
        if is_iss_overhead() and is_dark():
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="Enter recipient address here",
                    msg=f"Subject:Look up the sky!\n\n The ISS is above you in the sky!")
        else:
            print("The ISS is not nearby or it's not dark yet")

    iss_overhead_and_dark()


while True:
    main()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
