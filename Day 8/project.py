# cecar cipel
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(plain_text, shiff):
#     newStr = ""
    # for i in range(0, len(plain_text)):
    #     charPlain.append(alphabet.index(plain_text[i])+shiff)
    # for data in charPlain:
    #     newStr += alphabet[data]
    # print(f"The encoded text is {newStr}")
    
    #angela
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         cipher_text += alphabet[position+shiff]
#     print(f"The encoded text is {cipher_text}")
    
# def decrypt(plain_text, shiff):
#     new_Str = ""
#     for i in range(0, len(plain_text)):
#         charPlain.append(alphabet.index(plain_text[i])-shiff)
    
#     for data in charPlain:
#         new_Str += alphabet[data]
#     print(f"The decoded text is {new_Str}")

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
# if direction == "encode":
#     text = input("Type your message: \n").lower()
#     shiff = int(input("Type the shiff number: \n"))
#     encrypt(text, shiff)
# elif direction == "decode":
#     text = input("Type your message: \n").lower()
#     shiff = int(input("Type the shiff number: \n"))
#     decrypt(text, shiff)
# else:
#     print("the keyword is missing")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shiff = int(input("Type the shiff number: \n"))



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
    for letter in plain_text:
        position = alphabet.index(letter)
        cipher_text += alphabet[position+shiff]
    print(f"The {direction} text is {cipher_text}")

caesar(direction=direction, plain_text=text, shiff=shiff)