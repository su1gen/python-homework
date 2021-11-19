# Напишите инструкцию, которая создает элемент интерфейса Frame. Его родительским
# элементом должен быть элемент self .main _ window.


import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame(self.main_window)

        self.frame.pack(side='left')

        tkinter.mainloop()


my_gui = MyGUI()