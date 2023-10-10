import streamlit as st
import function


todos = function.get_todos()
def add_todo():
    if not st.session_state["new_todo"] == "":
        todo = st.session_state["new_todo"]
        todos.append(todo)
        function.write_todos(todos)
    else:
        print("Write something that counts")


st.title("My To-do App")
st.subheader("This is my todo app.")
st.write("This app is to increase my motivation")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add something new to do...",
              on_change=add_todo, key="new_todo")

st.session_state