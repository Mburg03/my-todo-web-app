FILEPATH = "todos.txt"
DELETED_TODOS_FILEPATH = "deleted_todos.txt"


def get_deleted_todos(filepath=DELETED_TODOS_FILEPATH):
    with open(filepath, 'r') as file_local:
        deleted_todos_local = file_local.readlines()
    return deleted_todos_local


def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes the to-do items list in the text file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


def write_deleted_todo(todos_arg, filepath=DELETED_TODOS_FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


def empty_deleted_todos(filepath=DELETED_TODOS_FILEPATH):
    with open(filepath, 'w') as file:
        pass

if __name__ == "__main__":
    print("Hello there!")
    print(get_todos())
