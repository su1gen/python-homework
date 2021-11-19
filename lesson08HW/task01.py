# Напишите инструкцию, которая создает элемент интерфейса Label. Его родительским
# элементом должен быть элемент self .main _ window, и он должен содержать текст
# 'Программировать - это круто! '.

import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window,
                                   text=' Программировать - это круто! ')
        self.label.pack()

        tkinter.mainloop()


my_gui = MyGUI()
