from typing import Any

from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine.reflection import Inspector


class BaseDatabaseInterface:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.engine = self.get_sqla_engine(connection_string)
        self.metadata = MetaData(bind=self.engine)
        self.inspector = self.get_sqla_inspector()

    def get_sqla_engine(self, connection_string):
        return create_engine(self.connection_string)

    def get_sqla_inspector(self):
        return Inspector.from_engine(self.engine)

    def get_schemas(self):
        inspector = Inspector.from_engine(self.engine)
        return inspector.get_schema_names()

    def get_tables(self, schema=None):
        if schema:
            return self.inspector.get_table_names(schema=schema)
        else:
            tables = []
            for schema in self.get_schemas():
                tables += self.inspector.get_table_names(schema=schema)
            return tables

    def get_columns(self, table_name, schema=None):
        return self.inspector.get_columns(table_name, schema=schema)

    def crawl(self, fetch_column_metadata=False) -> dict[str, Any]:
        inspector = Inspector.from_engine(self.engine)
        database_structure: dict[str, Any] = {}

        for schema in inspector.get_schema_names():
            database_structure[schema] = {"tables": {}}
            for table_name in inspector.get_table_names(schema=schema):
                database_structure[schema]["tables"][table_name] = {"columns": {}}
                if fetch_column_metadata:
                    for column in inspector.get_columns(table_name, schema=schema):
                        database_structure[schema]["tables"][table_name]["columns"][
                            column["name"]
                        ] = {
                            "type": str(column["type"]),
                            "nullable": column["nullable"],
                            "default": str(column["default"])
                            if column["default"]
                            else None,
                        }
        return database_structure
