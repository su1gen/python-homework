class Planet:
    def __init__(self, name, radius, core_temperature, has_atmosphere, has_life, galaxy_id, id=None):
        self.id = id
        self.name = name
        self.radius = radius
        self.core_temperature = core_temperature
        self.has_atmosphere = has_atmosphere
        self.has_life = has_life
        self.galaxy_id = galaxy_id


    def __str__(self):
        return f'Planet: {self.name}, {self.radius}, {self.core_temperature}, {self.has_atmosphere}, {self.has_life}, {self.galaxy_id}'

    def __repr__(self):
        return self.__str__()