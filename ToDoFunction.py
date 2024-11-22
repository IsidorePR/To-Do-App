def get_ToDos(filepath = 'ToDos.txt'):
    with open(filepath, 'r') as file_read:
            Tasks_local = file_read.readlines()
    return Tasks_local

def write_ToDos(Tasks_arg, filepath = 'ToDos.txt'):#Tasks_arg - non-default parameter, ToDos.txt - default
    with open(filepath, 'w') as file:
        file.writelines(Tasks_arg)
