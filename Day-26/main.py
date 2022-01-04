import pandas
data = pandas.read_csv("Day-26\\nato_phonetic_alphabet.csv")

def gen_phonetic():
    phonetic_dict = {row.letter:row.code  for (index, row) in data.iterrows()}
    word = input("Enter your word :").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:    
        print("Sorry the input is not valid please enter alphabetes") 
        gen_phonetic()
    else:
        print(output_list)


gen_phonetic()