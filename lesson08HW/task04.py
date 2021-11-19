# Напишите инструкцию, которая выводит на экран информационное диалоговое окно с заголовком "Программа приостановлена"
# и сообщением "Нажмите ОК, когда будете готовы продолжить".

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.button = tkinter.Button(self.main_window, text='button', command=self.show)

        self.button.pack()

        tkinter.mainloop()

    def show(self):
        tkinter.messagebox.showinfo('Программа приостановлена', 'Нажмите ОК, когда будете готовы продолжить')


my_gui = MyGUI()