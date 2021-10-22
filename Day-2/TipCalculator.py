print("Welcome to the tip calculator!")
bill = float(input("What was the total Bill? $ "))
# Tip Percentage %
tip = int(input("What percentage tip would you like to give? 10%, 12% or 15%? "))
# No of people
no_of_people = int(input("How many people to split the bill? "))

# calculating the Percen
total_bill = tip / 100 * bill + bill
pay =total_bill / no_of_people

print("Each Person Need's To Pay ",pay,"$")