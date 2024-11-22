# feet_inches = input("Enter feet and inches: ")
#
# def convert(feet_inches):
#     parts = feet_inches.split(' ')
#     feet = float(parts[0])
#     inches = float(parts[1])
#
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters
#
# result = convert(feet_inches)
# print(convert(feet_inches))
#
# if result < 1:
#     print('KId is too else')
# else:
#     print('Kid can use the ride')

# Decoupling
from Bonus.ParseFIB import parse
from Bonus.ConvertFIB import convert

feet_inches = input("Enter feet and inches: ")

f, i= parse(feet_inches)
print(f, i)
result = convert(f, i)
print(result)
if result < 1:
    print('Kid is too small')
else:
    print('Kid can use the ride')