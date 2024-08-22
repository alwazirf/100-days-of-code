import pandas as pd

# data = pd.read_csv("./weather_data.csv")

# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()

# avg = sum(temp_list) / len(temp_list) 
# print(f"average data is {avg}")

# print(data["temp"].max())

# get data in columns
# print(data.condition)

# get data in row
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # celc = monday.at[0, "temp"]
# celc = monday.temp[0]
# fahr = (celc* 9/5) + 32
# print(f"Celcius = {celc} | Fahrenheit = {fahr}")

# # create data frame from scratch
# data_dict = {
#     "students": ["amy", "james", "angela"],
#     "scores": [76,56,65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("./new_data.csv")

# Fur Color, Count
data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240822.csv")
color = data["Primary Fur Color"]
grey_count = len(data[color == "Gray"])
red_count = len(data[color == "Cinnamon"])
black_count = len(data[color == "Black"])
data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("./squirrel_count.csv")