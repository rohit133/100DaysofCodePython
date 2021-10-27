#Step 5

import random
from hangman_art import stages,logo
from hangman_words import word_list
#Done
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
# Done
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Done
    if guess in display:
        print(f"You have already guessed {guess} please move forward to another one")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        # Done
        lives -= 1
        print(f"You chosen a wrong letter {guess}, you lose 1 live no of live remaining {lives} ")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Done
    print(stages[lives])