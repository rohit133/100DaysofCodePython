import flight_search
from twilio.rest import Client
TWILIO_SID = "AC51395c37ec339ec819bbb2f3b8d251c1"
TWILIO_AUTH_TOKEN = "091ff1688be61ad7170a1a2cd7c96645"
TWILIO_VIRTUAL_NUMBER = '+18646893080'
TWILIO_VERIFIED_NUMBER = '+918250948396'

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client =Client(TWILIO_SID,TWILIO_AUTH_TOKEN)
    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)