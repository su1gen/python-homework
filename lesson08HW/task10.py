# Переводчик с латинского. Взгляните на приведенный в табл. 13.12 список латинских
# слов и их значений.
# Напишите программу с GUI, которая переводит латинские слова на русский язык. Окно
# должно иметь три кнопки, по одной для каждого латинского слова (рис. 13.43). Когда
# пользователь нажимает кнопку, программа должна выводить на экран русский перевод
# в элемент интерфейса Label.


import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.button_frame = tkinter.Frame(self.main_window)
        self.button1 = tkinter.Button(self.button_frame, text='sinister', command=self.show_left)
        self.button2 = tkinter.Button(self.button_frame, text='dexter', command=self.show_right)
        self.button3 = tkinter.Button(self.button_frame, text='medium', command=self.show_middle)
        self.value = tkinter.StringVar()
        self.label = tkinter.Label(self.main_window, textvariable=self.value)

        self.label.pack()
        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button3.pack(side='left')
        self.button_frame.pack()



        tkinter.mainloop()

    def show_left(self):
        self.value.set('Левый')

    def show_right(self):
        self.value.set('Правый')

    def show_middle(self):
        self.value.set('Центральный')


my_gui = MyGUI()