import pandas
data = pandas.read_csv("Day-26\\nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
# Keyword Method with iterrows()
phonetic_dict = {row.letter:row.code  for (index, row) in data.iterrows()}
# print(code)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter your word :").upper()
output_list = [phonetic_dict[letter] for letter in word]

print(output_list)
