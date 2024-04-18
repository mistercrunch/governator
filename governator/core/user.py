from dataclasses import dataclass

from governator.core.base import Serializable


@dataclass
class User(Serializable):
    username: str

    @property
    def key(self):
        return self.username
