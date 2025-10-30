from __future__ import annotations
from dataclasses import dataclass
from datetime import date

@dataclass
class Subscription:
    student_id: int
    amount: float
    date: date
    status: str = "unpaid"

    def display(self) -> str:
        return f"Sub({self.student_id}) {self.amount} on {self.date.isoformat()} [{self.status}]"

    def mark_paid(self) -> None:
        self.status = "paid"

    def mark_unpaid(self) -> None:
        self.status = "unpaid"
