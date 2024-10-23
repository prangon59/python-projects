import functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip = "Enter a to-do", key="todo_input_box")
add_button = gui.Button("Add")
todo_list = gui.Listbox(values=functions.get_todos(),
                        key="todos_list_box",
                        enable_events=True,
                        size=[45, 10])
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window_instance = gui.Window("My To-do App", 
                             layout = [[label], 
                                       [input_box, add_button], 
                                       [todo_list, edit_button, complete_button]]
                                       [exit_button], 
                             font=('Helvetica', 14))
window_instance.read()

while True:
    event, values = window_instance.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo_input_box"].strip() + "\n"
            todos.append(new_todo)
            functions.save_todos(todos)
            window_instance["todos_list_box"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos_list_box"][0]
            new_todo = values["todo_input_box"].strip()
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            # todos[todos.index(todo_to_edit)] = new_todo
            todos[index] = new_todo + "\n"
            functions.save_todos(todos)
            window_instance["todos_list_box"].update(values=todos)

        case "Complete":
            todo_to_complete = values["todos_list_box"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.save_todos(todos)
            window_instance["todos_list_box"].update(values=todos)
            window_instance["todo_input_box"].update(value="")

        case "Exit":
            break

        case "todos_list_box":
            window_instance["todo_input_box"].update(value=values["todos_list_box"][0].strip())

        case gui.WIN_CLOSED:
            break

window_instance.close()