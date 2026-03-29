from dataclasses import dataclass, field
from typing import Dict, List


class Owner:
    def __init__(
        self,
        owner_id: str,
        name: str,
        preferred_schedule_style: str,
        daily_available_minutes: int,
    ) -> None:
        self.owner_id = owner_id
        self.name = name
        self.preferred_schedule_style = preferred_schedule_style
        self.daily_available_minutes = daily_available_minutes
        self.pets: List["Pet"] = []

    def add_pet(self, pet: "Pet") -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def update_preferences(self, style: str, minutes: int) -> None:
        """Update scheduling style and available daily minutes."""
        self.preferred_schedule_style = style
        self.daily_available_minutes = minutes

    def get_all_tasks(self) -> List["Task"]:
        """Return all tasks across all pets owned by this owner."""
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    age: int
    notes: str
    tasks: List["Task"] = field(default_factory=list)

    def update_info(self, name: str, age: int, notes: str) -> None:
        """Update this pet's basic information."""
        self.name = name
        self.age = age
        self.notes = notes

    def view_tasks(self) -> List["Task"]:
        """Return this pet's current task list."""
        return self.tasks

    def add_task(self, task: "Task") -> None:
        """Add one care task to this pet."""
        self.tasks.append(task)

    def edit_task(self, task_id: str, updates: Dict[str, object]) -> None:
        """Update fields on a task that matches task_id."""
        for task in self.tasks:
            if task.task_id == task_id:
                for key, value in updates.items():
                    if hasattr(task, key):
                        setattr(task, key, value)
                return

    def remove_task(self, task_id: str) -> None:
        """Remove the first task that matches task_id."""
        for index, task in enumerate(self.tasks):
            if task.task_id == task_id:
                self.tasks.pop(index)
                return


@dataclass
class Task:
    task_id: str
    title: str
    duration_minutes: int
    priority: int
    preferred_time: str
    status: str = "pending"

    def edit_task(self, updates: Dict[str, object]) -> None:
        """Update this task with provided field values."""
        for key, value in updates.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def mark_complete(self) -> None:
        """Set this task status to complete."""
        self.status = "complete"


class Scheduler:
    def generate_daily_schedule(
        self,
        owner: Owner,
    ) -> List[Task]:
        """Build a daily task list for an owner using available time."""
        all_tasks = owner.get_all_tasks()
        return self.rank_tasks_by_priority_and_fit(
            all_tasks,
            owner.daily_available_minutes,
        )

    def rank_tasks_by_priority_and_fit(
        self,
        tasks: List[Task],
        available_minutes: int,
    ) -> List[Task]:
        """Sort tasks by priority and keep only tasks that fit in time."""
        sorted_tasks = sorted(
            tasks,
            key=lambda task: (-task.priority, task.duration_minutes),
        )

        selected_tasks: List[Task] = []
        used_minutes = 0

        for task in sorted_tasks:
            next_total = used_minutes + task.duration_minutes
            if next_total <= available_minutes:
                selected_tasks.append(task)
                used_minutes = next_total

        return selected_tasks

    def build_timeline(self, tasks: List[Task]) -> List[str]:
        """Return a readable line for each scheduled task."""
        timeline: List[str] = []
        for index, task in enumerate(tasks, start=1):
            line = (
                f"{index}. {task.title} "
                f"({task.duration_minutes} min, "
                f"priority {task.priority}, "
                f"{task.status})"
            )
            timeline.append(line)
        return timeline

    def explain_plan(self) -> str:
        """Explain how the daily plan was selected."""
        return "Tasks were selected by highest priority first and limited by available time."
