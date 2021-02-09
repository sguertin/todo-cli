from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path
from dataclasses_json import dataclass_json, LetterCase


class Status(Enum):
    Urgent: int = 6
    Overdue: int = 5
    DueToday: int = 4
    DueThisWeek: int = 3
    DueNextWeek: int = 2
    DueThisMonth: int = 1
    DueLater: int = 0


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TodoItem:
    due: datetime
    summary: str
    details: str
    category: str
    urgent: bool

    @property
    def status(self) -> Status:
        if self.urgent:
            return Status.Urgent
        difference = self.due.date() - datetime.today().date()
        if difference.days == 0:
            return Status.DueToday
        if difference.days < 0:
            return Status.Overdue
        if difference.days <= 7:
            return Status.DueThisWeek
        if difference.days <= 14:
            return Status.DueNextWeek
        if self.due.month == datetime.today().month:
            return Status.DueThisMonth
        return Status.DueLater
    
    def __lt__(self, other) -> bool:        
        return self.due < other.due
    
    def __le__(self, other) -> bool:
        return self.due <= other.due
    
    def __gt__(self, other) -> bool:
        return self.due > other.due
    
    def __ge__(self, other) -> bool:
        return self.due >= other.due


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TodoList:
    todo_items: list[TodoItem]
    file_path: Path
