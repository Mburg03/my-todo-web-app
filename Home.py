import streamlit as st
import functions

# https://mburg03-my-todo-web-app-home-yqwux3.streamlit.app/
todos = functions.get_todos()
deleted_todos = functions.get_deleted_todos()
is_todo_empty = False

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if (not todo or not todo.strip()): 
        global is_todo_empty 
        is_todo_empty = True
    else: 
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  


st.title("My Todo App ✏️") 
st.subheader("Keep your tasks simple!")
st.write("This app is to increase your <b>productivity</b>.", unsafe_allow_html=True)

todo = st.text_input(label="New todo", label_visibility='hidden', placeholder="Add new todo...", on_change=add_todo, key='new_todo')

if is_todo_empty:
    st.waring('Please provide a todo', icon='⚠️')
    
todo_priority = st.selectbox("Select the priority of your todo", ('-','Top priority', 'Half priority', 'Low priority'), placeholder='Select here', label_visibility='visible', key='todo_priority')


def add_todo2(todo_to_write, todo_priority, color):
    todo_to_write += "\n"
    todos.append(todo_to_write)
    functions.write_todos(todo_to_write)


st.write("")

# Top priority todos
st.markdown(":gray[● **Todos**]")

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
    st.write(f":grey[*<del>{deleted_todo}</del>*]", unsafe_allow_html=True)
    
st.write("")
st.button(label="Clear completed todos", type="primary", key="clear_completed_todos_button", on_click=functions.empty_deleted_todos)
    

st.write("-------------------------------------------")

st.markdown("")
st.session_state
