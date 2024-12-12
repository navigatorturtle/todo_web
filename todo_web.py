import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    newtodo = st.session_state["new_todo"]
    todos.append(newtodo+"\n")
    functions.write_todos_to_text_file(todos)
    st.session_state["new_todo"] = ""

st.title("My todo App")
st.write("This app will increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=f"{todo}{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos_to_text_file(todos)
        del st.session_state[f"{todo}{index}"]
        st.rerun()

st.text_input(label="Enter new todo",placeholder="Enter a todo",
              on_change=add_todo, key= "new_todo",label_visibility="hidden" )