# Викторина. В этой задаче по программированию следует создать простую викторину для
# двух игроков. Программа будет работать следующим образом.
# • Начиная с игрока 1, каждый игрок по очереди отвечает на 5 вопросов викторины.
# (Должно быть в общей сложности 10 вопросов.) При выводе вопроса на экран также
# выводятся 4 возможных ответа. Только один из этих ответов является правильным,
# и если игрок выбирает правильный ответ, то он зарабатывает очко.
# • После того как были выбраны ответы на все вопросы, программа показывает количество очков,
# заработанное каждым игроком, и объявляет игрока с наибольшим количеством очков победителем.
# Для создания этой программы напишите класс Question (Вопрос), который будет содержать данные о вопросе викторины.
# Класс Question должен иметь атрибуты для приведенных ниже данных:
# • вопрос викторины;
# • возможный ответ 1;
# • возможный ответ 2;
# • возможный ответ 3;
# • возможный ответ 4;
# • номер правильного ответа ( 1, 2, 3 или 4 ).
# Класс Question также должен иметь соответствующий метод
# получатели и методы-модификаторы.
# ini t () , методыПрограмма должна содержать список или словарь с 10 объектами Question, один для
# каждого вопроса викторины. Составьте для объектов собственные вопросы викторины по
# теме или темам по вашему выбору.

from lesson06HW.task12.question import Question

if __name__ == '__main__':

    user1_answers = 0
    user2_answers = 0


    question_list = [
         Question('question1', 'answer1', 'answer2', 'answer3', 'answer4', 1),
         Question('question2', 'answer1', 'answer2', 'answer3', 'answer4', 1),
         Question('question3', 'answer1', 'answer2', 'answer3', 'answer4', 1),
         Question('question4', 'answer1', 'answer2', 'answer3', 'answer4', 1),
         Question('question5', 'answer1', 'answer2', 'answer3', 'answer4', 1),
         Question('question6', 'answer1', 'answer2', 'answer3', 'answer4', 1),
         Question('question7', 'answer1', 'answer2', 'answer3', 'answer4', 1),
         Question('question8', 'answer1', 'answer2', 'answer3', 'answer4', 1),
         Question('question9', 'answer1', 'answer2', 'answer3', 'answer4', 1),
         Question('question10', 'answer1', 'answer2', 'answer3', 'answer4', 1)
    ]

    question = 0

    while question < len(question_list):
        print('Question for user 1 ')
        print(question_list[question].get_question())
        print('Possible answers: ')
        print(f'1.{question_list[question].get_answer1()}')
        print(f'2.{question_list[question].get_answer2()}')
        print(f'3.{question_list[question].get_answer3()}')
        print(f'4.{question_list[question].get_answer4()}')

        answer = int(input('Enter number of answer '))

        if 0 > answer > 4:
            print('Incorrect answer')
        else:
            if answer == question_list[question].get_right_answer():
                user1_answers += 1

        question += 1

        print('Question for user 2 ')
        print(question_list[question].get_question())
        print('Possible answers: ')
        print(f'1.{question_list[question].get_answer1()}')
        print(f'2.{question_list[question].get_answer2()}')
        print(f'3.{question_list[question].get_answer3()}')
        print(f'4.{question_list[question].get_answer4()}')

        answer = int(input('Enter number of answer '))

        if 0 > answer > 4:
            print('Incorrect answer')
        else:
            if answer == question_list[question].get_right_answer():
                user2_answers += 1

        question += 1

    print(user1_answers, user2_answers)

    if user1_answers > user2_answers:
        print('User 1 wins')
    elif user1_answers < user2_answers:
        print('User 2 wins')
    else:
        print('Draw')




