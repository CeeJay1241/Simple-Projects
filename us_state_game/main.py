import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# data_dict = data.to_dict()
# #print(data_dict)

# temp_list = data["temp"].to_list()
# #print(temp_list)

# average = sum(temp_list) / len(temp_list)

# maximum = data["temp"].max()
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp.values[0]

# print(monday_temp)

data_color = data["Primary Fur Color"].to_list()

fur = {}

g = 0
c = 0
b = 0
for i in data_color:
    if i == "Gray":
        g += 1
    elif i == "Cinnamon":
        c += 1
    elif i == "Black":
        b += 1

fur["Gray"] = [g]
fur["Cinnamon"] = [c]
fur["Black"] = [b]

#print(fur)
fur_color_count = pandas.DataFrame(fur)

print(fur_color_count)