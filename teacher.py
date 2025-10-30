from __future__ import annotations
from dataclasses import dataclass
from member import Member

@dataclass
class Teacher(Member):
    teacher_id: int = 0

    def display(self) -> str:
        return f"Teacher #{self.teacher_id} | {self.full_name}"

    def display_group(self) -> str:
        return f"Groups of {self.full_name}"

    def assign_event(self, event: "Event") -> None:
        if self not in event.organizers:
            event.organizers.append(self)

    def assign_group(self, student: "Student") -> None:
        pass
