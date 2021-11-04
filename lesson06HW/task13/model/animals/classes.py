class Cat:
    def __init__(self, name="Anonim", age=0, weight=0):
        self.__weight = weight
        self.__age = age
        self.__name = name
        self.__mousses = list()

    def add_mouse_to_eaten(self, mouse):
        self.__mousses.append(mouse)

    def get_mousses(self):
        return self.__mousses
    def get_weight(self):
        return self.__weight
    def set_weight(self, value):
        self.__weight = value

    def get_name(self):
        return self.__name
    def set_name(self, value):
        if str(value).isalpha():
            self.__name = value
        else:
            raise ValueError("Error name")

    def get_age(self):
        return self.__age
    def set_age(self, value):
        if value in range(1,20):
            self.__age = value
        else:
            raise ValueError("Error age")

    def eat_mouse(self, mouse):
        print("eating mouse", mouse.get_name())
        self.eat(mouse.get_weight())
        mouse.set_weight(0)
        self.__mousses.append(mouse)
        mouse.killer = self
   #     self.__weight+=mouse.get_weight()

    def eat(self, food):
        print("eating food", food)
        if not self.is_alife():
            raise OverflowError("Dead cat can't eat")
        if 0< food < self.__weight:
            self.__weight+=food
        else:
            print("Error food")
        self.validate_weight()

    def validate_weight(self):
        if self.__weight > 20:
            self.__weight = 0
            print("....fat cat - > dead cat... game over")

    def is_alife(self):
        return self.__weight > 0

    def print_info(self):
        self.print_str_info()
        print("Eating mouse:")
        for mouse in self.__mousses:
            print(mouse.get_name())

    def print_str_info(self):
        print("Cat: ",self.get_name(), self.get_age(), self.get_weight())

    def print_self_info(self):
        print("Cat: ",self.__name, self.__age, self.__weight)


class Mouse:
    def __init__(self, name="Anonim", weight=0):
        self.__weight = weight
        self.__name = name
        self.killer = None

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        self.__weight = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        if str(value).isalpha():
            self.__name = value
        else:
            raise ValueError("Error name")
    def is_alife(self):
        return self.__weight > 0
    def print_info(self):
        if self.is_alife():
            print("Mouse: ",self.__name,  self.__weight)
        else:
            print("... RIP... Mouse: ",self.__name, " kill by", self.killer.get_name())