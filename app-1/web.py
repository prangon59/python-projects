import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo_from_input = st.session_state["new_todo"].strip() + "\n"
    todos.append(new_todo_from_input)
    functions.save_todos(todos)

st.title("My Todo App")
st.subheader("A simple todo app")
st.write("Increace your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", 
              placeholder="Add new todo...",
              key="new_todo",
              on_change=add_todo)

st.session_state