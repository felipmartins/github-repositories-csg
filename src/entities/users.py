from typing import List
from dataclasses import dataclass
from src.entities.repos import Repo


@dataclass
class User:
    name: str
    repos: List[Repo]

    def to_dict(self):
        return {
            "name": self.name,
            "repos": [repo.to_dict() for repo in self.repos],
        }


@dataclass
class StoredUser(User):
    id: str
    is_new: bool
