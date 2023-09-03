import requests
from datetime import datetime
import smtplib
import time
import json

class ISSNotifier:
    def __init__(self, email, password, latitude, longitude, smtp_address):
        self.email = email
        self.password = password
        self.latitude = latitude
        self.longitude = longitude
        self.smtp_address = smtp_address

    def is_iss_overhead(self):
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = json.loads(response.text)

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        if abs(iss_latitude - self.latitude) <= 5 and abs(iss_longitude - self.longitude) <= 5:
            return True
        return False

    def is_night(self):
        params = {"lat": self.latitude, "lng": self.longitude, "formatted": 0}
        response = requests.get("https://api.sunrise-sunset.org/json", params=params)
        response.raise_for_status()
        data = json.loads(response.text)

        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        current_hour = datetime.now().hour

        if current_hour >= sunset or current_hour <= sunrise:
            return True
        return False

    def send_email(self):
        with smtplib.SMTP(self.smtp_address) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )

if __name__ == "__main__":
    notifier = ISSNotifier(
        email="___YOUR_EMAIL_HERE____",
        password="___YOUR_PASSWORD_HERE___",
        latitude=51.507351,
        longitude=-0.127758,
        smtp_address="__YOUR_SMTP_ADDRESS_HERE___"
    )

    while True:
        time.sleep(60)
        if notifier.is_iss_overhead() and notifier.is_night():
            notifier.send_email()
