#Password Generator Project
import random
import string_utils
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for char in range(1,nr_letters +1):
#     password += random.choice(letters)

password = [random.choice(letters) for letters in nr_letters]


for smy in range(1, nr_symbols + 1):
     password += random.choice(numbers)

for num in range(1, nr_numbers + 1):
     password += random.choice(symbols)
print(f"Your Password '{password}' on Easy Level!")




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1,nr_letters +1):
    password_list.append(random.choice(letters))

for smy in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)


password = ""
for char in password_list:
    password += char

print(f"Your Password '{password}' after suffling")