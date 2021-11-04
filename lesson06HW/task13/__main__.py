from lesson06HW.task13.controll.cat_doctor_controller import CatDoctorController
from lesson06HW.task13.controll.cat_eat_controller import CatEatController
from lesson06HW.task13.controll.doctor_controller import DoctorController
from lesson06HW.task13.controll.grandma_controller import GrandmaController
from lesson06HW.task13.controll.mouse_eat_controller import MouseEatController
from lesson06HW.task13.model.animals.classes import Cat, Mouse
from lesson06HW.task13.model.keppers.grandma import Grandma
from lesson06HW.task13.model.medic.doctor import Doctor


def test_class_cat():
    cat1 = Cat("Tom", 5, 7)
    cat1.print_info()
    cat1.eat(10.5)
    cat1.set_name("abc567")
    cat1.print_info()
    m1 = Mouse("Jerry", 0.35)
    cat1.eat(m1.get_weight())
    cat1.print_info()
    m1.print_info()
    cat2 = Cat(name="Bob", age=10, weight=11)
    cat2.print_info()
    cat3 = Cat()
    cat3.print_info()
    cat4 = Cat(name="Alice", age=1)
    cat4.print_info()


if __name__ == '__main__':
    # cat1 = Cat("Tom", 5, 7)
    # while(True):
    #     print("1. Grandma")
    #     print("2. Doctor")
    #     choise = input("enter choice")
    #     if choise == "1":
    #         try:
    #             cat1.print_info()
    #             grandma_controll = GrandmaController(Grandma("GrandBa"))
    #             grandma_controll.feed_cat(cat1)
    #             cat1.print_info()
    #
    #         except Exception as e:
    #             print(e)
    #     elif choise == "2":
    #         doc_controll = DoctorController(Doctor("AyBolit"))
    #         doc_controll.diagnose(cat1)
    #     else:
    #         print("Exit")
    #         break
    cat1 = Cat("Tom", 5, 7)
    m1 = Mouse("Jerry", 0.35)
    mouse_eat_controller = MouseEatController(m1)
    mouse_eat_controller.eat(0.2)

    doc = Doctor('Ivan')

    cat_doctor_controller = CatDoctorController(cat1, doc)
    print(cat_doctor_controller.diag_weight())

    cat_eat_controller = CatEatController(cat1)
    cat_eat_controller.eat_from_file('controll/food.txt')