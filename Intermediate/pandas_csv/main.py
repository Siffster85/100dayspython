import pandas

data = pandas.read_csv("./Intermediate/pandas_csv/weather_data.csv")

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

print(round(data["temp"].mean()))

print(data.temp.max())

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

print((monday.temp * (9/5)) + 32)

database_dict = {
  "students": ["Amy", "James", "Angela"],
  "scores": [76, 56, 65]
}

database = pandas.DataFrame(database_dict)
database.to_csv("./Intermediate/pandas_csv/student_data.csv")

squirrels = pandas.read_csv("./Intermediate/pandas_csv/004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

grey_squirrel_count = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrels[squirrels["Primary Fur Color"] == "Black"])


squirrel_dict = {
  "Fur Colour": ["Grey", "Red", "Black"],
  "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

count_dataframe = pandas.DataFrame(squirrel_dict)
count_dataframe.to_csv("./Intermediate/pandas_csv/squirrel_count.csv")

