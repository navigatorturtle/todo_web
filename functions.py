import os
FILEPATH = 'todos.txt'
if not os.path.exists(FILEPATH):
    with open(FILEPATH,'w') as file:
        pass

def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns the todo list
    :param filepath:
    :return: todo list
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos_to_text_file(todos_arg,filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())


