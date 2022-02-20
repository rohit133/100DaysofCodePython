import smtplib 
from twilio.rest import Client
TWILIO_SID = "AC51395c37ec339ec819bbb2f3b8d251c1"
TWILIO_AUTH_TOKEN = "091ff1688be61ad7170a1a2cd7c96645"
TWILIO_VIRTUAL_NUMBER = '+18646893080'
TWILIO_VERIFIED_NUMBER = '+918250948396'
MY_EMAIL = "0day2001testing@gmail.com"
MY_PASSWORD = "0day@2001"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )


