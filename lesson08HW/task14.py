# Авторемонтная фирма "Автоцех". Авторемонтная фирма "Автоцех" предлагает услуги
# по регламентному техобслуживанию:
# • замена масла - 500.00 руб.;
# • смазочные работы - 300.00 руб.;
# • промывка радиатора- 700.00 руб.;
# • замена жидкости в трансмиссии - 1000.00 руб.;
# • осмотр - 800.00 руб.;
# • замена глушителя выхлопа- 1300.00 руб.;
# • перестановка шин - 1300.00 руб.
# Напишите программу с GUI с использованием флаговых кнопок, которые позволяют
# пользователю выбирать любые из этих видов услуг. При нажатии пользователем кнопки
# должна быть выведена общая стоимость услуг (рис. 13.47).

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.check_frame = tkinter.Frame(self.main_window)
        self.buttons_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        self.cb1 = tkinter.Checkbutton(self.check_frame, text='замена масла - 500.00 руб.', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.check_frame, text='смазочные работы - 300.00 руб.', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.check_frame, text='промывка радиатора- 700.00 руб.', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.check_frame, text='замена жидкости в трансмиссии - 1000.00 руб.', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.check_frame, text='осмотр - 800.00 руб.', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.check_frame, text='замена глушителя выхлопа- 1300.00 руб.', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.check_frame, text='перестановка шин - 1300.00 руб.', variable=self.cb_var7)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        self.calc_button = tkinter.Button(self.buttons_frame, text='Показать стоимость',
                                          command=self.calculate)
        self.exit_button = tkinter.Button(self.buttons_frame, text='Выйти', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.exit_button.pack(side='left')

        self.check_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()

    def calculate(self):

        amount = 0

        if self.cb_var1.get() == 1:
            amount += 500
        if self.cb_var2.get() == 1:
            amount += 300
        if self.cb_var3.get() == 1:
            amount += 700
        if self.cb_var4.get() == 1:
            amount += 1000
        if self.cb_var5.get() == 1:
            amount += 800
        if self.cb_var6.get() == 1:
            amount += 1300
        if self.cb_var7.get() == 1:
            amount += 1300

        tkinter.messagebox.showinfo('Ваши Затраты : ', amount)


my_gui = MyGUI()