from pawpal_system import Owner, Pet, Task, Scheduler


def main() -> None:
    owner = Owner(
        owner_id="O1",
        name="Hello Kitty",
        preferred_schedule_style="priority-first",
        daily_available_minutes=60,
    )

    dog = Pet(
        pet_id="P1",
        name="Clifford",
        species="Dog",
        age=4,
        notes="Needs exercise every day",
    )

    cat = Pet(
        pet_id="P2",
        name="Garfield",
        species="Cat",
        age=2,
        notes="Takes evening medication",
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
    task3 = Task(
        task_id="T3",
        title="Give Garfield medication",
        duration_minutes=5,
        priority=3,
        preferred_time="evening",
    )
    task4 = Task(
        task_id="T4",
        title="Play enrichment session",
        duration_minutes=25,
        priority=1,
        preferred_time="afternoon",
    )

    dog.add_task(task1)
    dog.add_task(task2)
    cat.add_task(task3)
    cat.add_task(task4)

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler()
    daily_schedule = scheduler.generate_daily_schedule(owner)
    timeline = scheduler.build_timeline(daily_schedule)

    print("Today's Schedule:")
    for item in timeline:
        print(item)

    print("\nPlan Explanation:")
    print(scheduler.explain_plan())


if __name__ == "__main__":
    main()