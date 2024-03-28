from dataclasses import dataclass

import governator
from governator.core.base import Serializable


@dataclass
class Role(Serializable):
    role: str
    description: str

    users: list[governator.User]
    groups: list[governator.Group]

    relations: list[governator.Relation]
    schemas: list[governator.Relation]
    databases: list[governator.Relation]

    @property
    def key(self):
        return self.role
