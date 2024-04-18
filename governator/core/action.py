from governator.core.base import Serializable


class Action(Serializable):
    def __init__(self, action):
        self.action = action

    @property
    def key(self):
        return f"{self.action}"
