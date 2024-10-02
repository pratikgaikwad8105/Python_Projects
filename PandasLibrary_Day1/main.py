# import csv
# temperature = []
# with open("PandasLibrary_Day1/weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1] == "temp":
#             continue

#         temperature.append(int(row[1]))

# print(temperature)

import pandas
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].tolist()

# avg = sum(temp_list) / len(temp_list)
# print(f"Average temp is {data["temp"].mean()}")

# print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
#
# print(monday.temp * 9/5 + 32)

# data_dict = {
#     "Cricketers": ["Virat", "ABD", "Rohit", "M.S.Dhoni", "DK"],
#     "Scores": [123, 156, 263, 189, 102]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("Cricket.csv")

data = pandas.read_csv("Squirrel_data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Colours": ["Gray", "Black", "Cinnamon"],
    "count": [gray_count, black_count, cinnamon_count]
}

color_data = pandas.DataFrame(data_dict)
print(color_data)

color_data.to_csv("Squirrel Colors data.csv")
