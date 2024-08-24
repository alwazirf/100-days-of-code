number = [1,2,3]
new_number = []
for n in number:
    add_1 = n + 1
    new_number.append(add_1)
print(new_number)

# [newitem for item in items] => list comprehension
new_list2 = [n+1 for n in number]
print(new_list2)

name = "Angela"
each_char_of_name = [letter for letter in name]
print(each_char_of_name)

new_list3 = [i*2 for i in range(1,5)]
print(new_list3)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

new_names = [name for name in names if len(name) < 5]
new_names2 = [name.upper() for name in names if len(name) > 5]
print(new_names2)