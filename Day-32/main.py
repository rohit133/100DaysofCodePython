##################### Extra Hard Starting Project ######################
from random import randint
import pandas as pd
import smtplib 
import datetime as dt
MY_EMAIL = "0day2001testing@gmail.com"
MY_PASSWORD = "0day@2001"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

# 2. Check if today matches a birthday in the birthdays.csv
data = pd.read_csv("Day-32//birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"Day-32\\letter_templates\\letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connections:
        connections.starttls()
        connections.login(user=MY_EMAIL, password=MY_PASSWORD)
        connections.sendmail(from_addr= MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday! \n\n {content}"
            )




 