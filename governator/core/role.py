import typing

import governator


class Role:
    def __init__(
        self,
        role: str,
        description: typing.Optional[str] = None,
        users: typing.Optional[typing.Iterable[governator.User]] = None,
        groups: typing.Optional[typing.Iterable[governator.Group]] = None,
        permissions: typing.Optional[typing.Iterable[governator.Permission]] = None,
    ):
        self.role = role
        self.description = description
        self.users = users or set()
        self.groups = groups or set()
        self.permissions = permissions or set()

    @property
    def key(self) -> str:
        return self.role
