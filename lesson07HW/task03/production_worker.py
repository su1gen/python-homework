from lesson07HW.task03.employee import Employee


class ProductionWorker(Employee):
    def __init__(self, name, number, shift, salary):
        super().__init__(name, number)
        self.shift = shift
        self.salary = salary


    @property
    def shift(self):
        return self.__shift

    @shift.setter
    def shift(self, value):
        self.__shift = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def __str__(self):
        return f'{super().__str__()} {self.__shift} {self.__salary}'
