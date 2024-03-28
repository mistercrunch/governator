from dataclasses import dataclass

from governator.core.base import Serializable, SerializableCollection
from governator.core.user import User


@dataclass
class Group(Serializable):
    group: str
    description: str

    users: list[User]

    @property
    def key(self):
        return self.group
