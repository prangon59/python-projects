import functions
import time

current_time = time.strftime("%b %d, %Y %H:%M:%S")
print(f"\nit is {current_time}")

# Load todos from the file at the start
todos = functions.get_todos()

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        # Get the todo from user input after "add " (i.e., everything after index 4)
        todo = user_action[4:].strip()
        todos = functions.get_todos()  # Load current todos from file
        todos.append(todo + "\n")  # Append new todo with a newline
        functions.save_todos(todos)  # Save the updated list back to the file

    elif user_action.startswith("show"):
        todos = functions.get_todos()  # Reload todos from file
        if not todos:
            print("No todos available.")
        else:
            for index, item in enumerate(todos):
                row = f"{index + 1} - {item.strip()}"  # Strip newlines for cleaner output
                print(row)

    elif user_action.startswith("edit"):
        try:
            # Get the number after "edit" (e.g., "edit 2" should extract '2')
            number = int(user_action[5:].strip()) - 1
            todos = functions.get_todos()  # Reload todos from file
            if 0 <= number < len(todos):
                new_todo = input("Enter new todo: ").strip()
                todos[number] = new_todo + "\n"  # Update the todo with the new input
                functions.save_todos(todos)  # Save changes to the file
            else:
                print("Invalid todo number.")
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            # Get the number after "complete" (e.g., "complete 2" should extract '2')
            number = int(user_action[9:].strip()) - 1
            todos = functions.get_todos()  # Reload todos from file
            if 0 <= number < len(todos):
                todos.pop(number)  # Remove the todo from the list
                functions.save_todos(todos)  # Save the updated list
            else:
                print("Invalid todo number.")
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("exit"):
        break
