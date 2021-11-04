from lesson06HW.task13.model.animals.classes import Mouse


class GrandmaController:
    def __init__(self, grandma):
        self.grandma = grandma

    def feed_cat(self, cat1):
        m1 = Mouse("Jerry1", 0.35)
        cat1.eat_mouse(m1)
        m2 = Mouse("Jerry2", 0.35)
        cat1.eat_mouse(m2)
        for i in range(0,30):
            cat1.eat_mouse(Mouse("BigJerry"+str(i), 0.5))