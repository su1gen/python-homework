import tkinter
import tkinter.messagebox

from lesson09HW.classes.connection_to_db import ConnectionToDB
from lesson09HW.classes.satellite import Satellite
from lesson09HW.controllers.planet_controller import PlanetController
from lesson09HW.controllers.satellite_controller import SatelliteController


class SatelliteWindow(tkinter.Toplevel):
    def __init__(self):
        self.satellite_window = tkinter.Tk()
        self.satellite_window.title("Satellite window")

        screen_width = self.satellite_window.winfo_screenwidth()
        screen_height = self.satellite_window.winfo_screenheight()
        position_x = int((screen_width - 500) / 2)
        position_y = int((screen_height - 500) / 2)

        self.satellite_window.geometry(f"500x500+{position_x}+{position_y + 200}")

        self.name_frame = tkinter.Frame(self.satellite_window)
        self.distance_frame = tkinter.Frame(self.satellite_window)
        self.planet_frame = tkinter.Frame(self.satellite_window)

        self.name_label = tkinter.Label(self.name_frame, text='Введите название спутника: ')
        self.name_entry = tkinter.Entry(self.name_frame, width=30)
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.distance_label = tkinter.Label(self.distance_frame, text='Введите расстояние до планеты: ')
        self.distance_entry = tkinter.Entry(self.distance_frame, width=30)
        self.distance_label.pack(side='left')
        self.distance_entry.pack(side='left')

        self.planet_label = tkinter.Label(self.planet_frame, text='Выберите планету: ')
        self.planet_listbox = tkinter.Listbox(self.planet_frame, width=30)
        self.planet_label.pack(side='left')
        self.planet_listbox.pack(side='left')

        self.planets = self.get_planets()

        for item in self.planets:
            self.planet_listbox.insert(tkinter.END, item.name)

        self.save_button = tkinter.Button(self.satellite_window, text='Добавить',
                                          command=self.save_satellite)
        self.name_frame.pack(pady=10)
        self.distance_frame.pack(pady=10)
        self.planet_frame.pack(pady=10)
        self.save_button.pack()

        self.satellite_window.mainloop()

    def get_planets(self):
        planet_controller = PlanetController()
        planets = planet_controller.get_planets()
        return planets

    def save_satellite(self):
        if len(self.planet_listbox.curselection()) == 0:
            tkinter.messagebox.showinfo('Внимание', 'Нужно выбрать планету!')
        else:
            new_satellite = Satellite(self.name_entry.get(), self.distance_entry.get(),
                                self.planets[self.planet_listbox.curselection()[0]].id)

            satellite_controller = SatelliteController()
            satellite_controller.add_satellite(new_satellite)

            tkinter.messagebox.showinfo('Внимание', 'Спутник успешно сохранен!')



if __name__ == '__main__':
    my_win = SatelliteWindow()
