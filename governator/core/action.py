from dataclasses import dataclass

from governator.core.base import Serializable


@dataclass
class Action(Serializable):
    action: str

    @property
    def key(self):
        return f"{self.action}"
