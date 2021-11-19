# Допустим, что self. labell и self. label2 ссылаются на два элемента интерфейса Label.
# Напишите фрагмент кода, который упаковывает эти два элемента таким образом, чтобы
# они были расположены в своем родительском элементе интерфейса максимально слева.

import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window,
                                   text=' Программировать - это круто! ')
        self.label2 = tkinter.Label(self.main_window,
                                   text=' Программировать - это круто! ')
        self.label1.pack(side='left')
        self.label2.pack(side='left')

        tkinter.mainloop()


my_gui = MyGUI()