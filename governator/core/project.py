from dataclasses import dataclass
from typing import Optional

from governator.config import conf
from governator.core.database import Database


@dataclass
class Project:
    databases: list[Database]
    path: Optional[str] = None

    def __post_init__(self):
        self.path = self.path or conf["GOVERNATOR_FOLDER"]

    def load(self, database_schema=None):
        pass

    def flush(self):
        pass
