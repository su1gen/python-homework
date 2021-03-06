# Допустим, что в программе приведенная ниже инструкция создает элемент интерфейса
# Canvas и присваивает его переменной self. canvas:
# self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
# Напишите инструкции, которые делают следующее:
# • чертят синюю прямую из левого верхнего угла элемента Canvas в его правый нижний
# угол, прямая должна быть шириной 3 пиксела;
# • чертят прямоугольник с красным контуром и черным заполнением, углы прямоугольника
# должны располагаться на холсте в приведенных ниже позициях:
# 0 левый верхний: (50, 50);
# 0 правый верхний: (100, 50);
# 0 левый нижний: (50, 100);
# 0 правый нижний: (100, 100);
# • чертят зеленый круг, центральная точка круга должна быть в координатах (100, 100),
# а ее радиус должен равняться 50;
# • чертят заполненную синим цветом дугу, заданную ограничивающим прямоугольником,
# чей левый верхний угол находится в координатах (20, 20), правый нижний
# угол - в координатах (180, 180). Дуга должна начинаться в 0° и простираться на 90°.


import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
        self.canvas.create_line(0, 0, 200, 200, fill='blue', width='3')
        self.canvas.create_rectangle(50, 50, 100, 100, outline='red', fill='black')
        self.canvas.create_oval(75, 75, 125, 125, fill='green')
        self.canvas.create_arc(20, 20, 180, 180, start=0, extent=90, fill='blue')

        self.canvas.pack()
        tkinter.mainloop()


my_gui = MyGUI()