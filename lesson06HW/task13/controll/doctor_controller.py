from lesson06HW.task13.model.animals.classes import Cat
from lesson06HW.task13.model.medic.doctor import Doctor
from lesson06HW.task13.view.display import DisplayToConsole


class DoctorController:

    def __init__(self, doctor: Doctor):
        self.doctor = doctor
        self.display = DisplayToConsole()

    def diagnose(self, cat: Cat):
        self.display.show("doctor name", self.doctor.get_name())
        self.display.show("is_alife :", cat.is_alife())
        self.display.show("name :", cat.get_name())
        self.display.show("age :", cat.get_age())
        self.display.show("weight :", cat.get_weight())
        self.display.show("weight :", cat.get_mousses())