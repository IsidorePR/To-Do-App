import ToDoFunction

import FreeSimpleGUI as sg

#from cliTodo import Tasks, new_task(Not required now)

label  =sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="Task")
add_button = sg.Button("Add")

#Having label,input box, add button in one list make them show in 1 row.Use multiple list if you want to separate
window =sg.Window('My To-Do App',
                  layout = [[label], [input_box, add_button]],
                  font=('Helvetica', 10))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            Tasks = ToDoFunction.get_ToDos()
            new_task = value['Task'] + "\n"
            Tasks.append(new_task)
            ToDoFunction.write_ToDos(Tasks)
        case sg.WINDOW_CLOSED:
            break

window.close()