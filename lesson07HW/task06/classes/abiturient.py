from lesson07HW.task06.classes.human import Human


class Abiturient(Human):
    def __init__(self, id, surname, name, patronymic, address, phone, grades):
        super().__init__(id, surname, name, patronymic, address, phone)
        self.grades = grades

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        self.__grades = value

    @property
    def grades_sum(self):
        return sum(self.__grades)

    def __str__(self):
        return f'{Human.__str__(self)}, {self.__grades} '

    def to_dict(self):
        abiturient_dict = super().to_dict()
        abiturient_dict["grades"] = self.__grades
        return abiturient_dict