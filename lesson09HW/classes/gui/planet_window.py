import tkinter
import tkinter.messagebox

from lesson09HW.classes.connection_to_db import ConnectionToDB
from lesson09HW.classes.planet import Planet
from lesson09HW.controllers.galaxy_controller import GalaxyController
from lesson09HW.controllers.planet_controller import PlanetController


class PlanetWindow(tkinter.Toplevel):
    def __init__(self):
        self.planet_window = tkinter.Tk()
        self.planet_window.title("Planet window")

        screen_width = self.planet_window.winfo_screenwidth()
        screen_height = self.planet_window.winfo_screenheight()
        position_x = int((screen_width - 500) / 2)
        position_y = int((screen_height - 500) / 2)

        self.planet_window.geometry(f"500x500+{position_x}+{position_y + 200}")

        self.name_frame = tkinter.Frame(self.planet_window)
        self.radius_frame = tkinter.Frame(self.planet_window)
        self.core_frame = tkinter.Frame(self.planet_window)
        self.atmosphere_frame = tkinter.Frame(self.planet_window)
        self.life_frame = tkinter.Frame(self.planet_window)
        self.galaxy_frame = tkinter.Frame(self.planet_window)

        self.name_label = tkinter.Label(self.name_frame, text='Введите название планеты: ')
        self.name_entry = tkinter.Entry(self.name_frame, width=30)
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.radius_label = tkinter.Label(self.radius_frame, text='Введите радиус планеты: ')
        self.radius_entry = tkinter.Entry(self.radius_frame, width=30)
        self.radius_label.pack(side='left')
        self.radius_entry.pack(side='left')

        self.core_label = tkinter.Label(self.core_frame, text='Введите тепературу ядра планеты: ')
        self.core_entry = tkinter.Entry(self.core_frame, width=30)
        self.core_label.pack(side='left')
        self.core_entry.pack(side='left')

        self.atmosphere_var = tkinter.IntVar()
        self.atmosphere_var.set(0)
        self.atmosphere_cb = tkinter.Checkbutton(self.atmosphere_frame, text='Есть ли атмосфера', variable=self.atmosphere_var)
        self.atmosphere_cb.pack()

        self.life_var = tkinter.IntVar()
        self.life_var.set(0)
        self.life_cb = tkinter.Checkbutton(self.life_frame, text='Есть ли жизнь', variable=self.life_var)
        self.life_cb.pack()

        self.galaxy_label = tkinter.Label(self.galaxy_frame, text='Выберите галактику: ')
        self.galaxy_listbox = tkinter.Listbox(self.galaxy_frame, width=30)
        self.galaxy_label.pack(side='left')
        self.galaxy_listbox.pack(side='left')

        self.galaxies = self.get_galaxies()

        for item in self.galaxies:
            self.galaxy_listbox.insert(tkinter.END, item.name)



        self.save_button = tkinter.Button(self.planet_window, text='Добавить',
                                          command=self.save_planet)
        self.name_frame.pack(pady=10)
        self.radius_frame.pack(pady=10)
        self.core_frame.pack(pady=10)
        self.atmosphere_frame.pack(pady=10)
        self.life_frame.pack(pady=10)
        self.galaxy_frame.pack(pady=10)
        self.save_button.pack()

        self.planet_window.mainloop()

    def get_galaxies(self):
        galaxy_controller = GalaxyController()
        galaxies = galaxy_controller.get_galaxies()
        return galaxies

    def save_planet(self):
        if len(self.galaxy_listbox.curselection()) == 0:
            tkinter.messagebox.showinfo('Внимание', 'Нужно выбрать галактику!')
        else:

            new_planet = Planet(self.name_entry.get(), self.radius_entry.get(), self.core_entry.get(),
                                self.atmosphere_var.get(), self.life_var.get(),
                                self.galaxies[self.galaxy_listbox.curselection()[0]].id)

            planet_controller = PlanetController()
            planet_controller.add_planet(new_planet)

            tkinter.messagebox.showinfo('Внимание', 'Планета успешно сохранена!')



if __name__ == '__main__':
    my_win = PlanetWindow()
