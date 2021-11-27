#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = '[name]'

with open("Day-24\\Input\\Names\\invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Day-24\Input\Letters\starting_letter.txt") as layout:
    format = layout.read()
    for name in names:
        stripped_name = name.strip("\n")
        letter = format.replace(PLACEHOLDER,stripped_name)
        with open(f"Day-24\\Output\\letter_for_{stripped_name}", mode="w") as ouput:
            ouput.write(letter)
