from pawpal_system import Owner, Pet, Task, Scheduler
import streamlit as st

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        owner_id="O1",
        name="Hello Kitty",
        preferred_schedule_style="priority-first",
        daily_available_minutes=60,
    )

if "pet_counter" not in st.session_state:
    st.session_state.pet_counter = 1

if "task_counter" not in st.session_state:
    st.session_state.task_counter = 1

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+.

This app helps a pet owner manage pet care tasks and generate a daily plan
based on available time and task priority.
"""
)

st.divider()

st.subheader("Owner Settings")

owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
available_minutes = st.number_input(
    "Available minutes today",
    min_value=1,
    max_value=600,
    value=st.session_state.owner.daily_available_minutes,
)

if st.button("Update Owner Preferences"):
    st.session_state.owner.name = owner_name
    st.session_state.owner.update_preferences("priority-first", int(available_minutes))
    st.success("Owner preferences updated.")

st.divider()

st.subheader("Add a Pet")

pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["Dog", "Cat", "Other"])
age = st.number_input("Age", min_value=0, max_value=50, value=1)
notes = st.text_input("Notes")

if st.button("Add Pet"):
    if pet_name.strip():
        pet = Pet(
            pet_id=f"P{st.session_state.pet_counter}",
            name=pet_name,
            species=species,
            age=int(age),
            notes=notes,
        )
        st.session_state.owner.add_pet(pet)
        st.session_state.pet_counter += 1
        st.success(f"{pet_name} added.")
    else:
        st.error("Please enter a pet name.")

if st.session_state.owner.pets:
    st.write("Current pets:")
    for pet in st.session_state.owner.pets:
        st.write(f"- {pet.name} ({pet.species}, age {pet.age})")
else:
    st.info("No pets added yet.")

st.divider()

st.subheader("Add a Task")

if st.session_state.owner.pets:
    pet_options = [pet.name for pet in st.session_state.owner.pets]
    selected_pet_name = st.selectbox("Choose pet", pet_options)

    task_title = st.text_input("Task title", value="Morning walk")
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority_label = st.selectbox("Priority", ["low", "medium", "high"], index=2)
    preferred_time = st.selectbox("Preferred time", ["morning", "afternoon", "evening"])

    if priority_label == "low":
        priority_value = 1
    elif priority_label == "medium":
        priority_value = 2
    else:
        priority_value = 3

    if st.button("Add Task"):
        selected_pet = next(
            pet for pet in st.session_state.owner.pets if pet.name == selected_pet_name
        )

        task = Task(
            task_id=f"T{st.session_state.task_counter}",
            title=task_title,
            duration_minutes=int(duration),
            priority=priority_value,
            preferred_time=preferred_time,
        )

        selected_pet.add_task(task)
        st.session_state.task_counter += 1
        st.success(f"Task added for {selected_pet.name}.")
else:
    st.info("Add a pet before adding tasks.")

st.divider()

st.subheader("Current Tasks")

all_tasks = st.session_state.owner.get_all_tasks()
if all_tasks:
    task_rows = []
    for task in all_tasks:
        task_rows.append(
            {
                "Title": task.title,
                "Duration": task.duration_minutes,
                "Priority": task.priority,
                "Preferred Time": task.preferred_time,
                "Status": task.status,
            }
        )
    st.table(task_rows)
else:
    st.info("No tasks added yet.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate Schedule"):
    scheduler = Scheduler()
    schedule = scheduler.generate_daily_schedule(st.session_state.owner)
    timeline = scheduler.build_timeline(schedule)

    if schedule:
        st.success("Schedule generated.")
        st.write("### Today's Schedule")
        for item in timeline:
            st.write(item)

        st.write("### Plan Explanation")
        st.write(scheduler.explain_plan())
    else:
        st.warning("No tasks fit within the available time.")