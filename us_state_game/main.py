import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

fur = {}


fur["Gray"] = [gray_squirrels_count]
fur["Cinnamon"] = [red_squirrels_count]
fur["Black"] = [black_squirrels_count]

fur_color_count = pandas.DataFrame(fur)

print(fur_color_count)

