print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.\n")
name = input("Choose a Cool Name for yourself:")
print(f"Hello {name} down below you will get your task make wise decison and find the Treasure and win or lose and GAME OVER\n")
step1 = input("You're at a cross road. Where do you want to go Type 'left' or 'right'\n").lower()
if(step1 == 'left'):
    step2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'Swim' to swim across.\n").lower()
    if(step2 == "wait"):
        step3 = input("You arrive at the island unharmed. There is a house with 3 door. one red one yellow and one blue. which colour do you choose?\n").lower()
        if(step3 == "red"):
            print(f"It is room on fire {name} you are burned Sorry Game Over!!")
        elif(step3 == "yellow"):
            print(f"Wow {name} You got the Treasure!! You Won !!")
        elif(step3 == "blue"):
            print(f"You enter a Wrong room {name} Game Over!!")
        else:
            print("Please check the Input Enter any 3 listed Colour!!\n")
    else:
        print("You got eatten up by Shark GAME OVER!!")
else:
    print("You were thrown in the SPACE TIME YOU LOOSE!!")    

