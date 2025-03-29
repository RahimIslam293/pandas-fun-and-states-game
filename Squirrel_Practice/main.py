import csv
import pandas
import statistics
# with open("weather_data.csv", 'r') as file:
#     list_of_weather = csv.reader(file, delimiter=",")
#     l = []
#     list_of_weather.__next__() #skip header
#     for i in list_of_weather:
#         print(i)
#         l.append(int(i[1]))
# print(l)

k = pandas.read_csv("weather_data.csv")
# k_dict = k.to_dict()
# j_series = k["temp"].to_list()
# k_series = k["temp"]
# print(k_dict)
# print(k["temp"][1])
# print(j_series)
# average = statistics.mean(j_series)
# average_two = sum(j_series)/len(j_series)
# print(average)
# print(k_series.mean())
# print(k_series.max())
#print(k)
# print(k[k.day == "Monday"].temp[0]*1.8+32)

#print(k[k.condition == "Sunny"])

full_squirrel_import = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(full_squirrel_import[full_squirrel_import["Primary Fur Color"] == "Gray"])
red_count = len(full_squirrel_import[full_squirrel_import["Primary Fur Color"] == "Cinnamon"])
black_count = len(full_squirrel_import[full_squirrel_import["Primary Fur Color"] == "Black"])

squirrel_colors_dict = {
    "fur color": ["gray","cinnamon","black"],
    "count":[gray_count,red_count,black_count]
}
new_colors_df = pandas.DataFrame(squirrel_colors_dict)
#print(new_colors_df)
new_colors_df.to_csv("squirrel_colors.csv")