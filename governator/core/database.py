from typing import Optional

from governator.core.base import Serializable


class Database(Serializable):
    def __init__(
        self,
        key: str,
        label: Optional[str] = None,
        description: Optional[str] = None,
        connection_string: Optional[str] = None,
    ):
        self.key = key
        self.label = label
        self.description = description
        self.connection_string = connection_string

    def to_dict(self):
        return {
            "key": self.key,
            "label": self.label,
            "description": self.description,
            "connection_string": self.connection_string,
        }

    def get_database_interface(self):
        pass

    def crawl(self, fetch_column_metadata: bool = False):
        pass
