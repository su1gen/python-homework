from lesson07HW.task06.classes.human import Human


class Student(Human):
    def __init__(self, id, surname, name, patronymic, address, phone, birthday, grades, faculty, course, group):
        super().__init__(id, surname, name, patronymic, address, phone)
        self.birthday = birthday
        self.grades = grades
        self.faculty = faculty
        self.course = course
        self.group = group

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        self.__birthday = value

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        self.__grades = value

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        self.__faculty = value

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        self.__course = value

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        self.__group = value

    def __str__(self):
        return f'{Human.__str__(self)}, {self.__birthday}, {self.__grades}, {self.__faculty}, {self.__course}, {self.__group} '

    def to_dict(self):
        student_dict = super().to_dict()
        student_dict["birthday"] = self.__birthday
        student_dict["grades"] = self.__grades
        student_dict["faculty"] = self.__faculty
        student_dict["course"] = self.__course
        student_dict["group"] = self.__group
        return student_dict
