FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    try:
        with open(filepath, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_todos(todos, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("something")