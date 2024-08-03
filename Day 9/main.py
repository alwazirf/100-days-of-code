# Dictionary
programming_dictionary = {
    "Bug" : "An error in program ...",
    "Function" : "A piece of code...",
    "Loop" : "the action of doing something over and over again"
    }

# retrieve items from dictionary
# print(programming_dictionary["Bug"])

programming_dictionary["Alwa"] = "Alwazir Fitrah"

#adding new itemas to dictionary.
programming_dictionary["Loop"] = "Looping"
# print(programming_dictionary)

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


#Nesting a list a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#Neting a dictionary in a dictionary
travel_log2 = {
    "France": {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12,   
    },
    "Germany": {
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

#Neting a dictionary in a list
travel_log3 = [
    {
        "country": "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12,
    },
    {
        "country": "Germany",
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 5,
    }
]

data = {
    "country" : "Indo",
    "cities_visited" : ["Jakarta", "Solo", "Semarang"],
    "total_visits" : 5
}

travel_log3.append(data)

print(travel_log["France"][1])
print(travel_log2["France"]["cities_visited"][1])
print(travel_log3[2]["cities_visited"][0])