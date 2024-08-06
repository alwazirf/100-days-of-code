# cecar cipel
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

char_plain = []

def encrypt(plain_text, shiff):
    new_str = ""
    for i in range(0, len(plain_text)):
        char_plain.append(alphabet.index(plain_text[i])+shiff)
    for data in char_plain:
        new_str += alphabet[data]
    print(f"The encoded text is {new_str}")
    
    # angela
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        cipher_text += alphabet[position+shiff]
    print(f"The encoded text is {cipher_text}")
    
def decrypt(plain_text, shiff):
    new_str = ""
    for i in range(0, len(plain_text)):
        char_plain.append(alphabet.index(plain_text[i])-shiff)
    
    for data in char_plain:
        new_str += alphabet[data]
    print(f"The decoded text is {new_str}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
if direction == "encode":
    text = input("Type your message:\n").lower()
    shiff = int(input("Type the shiff number:\n"))
    encrypt(text, shiff)
elif direction == "decode":
    text = input("Type your message: \n").lower()
    shiff = int(input("Type the shiff number: \n"))
    decrypt(text, shiff)
else:
    print("the keyword is missing")

import art

print(art.logo)

#combine the encrypt() and decrypt() to caesar().
#Alwa version
# def caesar(direction, plain_text, shiff):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         if direction == "encode":
#             cipher_text += alphabet[position+shiff]
#         elif direction == "decode":
#             cipher_text += alphabet[position-shiff]
#         else:
#             print("Suka suka lu")
#     print(f"The {direction} text is {cipher_text}")
    
#angela version
def caesar(direction, plain_text, shiff):
    cipher_text = ""
    if direction == "decode":
        shiff *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            cipher_text += alphabet[position+shiff]
        else:
            cipher_text += char
    print(f"The {direction} text is {cipher_text}")
    
is_continue = True
while is_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shiff = int(input("Type the shiff number: \n"))
    shiff = shiff % 26

    caesar(direction=direction, plain_text=text, shiff=shiff)
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no' if not \n")
    if result == "no":
        is_continue = False
        print("Goodbye")