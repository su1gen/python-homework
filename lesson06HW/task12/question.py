class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, right_answer):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer3
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__right_answer = right_answer

    def get_question(self):
        return self.__question

    def set_question(self, value):
        self.__question = value

    def get_answer1(self):
        return self.__answer1

    def set_answer1(self, value):
        self.__answer1 = value

    def get_answer2(self):
        return self.__answer2

    def set_answer2(self, value):
        self.__answer2 = value

    def get_answer3(self):
        return self.__answer3

    def set_answer3(self, value):
        self.__answer3 = value

    def get_answer4(self):
        return self.__answer4

    def set_answer4(self, value):
        self.__answer4 = value

    def get_right_answer(self):
        return self.__right_answer

    def set_right_answer(self, value):
        self.__right_answer = value

