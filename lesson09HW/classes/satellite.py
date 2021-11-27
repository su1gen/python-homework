class Satellite:
    def __init__(self, name, distance, planet_id, id=None):
        self.id = id
        self.name = name
        self.distance = distance
        self.planet_id = planet_id

    def __str__(self):
        return f'Satellite: {self.name}, {self.distance}, {self.planet_id}'

    def __repr__(self):
        return self.__str__()