# To know all txt file saved in python
# import glob
#
# myfiles = glob.glob('File/*.txt')
# print(myfiles)

# To access the content in the txt files

import glob

myfiles = glob.glob('File/*.txt')

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())