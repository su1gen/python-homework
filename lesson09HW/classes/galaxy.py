class Galaxy:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __str__(self):
        return f'Galaxy: {self.name}'

    def __repr__(self):
        return self.__str__()