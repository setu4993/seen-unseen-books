from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Episode:
    title: str
    url: str

    def md(self) -> str:
        return f"[{self.title}]({self.url})"


@dataclass
class Episodes:
    episodes: List[Episode] = field(default_factory=list)

    def __len__(self) -> int:
        return len(self.episodes)

    def md(self, tabbed: bool = True) -> List[str]:
        prefix = "    " if tabbed else ""
        return [f"{prefix}- {episode.md()}" for episode in self.episodes]


@dataclass
class Book:
    title: str
    author: str
    url: Optional[str] = None

    def md(self) -> str:
        return f"[{self.title} by {self.author}]({self.url})"
