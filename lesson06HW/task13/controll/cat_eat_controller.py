class CatEatController:
    def __init__(self, cat):
        self.__cat = cat

    def eat_from_file(self, filename):
        with open(filename, 'r', encoding='utf8') as file:
            value = float(file.read())
        self.__cat.eat_cost(value)
