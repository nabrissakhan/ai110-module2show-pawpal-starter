from pawpal_system import Owner, Pet, Task, Scheduler


def test_mark_complete_changes_status():
    task = Task(
        task_id="T1",
        title="Feed Clifford",
        duration_minutes=10,
        priority=2,
        preferred_time="morning",
    )

    task.mark_complete()

    assert task.status == "complete"


def test_add_task_increases_task_count():
    dog = Pet(
        pet_id="P1",
        name="Clifford",
        species="Dog",
        age=4,
        notes="Needs exercise every day",
    )

    task = Task(
        task_id="T1",
        title="Morning walk",
        duration_minutes=30,
        priority=3,
        preferred_time="morning",
    )

    dog.add_task(task)

    assert len(dog.tasks) == 1
    assert dog.tasks[0].title == "Morning walk"


def test_scheduler_respects_time_limit():
    owner = Owner(
        owner_id="O1",
        name="Hello Kitty",
        preferred_schedule_style="priority-first",
        daily_available_minutes=30,
    )

    dog = Pet(
        pet_id="P1",
        name="Clifford",
        species="Dog",
        age=4,
        notes="Needs exercise every day",
    )

    task1 = Task(
        task_id="T1",
        title="Morning walk",
        duration_minutes=30,
        priority=3,
        preferred_time="morning",
    )
    task2 = Task(
        task_id="T2",
        title="Feed Clifford",
        duration_minutes=10,
        priority=2,
        preferred_time="morning",
    )

    dog.add_task(task1)
    dog.add_task(task2)
    owner.add_pet(dog)

    scheduler = Scheduler()
    schedule = scheduler.generate_daily_schedule(owner)

    assert len(schedule) == 1
    assert schedule[0].title == "Morning walk"


def test_scheduler_orders_by_priority():
    owner = Owner(
        owner_id="O1",
        name="Hello Kitty",
        preferred_schedule_style="priority-first",
        daily_available_minutes=60,
    )

    cat = Pet(
        pet_id="P2",
        name="Garfield",
        species="Cat",
        age=2,
        notes="Takes evening medication",
    )

    low_priority_task = Task(
        task_id="T1",
        title="Play enrichment session",
        duration_minutes=25,
        priority=1,
        preferred_time="afternoon",
    )
    high_priority_task = Task(
        task_id="T2",
        title="Give Garfield medication",
        duration_minutes=5,
        priority=3,
        preferred_time="evening",
    )

    cat.add_task(low_priority_task)
    cat.add_task(high_priority_task)
    owner.add_pet(cat)

    scheduler = Scheduler()
    schedule = scheduler.generate_daily_schedule(owner)

    assert schedule[0].title == "Give Garfield medication"