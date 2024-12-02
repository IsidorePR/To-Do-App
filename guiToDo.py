import ToDoFunction

import FreeSimpleGUI as sg

#from cliTodo import Tasks, new_task(Not required now)

label  =sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="Task")
add_button = sg.Button("Add")
list_box = sg.Listbox(values =ToDoFunction.get_ToDos(), key ="Tasks",
                      enable_events = True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

#Having label,input box, add button in one list make them show in 1 row.Use multiple list if you want to separate
window =sg.Window('My To-Do App',
                  layout = [[label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                  font=('Helvetica', 10))

while True:
    event, value = window.read()
    print(1,event)
    print(2,value)
    print(3,value['Tasks'])
    match event:
        case "Add":
            Tasks = ToDoFunction.get_ToDos()
            new_task = value['Task'] + "\n"
            Tasks.append(new_task)
            ToDoFunction.write_ToDos(Tasks)
            window['Tasks'].update(values=Tasks)
        case "Edit":
            Task_to_edit = value['Tasks'][0]#Based on keys(Task, Tasks)and event(add,edit,complete etc)
            new_task = value["Task"]

            Tasks = ToDoFunction.get_ToDos()
            index = Tasks.index(Task_to_edit)
            Tasks[index] = new_task
            ToDoFunction.write_ToDos(Tasks)
            window['Tasks'].update(values=Tasks)
        case "Complete":
            Task_to_complete = value['Tasks'][0]
            Tasks = ToDoFunction.get_ToDos()
            Tasks.remove(Task_to_complete)
            ToDoFunction.write_ToDos(Tasks)
            window['Tasks'].update(values=Tasks)
        case "Exit":
            break
        case "Tasks":
            window["Task"].update(value=value["Tasks"][0])
        case sg.WINDOW_CLOSED:
            break

window.close()