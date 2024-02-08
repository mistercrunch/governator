from typing import Optional

from governator.config import conf
from governator.core.database_connection import DatabaseConnection


class Project:
    databases: list[DatabaseConnection]

    def __init__(self, path: Optional[str] = None):
        self.path = path or conf["GOVERNATOR_FOLDER"]

    def load(self, database_schema=None):
        pass

    def flush(self):
        pass
