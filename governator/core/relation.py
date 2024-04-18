from typing import Literal

from governator.core.base import SerializableCollection


class Column:
    def __init__(self, key: str, name: str, description: str, data_type: str):
        self.key = key
        self.name = name
        self.description = description
        self.data_type = data_type


class Relation:
    # the database schema
    database_schema: str
    # the view_name or table_name
    reference: str
    relation_type: Literal["view", "table"]
    columns: SerializableCollection

    include_count_metric: bool = True
    include_columns_as_dimensions: bool = True

    def __init__(
        self,
        database_schema: str,
        reference: str,
        relation_type: Literal["view", "table"],
        columns: SerializableCollection,
        include_count_metric: bool = True,
        include_columns_as_dimensions: bool = True,
    ):
        self.database_schema = database_schema
        self.reference = reference
        self.relation_type = relation_type
        self.columns = columns
        self.include_count_metric = include_count_metric
        self.include_columns_as_dimensions = include_columns_as_dimensions

    @property
    def key(self):
        return f"{self.database_schema}.{self.reference}"
