from governator.core.base import Serializable


class Group(Serializable):
    def __init__(self, group, users=None, description=None):
        self.group = group
        self.users = users or []
        self.description = description

    @property
    def key(self):
        return self.group
