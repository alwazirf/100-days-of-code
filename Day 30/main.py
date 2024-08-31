# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Alwa version
# while True:
#     try:
#         word = input("Enter a word: ").upper()
#         for char in word:    
#             if char not in data["letter"].values:
#                 raise ValueError('Sorry, only letters in the alphabet please')
#     except ValueError as error_msg:
#         print(error_msg)
#     else:
#         output_list = [phonetic_dict[letter] for letter in word]
#         print(output_list)
#         break
    

# Angela version
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()