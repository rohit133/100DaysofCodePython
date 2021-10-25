rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
computer_input = random.randint(0,2)
user_input = int(input("Type '0' for Rock,'1' for Paper and '2' for Scissors: "))
print(user_input)
if(user_input == 0):
    print(rock)
elif(user_input == 1):
    print(paper)
elif(user_input == 2):
    print(scissors)
else:
    print("Please Choose a valid Input!!")


print(computer_input)
if(computer_input == 0):
    print(rock)
elif(computer_input == 1):
    print(paper)
elif(computer_input == 2):
    print(scissors)
else:
    print("Something Went Wrong!")

if(user_input == computer_input):
    print("Draw Retry!\n")
elif(user_input == 0 and computer_input == 2):
    print("You win!")
elif(user_input == 1 and computer_input == 0):
    print("You win")
elif(user_input == 2 and computer_input == 1):
    print("You Win!")
else:
    print("You Lose!!")
