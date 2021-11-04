class MouseEatController:
    def __init__(self, mouse):
        self.__mouse = mouse

    def eat(self, value):
        print("mouse eating ")
        self.__mouse.set_weight(self.__mouse.get_weight() + value)
        print(self.__mouse.get_weight())
