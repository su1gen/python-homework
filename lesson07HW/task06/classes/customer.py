from lesson07HW.task06.classes.human import Human


class Customer(Human):
    def __init__(self, id, surname, name, patronymic, address, phone, credit_card, bank_account):
        super().__init__(id, surname, name, patronymic, address, phone)
        self.credit_card = credit_card
        self.bank_account = bank_account

    @property
    def credit_card(self):
        return self.__credit_card

    @credit_card.setter
    def credit_card(self, value):
        self.__credit_card = value

    @property
    def bank_account(self):
        return self.__bank_account

    @bank_account.setter
    def bank_account(self, value):
        self.__bank_account = value

    def __str__(self):
        return f'{Human.__str__(self)}, {self.__credit_card}, {self.__bank_account} '

    def to_dict(self):
        customer_dict = super().to_dict()
        customer_dict["credit_card"] = self.__credit_card
        customer_dict["bank_account"] = self.__bank_account
        return customer_dict
