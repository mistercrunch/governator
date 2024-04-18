from collections.abc import Iterable
from dataclasses import dataclass
from typing import Optional

import governator
from governator.core.base import Serializable


@dataclass
class Role(Serializable):
    role: str
    description: Optional[str] = None

    users: "Optional[Iterable[governator.User]]" = set()
    groups: "Optional[Iterable[governator.Group]]" = set()

    permissions: "Optional[Iterable[governator.Permission]]" = set()

    @property
    def key(self):
        return self.role
