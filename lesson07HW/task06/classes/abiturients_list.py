from lesson07HW.task06.classes.abiturient import Abiturient
import operator


class AbiturientsList:
    def __init__(self):
        self.__abiturients = list()

    def add(self, abiturient):
        self.__abiturients.append(abiturient)

    def get_abiturients_with_negative_grades(self):
        return [abiturient.__str__() for abiturient in self.__abiturients if len(set(abiturient.grades).intersection({1, 2})) > 0]

    def get_abiturients_with_grades_sum(self, summa):
        return [abiturient.__str__() for abiturient in self.__abiturients if sum(abiturient.grades) >= summa]

    def get_sorted_abiturients_by_grades(self, length=None):
        sorted_abiturients = sorted(self.__abiturients, key=operator.attrgetter('grades_sum'))
        abiturients_list = [customer.__str__() for customer in sorted_abiturients]

        if length:
            return abiturients_list[:length]

        return abiturients_list





    def get_abiturients_dict(self):
        return [abiturient.to_dict() for abiturient in self.__abiturients]

    def get_abiturients_from_dict(self, data):
        for abiturient in data:
            self.__abiturients.append(
                Abiturient(abiturient['id'], abiturient['surname'], abiturient['name'], abiturient['patronymic'],
                         abiturient['address'], abiturient['phone'], abiturient['grades']))