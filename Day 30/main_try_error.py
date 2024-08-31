# FileNotFound
# with open("./a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key", "Value"}
# value = a_dictionary["keeey"]

# IndexError
# fruit_list = ["Apple", "Banana", "Melon"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text+5)

# try -> something that might cause an exeption
# execpt: -> do this if there is an error
# else: -> do this if no error
# finally -> do this on the end step, if any error or not

# try:
#     file = open("./a_file.txt")
#     a_dictionary = {"key": "Value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_msg:
#     print(f"Key: {error_msg} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that i made up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight/height**2
print(bmi)