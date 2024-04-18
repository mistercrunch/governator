from dataclasses import dataclass

from governator.core.base import Serializable


@dataclass
class Schema(Serializable):
    schema: str

    @property
    def key(self):
        return f"{self.schema}"
