from lesson07HW.task06.classes.student import Student


class StudentsList:
    def __init__(self):
        self.__students = list()

    def add(self, student):
        self.__students.append(student)

    def get_students_by_faculty(self, faculty):
        students_list = list()
        for student in self.__students:
            if student.faculty == faculty:
                students_list.append(f'{student.surname} {student.name} {student.patronymic}')
        return students_list

    def get_students_by_all_faculties(self):
        students_list = dict()
        for student in self.__students:
            if student.faculty in students_list:
                students_list[student.faculty].append(f'{student.surname} {student.name} {student.patronymic}')
            else:
                students_list[student.faculty] = [f'{student.surname} {student.name} {student.patronymic}']
        return students_list

    def get_students_bore_after_year(self, year):
        students_list = list()
        for student in self.__students:
            if int(student.birthday.split('.')[2]) >= year:
                students_list.append(f'{student.surname} {student.name} {student.patronymic}')
        return students_list

    def get_groups_by_average_grade(self, grade):
        groups_list = dict()
        groups_with_average_grade = list()
        for student in self.__students:
            if student.group in groups_list:
                groups_list[student.group] += student.grades
            else:
                groups_list[student.faculty] = student.grades

        for group, grades in groups_list.items():
            average_grade = round(sum(grades) / len(grades), 1)
            if average_grade >= grade:
                groups_with_average_grade.append(group)

        return groups_with_average_grade

    def get_students_dict(self):
        return [student.to_dict() for student in self.__students]

    def get_students_from_dict(self, data):
        for student in data:
            self.__students.append(
                Student(student['id'], student['surname'], student['name'], student['patronymic'], student['address'],
                        student['phone'], student['birthday'], student['grades'], student['faculty'], student['course'],
                        student['group']))
