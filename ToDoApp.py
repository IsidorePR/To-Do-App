# #Lesson 1
from bdb import Breakpoint
from fileinput import filename
from tokenize import Number

# print('My to do list')
# user_prompt = 'Enter Task :'
# Task1 = input(user_prompt)
# print(Task1)
#
# #Multiple input Test
# name_prompt = 'Enter Name:'
# city_prompt = 'Enter City:'
# country_prompt = 'Enter Country:'
# Name = input(name_prompt)
# City = input(city_prompt)
# Country = input(country_prompt)
# print(Name,City,Country)

# #Lesson 2

# print('My to do list')
# user_prompt = 'Enter Task'
# Task1 = input(user_prompt)
# Task2 = input(user_prompt)
# Task3 = input(user_prompt)
#
# Tasks = [Task1, Task2, Task3]
# print(Tasks)

# #Lesson 3

# user_prompt = 'Enter Task'
#
# while 2>1:
#     Task = input(user_prompt)
#     print(Task)
#     print("Next")

# #Lesson 3 Better way(Boolean way)

# user_prompt = 'Enter Task'
#
# while True:
#     Task = input(user_prompt)
#     print(Task)
#     print("Next")

# #Lesson 4

# user_prompt = "Enter Task"
# Tasks = []
# while True:
#     Task = input(user_prompt)
#     Tasks.append(Task)
#     print(Tasks)

# # Lesson 5
#
# Password = input("Enter Password")
# while Password != "Pass123":
#     Password = input("Enter Password")
#
# print("Password is Correct")

# # Lesson 6
#
# x = 1
# while x<=6 :
#     print(x)
#     x = x + 1

# # Lesson 7
#
# Tasks =[]
#
# while True:
#     user_action = input("Type add, show or exit:" )
#
#     match user_action:
#         case 'add':
#             Task = input("Enter Tasks:")
#             Tasks.append(Task)
#         case 'show':
#             print(Tasks)
#         case 'exit':
#             break
# print("Bye")

# # Lesson 7.1(Better version Show will be in column form)
# Tasks = []
# while True:
#     user_action = input('Enter add,show or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#     match user_action:
#         case 'add':
#             Task = input('Enter Task: ')
#             Tasks.append(Task)
#         case 'show':
#             for items in Tasks:
#                 items = items.title()
#                 print(items)
#         case 'exit':
#             break
#         case _:
#             print('Invalid input')
# print('Bye!')

# #Example
# country = "USA"
#
# match country:
#     case 'USA' | 'United States':
#         print('Hello')
#     case 'Italy':
#         print('Ciao')
#     case 'Germany':
#         print('Hallo')

# # Example
# employees = ["john smith", "sarah bremen", "dora dawson"]
#
# for i in employees:
#     print(i.title())

# Lesson 7 LIST INDEXING

# # Lesson 7.1(Better version Show will be in column form)
# Tasks = []
# while True:
#     user_action = input('Enter add,show,edit or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#     match user_action:
#         case 'add':
#             Task = input('Enter Task: ')
#             Tasks.append(Task)
#         case 'show':
#             for items in Tasks:
#                 items = items.title()
#                 print(items)
#         case 'edit':
#             number = int(input('Enter the number:'))
#             number = number -1 # sice people wont know that python starts from 0
#             new_task = input('Enter new task')
#             Tasks[number] = new_task
#
#         case 'exit':
#             break
#         case _:
#             print('Invalid input')
#
# print('Bye!')

# #Lesson 8
# filenames = ['1.Raw Data.txt', '2.Report.txt', '3.Present.txt']
#
# for filename in filenames:
#     filename = filename.replace('.','-',1)
#     print(filename)

# # Lesson 9 Numbered Task Enumeration
#
# Tasks = []
# while True:
#     user_action = input('Enter add,show,edit or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#     match user_action:
#         case 'add':
#             Task = input('Enter Task: ')
#             Tasks.append(Task)
#         case 'show':
#             for index, items in enumerate(Tasks):
#                 items = items.title()
#                 row = f"{index}:{items}"
#                 print(row)
#         case 'edit':
#             number = int(input('Enter the number:'))
#             #number = number -1 # since people won't know that python starts from 0
#             new_task = input('Enter new task')
#             Tasks[number] = new_task
#
#         case 'exit':
#             break
#         case _:
#             print('Invalid input')
#
# print('Bye!')


# # Lesson 10 Complete Task
#
# Tasks = []
# while True:
#     user_action = input('Enter add,show,edit,complete or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#     match user_action:
#         case 'add':
#             Task = input('Enter New Task: ')
#             Tasks.append(Task)
#         case 'show':
#             for index, items in enumerate(Tasks):
#                 items = items.title()
#                 row = f"{index + 1}:{items}"
#                 print(row)
#         case 'edit':
#             number = int(input('Enter the Task number to edit:'))
#             number = number -1 # since people won't know that python starts from 0
#             new_task = input('Enter new task')
#             Tasks[number] = new_task
#         case 'complete':
#             number = int(input('Enter the Task number completed:'))
#             Tasks.pop(number - 1)
#         case 'exit':
#             break
#         case _:
#             print('Invalid input')
#
# print('Bye!')

# #Lesson 11 Storing items in TXT file
#
# #Tasks = [] Problem with this is that everytime we exit the code and run it again the existing todo list is deleted so
#           #so we do not use this line
# while True:
#     user_action = input('Enter add, show, edit, complete or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#     match user_action:
#         case 'add':
#             Task = input('Enter New Task: ') + '\n' #\n for leaving 1 line and showing output in txt file
#
#             file_read = open('ToDos.txt', 'r')
#             Tasks =file_read.readlines()
#             file_read.close()
#
#             Tasks.append(Task)
#
#             file = open('ToDos.txt', 'w') #w for write r for read
#             file.writelines(Tasks)
#             file.close()
#         case 'show':
#             file = open('ToDos.txt', 'r')
#             Tasks = file.readlines() #readline all input individual strings, read all input in one line
#             file.close()
#
#             Tasks= [items.strip('\n') for items in Tasks] #removes extra line space after each word in the output
#
#             for index, items in enumerate(Tasks):
#                 items = items.title()
#                 row = f"{index + 1}:{items}"
#                 print(row)
#         case 'edit':
#             number = int(input('Enter the Task number to edit:'))
#             number = number -1 # since people won't know that python starts from 0
#             new_task = input('Enter new task')
#             Tasks[number] = new_task
#         case 'complete':
#             number = int(input('Enter the Task number completed:'))
#             Tasks.pop(number - 1)
#         case 'exit':
#             break
#         case _:
#             print('Invalid input')
#
# print('Bye!')

# # Lesson 12 creating multiple files
# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
# filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
#
# for content, filename in zip(countries, filenames):
#     file = open(filename, 'w')
#     file.write(content)
#     file.close()

# # Lesson 12.1
# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
#
# for item in countries:
#     file = open(f'{item}.txt','w')
#     file.write(item)
#     file.close()

# #List comprehension
# names = ["john smith", "jay santi", "eva kuki"]
# names = [name.title() for name in names]
# print(names)

# #List comprehension length
# usernames = ["john 1990", "alberta1970", "magnola2000"]
# usernames = [len(username) for username in usernames]
# print(usernames)

# #List comprehension numbers
# numbers = [10, 20, 30]
# numbers = [i*2 for i in numbers]
# print(numbers)

# #List comprehension sum numbers
# user_entries = ['10', '19.1', '20']
# user_entries = [float(i) for i in user_entries]
# print(sum(user_entries))


#Lesson 13 Use 'With Context Manager' to optimize code

# #Tasks = [] Problem with this is that everytime we exit the code and run it again the existing todo list is deleted so
#           #so we do not use this line
# while True:
#     user_action = input('Enter add, show, edit, complete or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#     match user_action:
#         case 'add':
#             Task = input('Enter New Task: ') + '\n' #\n for leaving 1 line and showing output in txt file
#
#             with open('ToDos.txt', 'r') as file_read: #replace below code
#                 Tasks = file_read.readlines()#need not close as with will close the file automatically
#             # file_read = open('ToDos.txt', 'r')
#             # Tasks =file_read.readlines()
#             # file_read.close()
#
#             Tasks.append(Task)
#
#             with open('ToDos.txt', 'w') as file:
#                 file.writelines(Tasks)
#             # file = open('ToDos.txt', 'w') #w for write r for read
#             # file.writelines(Tasks)
#             # file.close()
#
#
#         case 'show':
#             with open('ToDos.txt', 'r') as file:
#                 Tasks = file.readlines()
#             # file = open('ToDos.txt', 'r')
#             # Tasks = file.readlines() #readline all input individual strings, read all input in one line
#             # file.close()
#
#             Tasks= [items.strip('\n') for items in Tasks] #removes extra line space after each word in the output
#
#             for index, items in enumerate(Tasks):
#                 items = items.title()
#                 row = f"{index + 1}:{items}"
#                 print(row)
#         case 'edit':
#             number = int(input('Enter the Task number to edit:'))
#             number = number -1 # since people won't know that python starts from 0
#             new_task = input('Enter new task')
#             Tasks[number] = new_task
#         case 'complete':
#             number = int(input('Enter the Task number completed:'))
#             Tasks.pop(number - 1)
#         case 'exit':
#             break
#         case _:
#             print('Invalid input')
#
# print('Bye!')


# #Lesson 14 Edit and Complete
#
# #Tasks = [] Problem with this is that everytime we exit the code and run it again the existing todo list is deleted so
#           #so we do not use this line
# while True:
#     user_action = input('Enter add, show, edit, complete or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#     match user_action:
#         case 'add':
#             Task = input('Enter New Task: ') + '\n' #\n for leaving 1 line and showing output in txt file
#
#             with open('ToDos.txt', 'r') as file_read:
#                 Tasks = file_read.readlines()
#
#             Tasks.append(Task)
#
#             with open('ToDos.txt', 'w') as file:
#                 file.writelines(Tasks)
#
#         case 'show':
#             with open('ToDos.txt', 'r') as file_read:
#                 Tasks = file_read.readlines()
#
#             Tasks= [items.strip('\n') for items in Tasks] #removes extra line space after each word in the output
#
#             for index, items in enumerate(Tasks):
#                 items = items.title()
#                 row = f"{index + 1}:{items}"
#                 print(row)
#
#         case 'edit':
#             number = int(input('Enter the Task number to edit:'))
#             number = number -1 # since people won't know that python starts from 0
#
#             with open('ToDos.txt', 'r') as file_read:
#                 Tasks = file_read.readlines()
#
#             new_task = input('Enter new task') +'\n'
#             Tasks[number] = new_task
#
#             with open('ToDos.txt', 'w') as file:
#                 file.writelines(Tasks)
#
#         case 'complete':
#             number = int(input('Enter the Task number completed:'))
#             with open('ToDos.txt', 'r') as file_read:
#                 Tasks = file_read.readlines()
#
#             Tasks.pop(number - 1)
#
#             with open('ToDos.txt', 'w') as file:
#                 file.writelines(Tasks)
#
#         case 'exit':
#             break
#         case _:
#             print('Invalid input')
#
# print('Bye!')

# #Lesson 15 Example create individual txt file
# languages = ['English', 'German', 'Spanish']
#
# for items in languages:
#     with open(f'{items}.txt', 'w') as file:
#         file.write(items)


# #Lesson 16 Improving ADD, EDIT, COMPLETE feature
#
# while True:
#     user_action = input('Enter add, show, edit, complete or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#
#     if 'add' in user_action:
#         Task = user_action[4:] #add + space = 4
#
#         with open('ToDos.txt', 'r') as file_read:
#             Tasks = file_read.readlines()
#
#         Tasks.append(Task +'\n')
#
#         with open('ToDos.txt', 'w') as file:
#             file.writelines(Tasks)
#     # if can we used all places but problem is the code will run all the if conditions elif fixes that and speedup prog
#     elif 'show' in user_action:
#         with open('ToDos.txt', 'r') as file_read:
#             Tasks = file_read.readlines()
#
#         Tasks= [items.strip('\n') for items in Tasks] #removes extra line space after each word in the output
#
#         for index, items in enumerate(Tasks):
#             items = items.title()
#             row = f"{index + 1}:{items}"
#             print(row)
#
#     elif 'edit' in user_action:
#         number = int(user_action[5:])
#         number = number -1 # since people won't know that python starts from 0
#
#         with open('ToDos.txt', 'r') as file_read:
#             Tasks = file_read.readlines()
#
#         new_task = input('Enter new task') +'\n'
#         Tasks[number] = new_task
#
#         with open('ToDos.txt', 'w') as file:
#             file.writelines(Tasks)
#
#     elif 'complete' in user_action:
#         number = int(user_action[9:])
#         with open('ToDos.txt', 'r') as file_read:
#             Tasks = file_read.readlines()
#
#         Tasks.pop(number - 1)
#
#         with open('ToDos.txt', 'w') as file:
#             file.writelines(Tasks)
#
#     elif 'exit' in user_action:
#         break
#     else:
#         print('Command is not valid')
#
# print('Bye!')

# #Lesson 17 Fixing add add new member, edit add new member
#
# while True:
#     user_action = input('Enter add, show, edit, complete or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#
#     if user_action.startswith('add'):
#         Task = user_action[4:] #add + space = 4
#
#         with open('ToDos.txt', 'r') as file_read:
#             Tasks = file_read.readlines()
#
#         Tasks.append(Task +'\n')
#
#         with open('ToDos.txt', 'w') as file:
#             file.writelines(Tasks)
#     # if can we used all places but problem is the code will run all the if conditions elif fixes that and speedup prog
#     elif user_action.startswith('show'):
#         with open('ToDos.txt', 'r') as file_read:
#             Tasks = file_read.readlines()
#
#         Tasks= [items.strip('\n') for items in Tasks] #removes extra line space after each word in the output
#
#         for index, items in enumerate(Tasks):
#             items = items.title()
#             row = f"{index + 1}:{items}"
#             print(row)
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number -1 # since people won't know that python starts from 0
#
#             with open('ToDos.txt', 'r') as file_read:
#                 Tasks = file_read.readlines()
#
#             new_task = input('Enter new task') +'\n'
#             Tasks[number] = new_task
#
#             with open('ToDos.txt', 'w') as file:
#                 file.writelines(Tasks)
#         except ValueError:
#             print("Enter valid command")
#             continue
#
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#             with open('ToDos.txt', 'r') as file_read:
#                 Tasks = file_read.readlines()
#
#             Tasks.pop(number - 1)
#
#             with open('ToDos.txt', 'w') as file:
#                 file.writelines(Tasks)
#
#         except IndexError:
#             print('Enter valid command')
#             continue
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print('Command is not valid')
#
# print('Bye!')

# #Lesson 18 Advance error handling
# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))
#     percentage = value / total_value * 100
#     print(f"That is {percentage}%")
# except ValueError:
#     print("You need to enter a number. Run the program again.")
# except ZeroDivisionError:
#     print("Your total value cannot be zero.")

# #Lesson 18.1
# filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
# for i in filenames:
#     print(filename[:-4].capitalize())

# #Lesson 19 Avoid repetitive code use Custom functions
#
# def get_ToDos():
#     with open('ToDos.txt', 'r') as file_read:
#             Tasks = file_read.readlines()
#     return Tasks
#
#
# while True:
#     user_action = input('Enter add, show, edit, complete or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#
#     if user_action.startswith('add'):
#         Task = user_action[4:] #add + space = 4
#
#         Tasks = get_ToDos()
#
#         Tasks.append(Task +'\n')
#
#         with open('ToDos.txt', 'w') as file:
#             file.writelines(Tasks)
#     # if can we used all places but problem is the code will run all the if conditions elif fixes that and speedup prog
#     elif user_action.startswith('show'):
#         Tasks = get_ToDos()
#
#         Tasks= [items.strip('\n') for items in Tasks] #removes extra line space after each word in the output
#
#         for index, items in enumerate(Tasks):
#             items = items.title()
#             row = f"{index + 1}:{items}"
#             print(row)
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number -1 # since people won't know that python starts from 0
#
#             Tasks = get_ToDos()
#
#             new_task = input('Enter new task') +'\n'
#             Tasks[number] = new_task
#
#             with open('ToDos.txt', 'w') as file:
#                 file.writelines(Tasks)
#         except ValueError:
#             print("Enter valid command")
#             continue
#
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#             Tasks = get_ToDos()
#
#             Tasks.pop(number - 1)
#
#             with open('ToDos.txt', 'w') as file:
#                 file.writelines(Tasks)
#
#         except IndexError:
#             print('Enter valid command')
#             continue
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print('Command is not valid')
#
# print('Bye!')

# #Lesson 19.1 Custom functions
# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     maximum = max(grades)
#     minimum = min(grades)
#     message = f'Max: {maximum}, Min: {minimum}'
#     return message
#
#
# print(get_max())

# #Lesson 19 Optimize code
#
# def get_ToDos(filepath):
#     with open(filepath, 'r') as file_read:
#             Tasks_local = file_read.readlines()
#     return Tasks_local
#
# def write_ToDos(filepath, Tasks_arg):
#     with open(filepath, 'w') as file:
#         file.writelines(Tasks_arg)
#
# while True:
#     user_action = input('Enter add, show, edit, complete or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#
#     if user_action.startswith('add'):
#         Task = user_action[4:] #add + space = 4
#
#         Tasks = get_ToDos('ToDos.txt')
#
#         Tasks.append(Task +'\n')
#
#         write_ToDos('ToDos.txt', Tasks)
#     # if can we used all places but problem is the code will run all the if conditions elif fixes that and speedup prog
#     elif user_action.startswith('show'):
#         Tasks = get_ToDos('ToDos.txt')
#
#         Tasks= [items.strip('\n') for items in Tasks] #removes extra line space after each word in the output
#
#         for index, items in enumerate(Tasks):
#             items = items.title()
#             row = f"{index + 1}:{items}"
#             print(row)
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number -1 # since people won't know that python starts from 0
#
#             Tasks = get_ToDos('ToDos.txt')
#
#             new_task = input('Enter new task') +'\n'
#             Tasks[number] = new_task
#
#             write_ToDos('ToDos.txt', Tasks)
#
#         except ValueError:
#             print("Enter valid command")
#             continue
#
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#             Tasks = get_ToDos('ToDos.txt')
#
#             Tasks.pop(number - 1)
#
#             write_ToDos('ToDos.txt', Tasks)
#
#         except IndexError:
#             print('Enter valid command')
#             continue
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print('Command is not valid')
#
# print('Bye!')

# #Lesson 20 Optimize code
#
# def get_ToDos(filepath = 'ToDos.txt'):
#     with open(filepath, 'r') as file_read:
#             Tasks_local = file_read.readlines()
#     return Tasks_local
#
# def write_ToDos(Tasks_arg, filepath = 'ToDos.txt'):#Tasks_arg - non-default parameter, ToDos.txt - default
#     with open(filepath, 'w') as file:
#         file.writelines(Tasks_arg)
#
# while True:
#     user_action = input('Enter add, show, edit, complete or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#
#     if user_action.startswith('add'):
#         Task = user_action[4:] #add + space = 4
#
#         Tasks = get_ToDos()# need not mention filepath(ToDotxt)it will be called automatically
#
#         Tasks.append(Task +'\n')
#
#         write_ToDos(Tasks,'ToDos.txt') #interchange
#         # write_ToDos(Tasks) simplified version since filepath is inbuilt
#
#     # if can we used all places but problem is the code will run all the if conditions elif fixes that and speedup prog
#     elif user_action.startswith('show'):
#         Tasks = get_ToDos('ToDos.txt')
#
#         Tasks= [items.strip('\n') for items in Tasks] #removes extra line space after each word in the output
#
#         for index, items in enumerate(Tasks):
#             items = items.title()
#             row = f"{index + 1}:{items}"
#             print(row)
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number -1 # since people won't know that python starts from 0
#
#             Tasks = get_ToDos()# need not mention filepath(ToDotxt)it will be called automatically
#
#             new_task = input('Enter new task') +'\n'
#             Tasks[number] = new_task
#
#             write_ToDos(Tasks,'ToDos.txt')
#             #write_ToDos(Tasks) simplified version since filepath is inbuilt
#         except ValueError:
#             print("Enter valid command")
#             continue
#
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#             Tasks = get_ToDos()# need not mention filepath(ToDotxt)it will be called automatically
#
#             Tasks.pop(number - 1)
#
#             write_ToDos(Tasks,'ToDos.txt')
#             # write_ToDos(Tasks) simplified version since filepath is inbuilt
#         except IndexError:
#             print('Enter valid command')
#             continue
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print('Command is not valid')
#
# print('Bye!')

#Lesson 21 Organizing the code in modules c

#from ToDoFunction import get_ToDos, write_ToDos #(Method 1- only 1 line of code)
# import ToDoFunction #(Method 2 if we have to call many functions)
# #from modules import ToDoFunction #(Method 3 We can use directory instead to file)
# while True:
#     user_action = input('Enter add, show, edit, complete or exit:')
#     user_action = user_action.strip()# used to remove extra spaces and store the new updated input
#
#     if user_action.startswith('add'):
#         Task = user_action[4:] #add + space = 4
#
#         Tasks = ToDoFunction.get_ToDos()# need not mention filepath(ToDotxt)it will be called automatically
#
#         Tasks.append(Task +'\n')
#
#         ToDoFunction.write_ToDos(Tasks,'ToDos.txt') #interchange
#         # write_ToDos(Tasks) simplified version since filepath is inbuilt
#
#     # if can we used all places but problem is the code will run all the if conditions elif fixes that and speedup prog
#     elif user_action.startswith('show'):
#         Tasks = ToDoFunction.get_ToDos('ToDos.txt')
#
#         Tasks= [items.strip('\n') for items in Tasks] #removes extra line space after each word in the output
#
#         for index, items in enumerate(Tasks):
#             items = items.title()
#             row = f"{index + 1}:{items}"
#             print(row)
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number -1 # since people won't know that python starts from 0
#
#             Tasks = ToDoFunction.get_ToDos()# need not mention filepath(ToDotxt)it will be called automatically
#
#             new_task = input('Enter new task') +'\n'
#             Tasks[number] = new_task
#
#             ToDoFunction.write_ToDos(Tasks,'ToDos.txt')
#             #write_ToDos(Tasks) simplified version since filepath is inbuilt
#         except ValueError:
#             print("Enter valid command")
#             continue
#
#
#     elif user_action.startswith('complete'):
#         try:
#             number = int(user_action[9:])
#             Tasks = ToDoFunction.get_ToDos()# need not mention filepath(ToDotxt)it will be called automatically
#
#             Tasks.pop(number - 1)
#
#             ToDoFunction.write_ToDos(Tasks,'ToDos.txt')
#             # write_ToDos(Tasks) simplified version since filepath is inbuilt
#         except IndexError:
#             print('Enter valid command')
#             continue
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print('Command is not valid')
#
# print('Bye!')

#Lesson 22 Date feature

import ToDoFunction #(Method 2 if we have to call many functions)
#from modules import ToDoFunction #(Method 3 We can use directory instead to file)
import time
now = time.strftime('%b %d, %Y %H:%M:%S')
print('Today is', now)
while True:
    user_action = input('Enter add, show, edit, complete or exit:')
    user_action = user_action.strip()# used to remove extra spaces and store the new updated input

    if user_action.startswith('add'):
        Task = user_action[4:] #add + space = 4

        Tasks = ToDoFunction.get_ToDos()# need not mention filepath(ToDotxt)it will be called automatically

        Tasks.append(Task +'\n')

        ToDoFunction.write_ToDos(Tasks,'ToDos.txt') #interchange
        # write_ToDos(Tasks) simplified version since filepath is inbuilt

    # if can we used all places but problem is the code will run all the if conditions elif fixes that and speedup prog
    elif user_action.startswith('show'):
        Tasks = ToDoFunction.get_ToDos('ToDos.txt')

        Tasks= [items.strip('\n') for items in Tasks] #removes extra line space after each word in the output

        for index, items in enumerate(Tasks):
            items = items.title()
            row = f"{index + 1}:{items}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number -1 # since people won't know that python starts from 0

            Tasks = ToDoFunction.get_ToDos()# need not mention filepath(ToDotxt)it will be called automatically

            new_task = input('Enter new task') +'\n'
            Tasks[number] = new_task

            ToDoFunction.write_ToDos(Tasks,'ToDos.txt')
            #write_ToDos(Tasks) simplified version since filepath is inbuilt
        except ValueError:
            print("Enter valid command")
            continue


    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            Tasks = ToDoFunction.get_ToDos()# need not mention filepath(ToDotxt)it will be called automatically

            Tasks.pop(number - 1)

            ToDoFunction.write_ToDos(Tasks,'ToDos.txt')
            # write_ToDos(Tasks) simplified version since filepath is inbuilt
        except IndexError:
            print('Enter valid command')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not valid')

print('Bye!')