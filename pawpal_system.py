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
        pass

    def update_preferences(self, style: str, minutes: int) -> None:
        pass

    def get_all_tasks(self) -> List["Task"]:
        pass


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str
    age: int
    notes: str
    tasks: List["Task"] = field(default_factory=list)

    def update_info(self, name: str, age: int, notes: str) -> None:
        pass

    def view_tasks(self) -> List["Task"]:
        pass

    def add_task(self, task: "Task") -> None:
        pass

    def edit_task(self, task_id: str, updates: Dict[str, object]) -> None:
        pass

    def remove_task(self, task_id: str) -> None:
        pass


@dataclass
class Task:
    task_id: str
    title: str
    duration_minutes: int
    priority: int
    preferred_time: str
    status: str

    def edit_task(self, updates: Dict[str, object]) -> None:
        pass

    def mark_complete(self) -> None:
        pass


class Scheduler:
    def generate_daily_schedule(
        self,
        owner: Owner,
    ) -> List[Task]:
        pass

    def rank_tasks_by_priority_and_fit(
        self,
        tasks: List[Task],
        available_minutes: int,
    ) -> List[Task]:
        pass

    def build_timeline(self, tasks: List[Task]) -> List[str]:
        pass

    def explain_plan(self) -> str:
        pass
