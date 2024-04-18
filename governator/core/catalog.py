from dataclasses import dataclass

from governator.core.base import Serializable


@dataclass
class Catalog(Serializable):
    catalog: str

    @property
    def key(self):
        return f"{self.catalog}"
