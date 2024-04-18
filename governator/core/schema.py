class Schema:
    def __init__(self, schema):
        self.schema = schema

    @property
    def key(self):
        return f"{self.schema}"
