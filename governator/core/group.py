from dataclasses import dataclass
from typing import Optional

from governator.core.base import Serializable
from governator.core.user import User


@dataclass
class Group(Serializable):
    group: str
    users: list[User]
    description: Optional[str] = None

    @property
    def key(self):
        return self.group
