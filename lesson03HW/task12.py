# Экзамен на получение водительских прав. Местный отдел по выдаче удостоверений на
# право вождения автомобиля попросил вас создать приложение, которое оценивает
# письменную часть экзамена на получение водительских прав. Экзамен состоит из 20 вопросов
# с множественным выбором. Вот правильные ответы:
# 1. А 6. в 11. А 16.С
# 2. с 7. с 12. D 17. в
# 3.А 8.А 13. с 18. в
# 4.А 9.С 14. А 19. D
# 5. D 10.В 15. D 20. А
# Ваша программа должна сохранить эти правильные ответы в списке. Программа должна
# прочитать из текстового файла ответы испытуемого на каждый из 20 вопросов и сохранить эти ответы в еще одном списке.
# (Создайте собственный текстовый файл для тестирования приложения
# или же воспользуйтесь файлом student_solution.txt, который можно
# найти в исходном коде главы 7 или в подпапке data "Решений задач по программированию" соответствующей главы.)
# После того как ответы испытуемого были считаны из
# файла, программа должна вывести сообщение о том, прошел ли испытуемый экзамен
# или нет. (Для того чтобы сдать экзамен, испытуемый должен правильно ответить на 15
# из 20 вопросов.) Затем программа должна вывести общее количество вопросов, ответы
# на которые были правильными, общее количество вопросов, ответы на которые были
# неправильными, и список, показывающий номера вопросов, ответы на которые были неправильными.

right_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

student_answers = []
right_answers_count = 0
wrong_answers_count = 0
wrong_answers_indexes = []

student_answers_file = open('student_solution.txt', 'r')

for item in student_answers_file:
    student_answers.append(item.rstrip('\n'))

student_answers_file.close()

for i in range(20):
    if right_answers[i] == student_answers[i]:
        right_answers_count += 1
    else:
        wrong_answers_count += 1
        wrong_answers_indexes.append(i + 1)

print(f'Right answers: {right_answers_count}')
print(f'Wrong answers: {wrong_answers_count}')        
print(f'Indexes of wrong answers: {wrong_answers_indexes}')