import re
from tkinter import Tk, Label, StringVar, Button, Canvas, Menu, Entry, messagebox


class RectangleCollision:
    def __init__(self, width=800, height=300):

        # window options
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.geometry(f"{self.__width}x{self.__height}")
        self.__root.title("Rectangle Collision")
        self.__root.option_add("*tearOff", False)

        # error label
        self.__errmsg = StringVar()
        self.__error__label = Label(
            foreground="red", textvariable=self.__errmsg, wraplength=250, font='Calibri 11')
        self.__error__label.grid(column=0, row=5, columnspan=4)

        # labels and entry for mass and velocity
        self.__rec1_mass_label = Label(
            text="Mass of the left object", font='Calibri 11')
        self.__rec1_mass_label.grid(column=0, row=0)
        self.__rec1_mass_entry = Entry(width=20)
        self.__rec1_mass_entry.grid(column=0, row=1)

        self.__rec2_mass_label = Label(
            text="Mass of the right object", font='Calibri 11')
        self.__rec2_mass_label.grid(column=1, row=0)
        self.__rec2_mass_entry = Entry(width=20)
        self.__rec2_mass_entry.grid(column=1, row=1)

        self.__rec1_velocity_label = Label(
            text="Velocity of the left object", font='Calibri 11')
        self.__rec1_velocity_label.grid(column=2, row=0)
        self.__rec1_velocity_entry = Entry(width=20)
        self.__rec1_velocity_entry.grid(column=2, row=1)

        self.__rec2_velocity_label = Label(
            text="Velocity of the right object", font='Calibri 11')
        self.__rec2_velocity_label.grid(column=3, row=0)
        self.__rec2_velocity_entry = Entry(width=20)
        self.__rec2_velocity_entry.grid(column=3, row=1)

        # button for start action
        self.__acceptButton = Button(
            self.__root, text="Accept data and start collision", command=self.__button_create_handler, font='Calibri 12', borderwidth="2", relief="solid")
        self.__acceptButton.grid(
            column=0, row=4, columnspan=4, padx=10, pady=10)

        # canvas for drawing
        self.__canvas = Canvas(
            self.__root, width=self.__width, height=self.__height, bg="white")
        self.__canvas.grid(column=0, row=6, columnspan=4)
        self.__rectangles = []

        # menu header
        self.__main_menu = Menu(self.__root)
        self.__main_menu.add_command(label="About", command=self.__about)
        self.__main_menu.add_command(label="Version", command=self.__version)

        self.__root.config(menu=self.__main_menu)

        # bind for close app
        self.__root.bind('<Escape>', self.__close_app)

    def __about(self):
        """Show info about app.
        """

        messagebox.showinfo(
            "About", "A Python application with tkinter that allows you to look at the collision of two rectangular bodies at a given mass and velocity")

    def __version(self):
        """Show info about version app.
        """

        messagebox.showinfo("Version", "v0.0.1")

    def __button_create_handler(self):
        """Accept entry data and start the collision.
        """

        mass1 = self.__rec1_mass_entry.get()
        mass2 = self.__rec1_mass_entry.get()
        vel1 = self.__rec1_velocity_entry.get()
        vel2 = self.__rec2_velocity_entry.get()
        if (self._entry_input_validate(mass1) and self._entry_input_validate(mass2) and self._entry_input_validate(vel1) and self._entry_input_validate(vel2)):
            self.__rectangles = []
            self.__create_rectangle(150, 100, 200, 150, int(mass1), [
                int(vel1)/100, 0], "aqua")
            self.__create_rectangle(600, 100, 650, 150, int(mass2), [
                -int(vel2)/100, 0], "black")
            self.__start_collision()

    def _entry_input_validate(self, input_value):
        """Destroy tkinter application.

        Keyword arguments:
        input_value:str -- the entry argument of the field to be validated

        """

        result = re.match("^[1-9]{1}$", input_value) is not None
        if not result and len(input_value) <= 12:
            self.__errmsg.set(
                "Each input field must be filled with a number from 1 to 9")
        else:
            self.__errmsg.set("")
        return result

    def __create_rectangle(self, x1, y1, x2, y2, mass, velocity, color):
        """Creates objects that will interact with each other.

        Keyword arguments:
        x1:int -- the coordinate for the initial rendering of the object
        y1:int -- the coordinate for the initial rendering of the object
        x2:int -- the coordinate for the initial rendering of the object
        y2:int -- the coordinate for the initial rendering of the object
        mass:int -- reflects the mass of the object
        velocity:int -- reflects the velocity of the object
        color:str -- reflects the color of the object

        """

        rectangle = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2,
                     'mass': mass, 'velocity': velocity, 'color': color}
        self.__rectangles.append(rectangle)

    def __update_rectangles(self):
        """Changes the coordinates of objects depending on the speed.
        """

        for rectangle in self.__rectangles:
            rectangle['x1'] += rectangle['velocity'][0]
            rectangle['y1'] += rectangle['velocity'][1]
            rectangle['x2'] += rectangle['velocity'][0]
            rectangle['y2'] += rectangle['velocity'][1]
            if rectangle['x1'] < 0 or rectangle['x2'] > self.__width:
                rectangle['velocity'][0] *= -1
            if rectangle['y1'] < 0 or rectangle['y2'] > self.__height:
                rectangle['velocity'][1] *= -1

    def __check_collisions(self):
        """Calculates the collision velocity.
        """

        for i in range(len(self.__rectangles)):
            for j in range(i + 1, len(self.__rectangles)):
                rect1 = self.__rectangles[i]
                rect2 = self.__rectangles[j]
                if rect1['x1'] < rect2['x2'] and rect1['x2'] > rect2['x1'] and rect1['y1'] < rect2['y2'] and rect1['y2'] > rect2['y1']:
                    v1 = ((rect1['mass'] - rect2['mass']) * rect1['velocity'][0] + 2 *
                          rect2['mass'] * rect2['velocity'][0]) / (rect1['mass'] + rect2['mass'])
                    v2 = ((rect2['mass'] - rect1['mass']) * rect2['velocity'][0] + 2 *
                          rect1['mass'] * rect1['velocity'][0]) / (rect1['mass'] + rect2['mass'])
                    rect1['velocity'][0] = v1
                    rect2['velocity'][0] = v2

    def __draw_rectangles(self):
        """Draws objects by coordinates.
        """

        self.__canvas.delete("all")
        for rectangle in self.__rectangles:
            self.__canvas.create_rectangle(
                rectangle['x1'], rectangle['y1'], rectangle['x2'], rectangle['y2'], fill=rectangle['color'], tags="4")
        self.__canvas.update()

    def __start_collision(self):
        """Starts rendering and interaction between objects.
        """

        while True:
            self.__update_rectangles()
            self.__check_collisions()
            self.__draw_rectangles()

    def __close_app(self, _):
        """Destroy tkinter application.
        """

        self.__root.destroy()

    def start_app(self):
        """Start tkinter application.
        """

        self.__root.mainloop()
