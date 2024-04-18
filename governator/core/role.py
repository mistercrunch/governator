from collections.abc import Iterable
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    import governator


class Role:
    def __init__(
        self,
        role: str,
        description: "Optional[str]" = None,
        users: "Optional[Iterable[governator.User]]" = None,
        groups: "Optional[Iterable[governator.Group]]" = None,
        permissions: "Optional[Iterable[governator.Permission]]" = None,
    ):
        self.role = role
        self.description = description
        self.users = users or set()
        self.groups = groups or set()
        self.permissions = permissions or set()

    @property
    def key(self) -> str:
        return self.role
