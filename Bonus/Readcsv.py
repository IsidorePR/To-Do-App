# #Read the csv data
# import csv
#
# with open('weather.csv', 'r') as file:
#     data = list(csv.reader(file))
#
# print(data)

#Read individual csv data
import csv

with open('weather.csv', 'r') as file:
    data = list(csv.reader(file))

city = input('Enter country: ').strip().lower()

for row in data:
    if row[0] == city:
        print(row[1])

