from dataclasses import dataclass

from governator import Action, Catalog, Database, Relation, Schema
from governator.core.base import Serializable


@dataclass
class Permission(Serializable):
    actions: "set[Action]"

    databases: "set[Database]" = set()
    catalogs: "set[Catalog]" = set()
    schemas: "set[Schema]" = set()
    relations: "set[Relation]" = set()

    @property
    def key(self):
        return "???"
