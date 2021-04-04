from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Episode:
    title: str
    url: str


@dataclass
class Episodes:
    episodes: List[Episode] = field(default_factory=list)

    def __len__(self):
        return len(self.episodes)


@dataclass
class Book:
    title: str
    author: str
    url: Optional[str] = None
