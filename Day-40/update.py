import requests
Google_sheet = "https://api.sheety.co/aaf08ad8b427ddd2ff059a068f2952f7/flightDeals/users"
def sheet_update():
  user_input={
    "user": 
      {
        "fname" : fname,
        "lname" : lname,
        "email": email,
      }
    }
  update_respons = requests.post(url=Google_sheet,json=user_input)
  print(update_respons.status_code)

def enter_email(email):
  re_email = input("Re Enter your email id: ")
  if email == re_email:
    sheet_update()
    print("Welcome to the club\nSuccess your email has been added!")
    return True
  else:
    print("Please check your email !!")
    return False

print("Welcome to the flight club\nWe help you find the best fligh deals!\nEnter your deatils below to register")
fname =input("Enter your First Name: ")
lname =input("Enter your Last Name: ")
email =input("Enter your email id: ")
is_email_correct = enter_email(email)
if(is_email_correct ==False):
  enter_email(email)

