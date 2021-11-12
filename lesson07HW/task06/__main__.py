# Cоздать классы, спецификации которых приведены ниже.
# Определить конструкторы и методы(свойства) set(), get(), __str__().
# Определить дополнительно методы в классе, создающем массив объектов.
# Задать критерий выбора данных и вывести эти данные на консоль, прочитать и записать результат из файла
# В каждом классе, обладающем информацией, должно быть объявлено несколько конструкторов.
# 1. Student: id, ФИО, Дата рождения, Адрес, Телефон, Оценки (5) Факультет, Курс, Группа.
# Создать массив объектов. Вывести:
# a) список студентов заданного факультета;
# b) списки студентов для каждого факультета и курса;
# c) список студентов, родившихся после заданного года;
# d) список учебной группы средний бал выше 4.5 .
# 2. Customer: id, Фамилия, Имя, Отчество, Адрес, Телефон,  Номер кредитной карточки, Номер банковского счета.
# Создать массив объектов.
# Вывести:
# a) список покупателей в алфавитном порядке;
# b) список покупателей, у которых номер кредитной карточки находится в заданном интервале.
# 3. Patient: id, Фамилия, Имя, Отчество, Адрес, Телефон, Номер медицинской карты, Диагноз.
# Создать массив объектов.
# Вывести:
# a) список пациентов, имеющих данный диагноз;
# b) список пациентов, номер медицинской карты которых находится в заданном интервале.
# 4. Abiturient: id, Фамилия, Имя, Отчество, Адрес, Телефон, Оценки.
# Создать массив объектов.
# Вывести:
# a) список абитуриентов, имеющих неудовлетворительные оценки;
# b) список абитуриентов, у которых сумма баллов выше заданной;
# c) выбрать заданное число n абитуриентов, имеющих самую высокую сумму баллов
# (вывести также полный список абитуриентов, имеющих полупроходную сумму).
from lesson07HW.task06.classes.abiturient import Abiturient
from lesson07HW.task06.classes.abiturients_list import AbiturientsList
from lesson07HW.task06.classes.customer import Customer
from lesson07HW.task06.classes.customers_list import CustomersList
from lesson07HW.task06.classes.helpers import save_data_to_json, get_data_from_json
from lesson07HW.task06.classes.patient import Patient
from lesson07HW.task06.classes.patients_list import PatientsList
from lesson07HW.task06.classes.student import Student
from lesson07HW.task06.classes.students_list import StudentsList

if __name__ == '__main__':
    st1 = Student(1, 'Ivanov', 'Ivan', 'Ivanovich', 'adr1', 333, '01.01.2000', [1, 2, 3, 4, 5], 'fac1', 1, 1)
    st2 = Student(2, 'Ivanova', 'Julia', 'Ivanovna', 'adr2', 222, '01.01.1989', [5, 5, 5, 5, 5], 'fac2', 1, 1)
    st3 = Student(3, 'Ivanov', 'Ivan', 'Ivanovich', 'adr1', 333, '01.01.2000', [1, 2, 3, 4, 5], 'fac1', 1, 1)

    stud_list = StudentsList()

    stud_list.add(st1)
    stud_list.add(st2)
    stud_list.add(st3)

    print(stud_list.get_students_by_faculty('fac2'))
    print(stud_list.get_students_by_all_faculties())
    print(stud_list.get_students_bore_after_year(1990))
    print(stud_list.get_groups_by_average_grade(3))

    print(stud_list.get_students_dict())
    save_data_to_json('students.txt', stud_list.get_students_dict())

    stud_list2 = StudentsList()
    stud_list2.get_students_from_dict(get_data_from_json('students.txt'))
    print(stud_list2.get_students_by_all_faculties())
    print('-----------------------------------------')

    cust1 = Customer(1, 'Ivanov2', 'Ivan2', 'Ivanovich2', 'adr1', 333, 1, 111111)
    cust2 = Customer(2, 'Avanova2', 'Julia2', 'Ivanovna2', 'adr2', 222, 2, 2222222)
    cust3 = Customer(3, 'Ovanov2', 'Ivan2', 'Ivanovich2', 'adr1', 333, 3, 333333)

    cust_list = CustomersList()

    cust_list.add(cust1)
    cust_list.add(cust2)
    cust_list.add(cust3)

    print(cust_list.get_sorted_customers_by_surname())
    print(cust_list.get_customers_in_credit_card_range(1, 2))

    save_data_to_json('customers.txt', cust_list.get_customers_dict())

    cust_list2 = CustomersList()
    cust_list2.get_customers_from_dict(get_data_from_json('customers.txt'))
    print(cust_list2.get_customers_in_credit_card_range(1, 3))
    print('-----------------------------------------')

    pat1 = Patient(1, 'Ivanov3', 'Ivan3', 'Ivanovich3', 'adr1', 333, 1, 'good')
    pat2 = Patient(2, 'Avanova3', 'Julia3', 'Ivanovna3', 'adr2', 222, 2, 'good')
    pat3 = Patient(3, 'Ovanov3', 'Ivan3', 'Ivanovich3', 'adr1', 333, 3, 'bad')

    pat_list = PatientsList()

    pat_list.add(pat1)
    pat_list.add(pat2)
    pat_list.add(pat3)

    print(pat_list.get_patients_by_diagnose('bad'))
    print(pat_list.get_patients_in_med_card_range(1, 2))

    save_data_to_json('patients.txt', pat_list.get_patients_dict())

    pat_list2 = PatientsList()
    pat_list2.get_patients_from_dict(get_data_from_json('patients.txt'))
    print(pat_list2.get_patients_in_med_card_range(1, 3))
    print('-----------------------------------------')

    ab1 = Abiturient(1, 'Ivanov4', 'Ivan4', 'Ivanovich3', 'adr1', 333, [1,2,3,4,5])
    ab2 = Abiturient(2, 'Avanova4', 'Julia4', 'Ivanovna3', 'adr2', 222, [5,5,5,5,5])
    ab3 = Abiturient(3, 'Ovanov4', 'Ivan4', 'Ivanovich3', 'adr1', 333, [1,2,3,4,5])

    ab_list = AbiturientsList()

    ab_list.add(ab1)
    ab_list.add(ab2)
    ab_list.add(ab3)

    print(ab_list.get_abiturients_with_negative_grades())
    print(ab_list.get_abiturients_with_grades_sum(20))
    print(ab_list.get_sorted_abiturients_by_grades())

    save_data_to_json('abiturients.txt', ab_list.get_abiturients_dict())

    ab_list2 = AbiturientsList()
    ab_list2.get_abiturients_from_dict(get_data_from_json('abiturients.txt'))
    print(ab_list2.get_sorted_abiturients_by_grades())


