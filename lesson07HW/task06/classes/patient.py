from lesson07HW.task06.classes.human import Human


class Patient(Human):
    def __init__(self, id, surname, name, patronymic, address, phone, med_card, diagnose):
        super().__init__(id, surname, name, patronymic, address, phone)
        self.med_card = med_card
        self.diagnose = diagnose

    @property
    def med_card(self):
        return self.__med_card

    @med_card.setter
    def med_card(self, value):
        self.__med_card = value

    @property
    def diagnose(self):
        return self.__diagnose

    @diagnose.setter
    def diagnose(self, value):
        self.__diagnose = value

    def __str__(self):
        return f'{Human.__str__(self)}, {self.__med_card}, {self.__diagnose} '

    def to_dict(self):
        customer_dict = super().to_dict()
        customer_dict["med_card"] = self.__med_card
        customer_dict["diagnose"] = self.__diagnose
        return customer_dict