# Взгляните на приведенное ниже определение:
# class Beverage:
#     def init (self, bev_narne):
#         self. bev narne = bev narne
# Напишите программный код для класса с именем Cola (Кока-кола), который является
# подклассом класса Beverage (Напиток). Метод _ ini t _ () класса Cola должен вызывать
# метод ini t () класса Beverage, передавая строковое значение 'кока-кола' в качестве
# аргумента.

class Beverage:
    def __init__(self, bev_name):
        self.bev_name = bev_name


class Cola(Beverage):
    def __init__(self):
        super().__init__('coca-cola')


cola = Cola()

print(cola.bev_name)
