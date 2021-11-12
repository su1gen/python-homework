from lesson07HW.task03.employee import Employee


class ShiftSupervisor(Employee):
    def __init__(self, name, number, year_salary, year_prize):
        super(ShiftSupervisor, self).__init__(name, number)
        self.year_salary = year_salary
        self.year_prize = year_prize

    @property
    def year_salary(self):
        return self.__year_salary

    @year_salary.setter
    def year_salary(self, value):
        self.__year_salary = value

    @property
    def year_prize(self):
        return self.__year_prize

    @year_prize.setter
    def year_prize(self, value):
        self.__year_prize = value

    def __str__(self):
        return f'{super().__str__()} {self.__year_salary} {self.__year_prize}'
