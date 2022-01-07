import smtplib
import datetime as dt 
import random


def monday_mail():
    # quotes 
    with open("Day-32\quotes.txt", "r") as quotes:
        quote = quotes.readlines()
        quote_of_the_day = random.choice(quote) 
        
    # email 
    my_email = "0day2001testing@gmail.com"
    my_password = "0day@2001"
    with smtplib.SMTP("smtp.gmail.com", 587) as new_connection:
        new_connection.starttls()
        new_connection.login(user=my_email, password=my_password)
        new_connection.sendmail(from_addr=my_email,
        to_addrs="sender@gmail.com",
        msg=f"Subject: Moday Quote \n\n {quote_of_the_day}")






now = dt.datetime.now()
week_day = now.weekday()
if week_day == 4:
    monday_mail()
