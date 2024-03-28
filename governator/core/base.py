from dataclasses import fields, is_dataclass
from typing import Any

import yaml


class Serializable:
    """Serializable mixin providing serialization to/from dictionary and YAML."""

    def to_dict(self) -> dict:
        """Converts the object to a dictionary, including properties."""
        if is_dataclass(self.__class__):
            d = {}
            for field in fields(self):  # type: ignore
                value = getattr(self, field.name)
                if hasattr(value, "to_serializable"):
                    d[field.name] = value.to_serializable()
                else:
                    d[field.name] = value

            props = {name: getattr(self, name) for name in self.properties()}
            return {**props, **d}
        else:
            raise Exception("Nah gotta provide a to_serializable for non-dataclass")

    def to_serializable(self) -> dict:
        return self.to_dict()

    @classmethod
    def properties(cls) -> set:
        """Finds all properties in the class."""
        return {
            name for name, value in vars(cls).items() if isinstance(value, property)
        }

    @classmethod
    def from_dict(cls, d: dict[Any, Any]) -> Serializable:
        """Creates an instance of the class from a dictionary, excluding properties."""
        filtered_dict = {
            key: value for key, value in d.items() if key not in cls.properties()
        }
        return cls(**filtered_dict)

    def to_yaml(self, key=None) -> str:
        """Converts the object to a YAML string."""
        obj = self.to_serializable()
        if key and key in obj:
            obj = obj[key]
        return yaml.dump(obj, sort_keys=False)

    def to_yaml_file(self, filename: str, wrap_under: str | None = None) -> None:
        """Writes the object to a YAML file."""
        d = self.to_serializable()
        if wrap_under is not None:
            d = {wrap_under: d}
        with open(filename, "w") as file:
            yaml.dump(d, file, sort_keys=False)

    @classmethod
    def from_yaml(cls, yaml_string: str) -> Serializable:
        """Creates an instance of the class from a YAML string, excluding properties."""
        data = yaml.load(yaml_string, Loader=yaml.FullLoader)
        return cls.from_dict(data)

    @classmethod
    def from_yaml_file(cls, filename: str, verbose: bool = True) -> Serializable:
        """Creates an instance of the class from a YAML file, excluding properties."""
        with open(filename) as file:
            print(f"Loading file {filename}")
            data = yaml.load(file, Loader=yaml.FullLoader)
        return cls.from_dict(data)


class SerializableCollection(dict, Serializable):
    def __init__(self, l: list | None = None) -> None:
        l = l or []
        for o in l:
            self[o.key] = o

    def to_serializable(self):
        l = []
        for o in self:
            if hasattr(o, "to_dict"):
                o = o.to_dict()
            l.append(o)
        return l

    @classmethod
    def from_yaml_file(  # type: ignore
        cls, filename: str, object_class: Serializable, key: str | None = None
    ) -> SerializableCollection:
        """Creates an instance of the class from a YAML file, excluding properties."""
        data = None
        with open(filename) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        if key and data:
            data = data.get(key)
        if data:
            data = [object_class.from_dict(o) for o in data]
        return cls(data)

    def append(self, obj):
        self[obj.key] = obj

    def upsert(self, collection):
        self.update(collection)

    def __iter__(self):
        return iter(self.values())
