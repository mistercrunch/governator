from collections.abc import Iterable
from typing import TYPE_CHECKING

from governator.core.base import Serializable

if TYPE_CHECKING:
    from governator import Action


class Permission(Serializable):
    def __init__(
        self,
        actions: "Iterable[Action]",
        databases=None,
        catalogs=None,
        schemas=None,
        relations=None,
    ):
        self.actions = actions
        self.databases = databases or set()
        self.catalogs = catalogs or set()
        self.schemas = schemas or set()
        self.relations = relations or set()

    @property
    def key(self):
        return "???"

    __slots__ = ("actions", "databases", "catalogs", "schemas", "relations")

    __annotations__ = {
        "actions": "set[Action]",
        "databases": "set[Database]",
        "catalogs": "set[Catalog]",
        "schemas": "set[Schema]",
        "relations": "set[Relation]",
    }
