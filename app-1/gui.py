import functions
import PySimpleGUI as gui
import time

gui.theme("Black")

clock_label = gui.Text("", key="clock")
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
                             layout = [[clock_label],
                                       [label],
                                       [input_box, add_button], 
                                       [todo_list, edit_button, complete_button],
                                       [exit_button]],
                             font=('Helvetica', 10))

while True:
    event, values = window_instance.read(timeout=200)
    # print(event)
    # print(values)

    if event == gui.WIN_CLOSED or event == "Exit":
        break

    # Only update the clock if the window is still open
    if event != gui.WIN_CLOSED:
        window_instance["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo_input_box"].strip() + "\n"
            todos.append(new_todo)
            functions.save_todos(todos)
            window_instance["todos_list_box"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos_list_box"][0]
                new_todo = values["todo_input_box"].strip()
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                # todos[todos.index(todo_to_edit)] = new_todo
                todos[index] = new_todo + "\n"
                functions.save_todos(todos)
                window_instance["todos_list_box"].update(values=todos)
            except IndexError:
                gui.popup("Please select a to-do first!")

        case "Complete":
            try:
                todo_to_complete = values["todos_list_box"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.save_todos(todos)
                window_instance["todos_list_box"].update(values=todos)
                window_instance["todo_input_box"].update(value="")
            except IndexError:
                gui.popup("Please select a to-do first!")

        case "Exit":
            break

        case "todos_list_box":
            window_instance["todo_input_box"].update(value=values["todos_list_box"][0].strip())

        case gui.WIN_CLOSED:
            break

window_instance.close()