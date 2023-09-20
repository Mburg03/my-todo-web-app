import streamlit as st
import functions

todos = functions.get_todos()
deleted_todos = functions.get_deleted_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App") 
st.subheader("Keep your tasks simple!")
st.write("This app is to increase your <b>productivity</b>.", unsafe_allow_html=True)
st.text_input(label="New todo", label_visibility='hidden', placeholder="Add new todo...", on_change=add_todo, key='new_todo')
st.write("")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        deleted_todos.append(todo)
        functions.write_deleted_todo(deleted_todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.write("-------------------------------------------")
st.markdown("**Completed todos:**")

for deleted_todo in deleted_todos:
    st.write(f"•:grey[<del>{deleted_todo}</del>]", unsafe_allow_html=True)
    
st.write("")
st.button(label="Clear completed todos", type="primary", key="clear_completed_todos_button", on_click=functions.empty_deleted_todos)
    

st.write("-------------------------------------------")

st.markdown("")
st.session_state
