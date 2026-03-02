# src/domain/models.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Activity:
    id: Optional[int]
    title: str
    type: str  # "Movie" o "Series"
    timestamp: datetime