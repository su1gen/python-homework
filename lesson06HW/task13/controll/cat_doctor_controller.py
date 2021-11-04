class CatDoctorController:
    def __init__(self, cat, doctor):
        self.__cat = cat
        self.__doctor = doctor

    def diag_weight(self):
        return  self.__cat.get_weight()