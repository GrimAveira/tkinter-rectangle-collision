import re
import tkinter as tk


class RectangleCollision:
    def __init__(self, width=800, height=300):

        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("Rectangle Collision")

        self.errmsg = tk.StringVar()

        error_label = tk.Label(
            foreground="red", textvariable=self.errmsg, wraplength=250)
        error_label.grid(
            column=0, row=5, columnspan=4, padx=10, pady=10)

        self.rec1_mass_label = tk.Label(
            text="Масса объекта слева", font='Calibri 11')
        self.rec1_mass_label.grid(column=0, row=0)
        self.rec1_mass_entry = tk.Entry(width=20)
        self.rec1_mass_entry.grid(column=0, row=1)

        self.rec2_mass_label = tk.Label(
            text="Масса объекта справа", font='Calibri 11')
        self.rec2_mass_label.grid(column=1, row=0)
        self.rec2_mass_entry = tk.Entry(width=20)
        self.rec2_mass_entry.grid(column=1, row=1)

        self.rec1_velocity_label = tk.Label(
            text="Скорость объекта слева", font='Calibri 11')
        self.rec1_velocity_label.grid(column=2, row=0)
        self.rec1_velocity_entry = tk.Entry(width=20)
        self.rec1_velocity_entry.grid(column=2, row=1)

        self.rec2_velocity_label = tk.Label(
            text="Скорость объекта справа", font='Calibri 11')
        self.rec2_velocity_label.grid(column=3, row=0)
        self.rec2_velocity_entry = tk.Entry(width=20)
        self.rec2_velocity_entry.grid(column=3, row=1)

        self._acceptButton = tk.Button(
            self.root, text="Применить данные и запустить коллизию", command=self.button_create_handler, font='Calibri 12', borderwidth="2", relief="solid")
        self._acceptButton.grid(
            column=0, row=4, columnspan=4, padx=10, pady=10)

        self.canvas = tk.Canvas(
            self.root, width=self.width, height=self.height, bg="white")
        self.canvas.grid(column=0, row=6, columnspan=4)
        self.rectangles = []

        self.main_menu = tk.Menu()
        self.main_menu.add_cascade(label="File")
        self.main_menu.add_cascade(label="Edit")
        self.main_menu.add_cascade(label="View")

        self.root.config(menu=self.main_menu)

        self.root.bind('<Escape>', self.close_app)

    def button_create_handler(self):
        mass1 = self.rec1_mass_entry.get()
        mass2 = self.rec1_mass_entry.get()
        vel1 = self.rec1_velocity_entry.get()
        vel2 = self.rec2_velocity_entry.get()
        if (self.entry_input_validate(mass1) and self.entry_input_validate(mass2) and self.entry_input_validate(vel1) and self.entry_input_validate(vel2)):
            self.rectangles = []
            self.create_rectangle(150, 100, 200, 150, int(mass1), [
                int(vel1)/100, 0], "aqua")
            self.create_rectangle(600, 100, 650, 150, int(mass2), [
                -int(vel2)/100, 0], "black")
            self.start_collision()

    def entry_input_validate(self, input_value):
        result = re.match("^[1-9]{1}$", input_value) is not None
        if not result and len(input_value) <= 12:
            self.errmsg.set(
                "Каждое поле для ввода должно быть заполнено цифрой от 1 до 9")
        else:
            self.errmsg.set("")
        return result

    def create_rectangle(self, x1, y1, x2, y2, mass, velocity, color):
        rectangle = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2,
                     'mass': mass, 'velocity': velocity, 'color': color}
        self.rectangles.append(rectangle)

    def update_rectangles(self):
        for rectangle in self.rectangles:
            rectangle['x1'] += rectangle['velocity'][0]
            rectangle['y1'] += rectangle['velocity'][1]
            rectangle['x2'] += rectangle['velocity'][0]
            rectangle['y2'] += rectangle['velocity'][1]
            if rectangle['x1'] < 0 or rectangle['x2'] > self.width:
                rectangle['velocity'][0] *= -1
            if rectangle['y1'] < 0 or rectangle['y2'] > self.height:
                rectangle['velocity'][1] *= -1

    def check_collisions(self):
        for i in range(len(self.rectangles)):
            for j in range(i + 1, len(self.rectangles)):
                rect1 = self.rectangles[i]
                rect2 = self.rectangles[j]
                if rect1['x1'] < rect2['x2'] and rect1['x2'] > rect2['x1'] and rect1['y1'] < rect2['y2'] and rect1['y2'] > rect2['y1']:
                    v1 = ((rect1['mass'] - rect2['mass']) * rect1['velocity'][0] + 2 *
                          rect2['mass'] * rect2['velocity'][0]) / (rect1['mass'] + rect2['mass'])
                    v2 = ((rect2['mass'] - rect1['mass']) * rect2['velocity'][0] + 2 *
                          rect1['mass'] * rect1['velocity'][0]) / (rect1['mass'] + rect2['mass'])
                    rect1['velocity'][0] = v1
                    rect2['velocity'][0] = v2

    def draw_rectangles(self):
        self.canvas.delete("all")
        for rectangle in self.rectangles:
            self.canvas.create_rectangle(
                rectangle['x1'], rectangle['y1'], rectangle['x2'], rectangle['y2'], fill=rectangle['color'], tags="4")
        self.canvas.update()

    def start_collision(self):
        while True:
            self.update_rectangles()
            self.check_collisions()
            self.draw_rectangles()

    def start_app(self):
        self.root.mainloop()

    def close_app(self, _):
        """Destroy tkinter application.

        Keyword arguments:
        self -- the mandatory default argument (default self)

        """
        self.root.destroy()
