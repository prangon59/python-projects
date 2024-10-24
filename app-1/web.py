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

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", 
              placeholder="Add new todo...",
              key="new_todo",
              on_change=add_todo)
