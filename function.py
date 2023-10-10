FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH):
    """ to read the text file and return
    to do list items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.read().splitlines()
    return todos_local


def write_todos(todos_arg, filepath = FILEPATH):
    """ Write to do items to the list"""
    todos_arg = [arg + '\n' for arg in todos_arg]
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
