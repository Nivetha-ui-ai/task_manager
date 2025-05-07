import streamlit as st

# Initialize task list in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("Simple Task Manager")

# Add a new task
new_task = st.text_input("Enter a new task")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success("Task added!")

st.write("## Your Tasks:")

# Display tasks with checkboxes
for i, t in enumerate(st.session_state.tasks):
    is_done = st.checkbox(t["task"], value=t["done"], key=i)
    st.session_state.tasks[i]["done"] = is_done

# Show only completed tasks
st.write("### Completed Tasks:")
for t in st.session_state.tasks:
    if t["done"]:
        st.write(f"✅ {t['task']}")
