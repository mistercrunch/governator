from dataclasses import dataclass
from typing import Literal

from governator.core.base import Serializable, SerializableCollection


@dataclass
class Column(Serializable):
    key: str
    name: str
    data_type: str


@dataclass
class Relation(Serializable):
    # the database schema
    database_schema: str
    # the view_name or table_name
    reference: str
    relation_type: Literal["view", "table"]
    columns: SerializableCollection

    include_count_metric: bool = True
    include_columns_as_dimensions: bool = True

    @property
    def key(self):
        return f"{self.database_schema}.{self.reference}"
