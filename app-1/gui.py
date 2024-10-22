import functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip = "Enter a to-do")
button = gui.Button("Add")

window_instance = gui.Window("My To-do App", layout = [[label], [input_box, button]])
window_instance.read()
window_instance.close()