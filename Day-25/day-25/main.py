# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    # for i in range(1, len(data):
    for row in data:
        if row[1] != 'temp':
            temperatures.append(row[1])
    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temperature_list = data['temp'].to_list()
print(temperature_list)
print(sum(temperature_list)/len(temperature_list))

print(data["temp"].mean())
print(data["temp"].max())

# Get data in columns
print(data.temp)

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])
monday = data[data.day == "Monday"]
print(monday.condition)

# create dataframe from scratch

data_dict = {
    "students":["Amy", "James", "Anna"],
    "scores": [76, 56, 55]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

dataframe = pandas.DataFrame(squirrel_dict)
dataframe.to_csv("squirrel_count.csv")



