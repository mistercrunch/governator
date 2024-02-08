from typing import Optional

from governator.core.base import Serializable


class DatabaseConnection(Serializable):
    def __init__(
        self, key: str, label: Optional[str] = None, description: Optional[str] = None
    ):
        self.key = key
        self.label = label
        self.description = description

    def to_dict(self):
        return {
            "key": self.key,
            "label": self.label,
            "description": self.description,
        }
