import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("A simple todo app")
st.write("Increace your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")
