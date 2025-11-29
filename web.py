import logging
import streamlit as st
from modules import functions

st_logger = logging.getLogger("streamlit")
st_logger.setLevel(logging.DEBUG)

st.title("My TODOs App")
st.subheader("Helps manage my TODO list.")
st.write ("Boosts my productivity too!")

existing_todos = functions.load_todos()

def add_todo():
    todo_to_add = st.session_state["new_todo"] + "\n"
    existing_todos.append(todo_to_add)
    functions.write_todos(existing_todos)
    st.session_state["new_todo"] = ""

for index, todo in enumerate(existing_todos):
    checkbox_val = st.checkbox(todo, key=todo)
    if checkbox_val:
        existing_todos.pop(index)
        functions.write_todos(existing_todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add TODO", label_visibility="collapsed", placeholder="Enter new TODO to add...", on_change=add_todo, key="new_todo")
