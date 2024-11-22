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