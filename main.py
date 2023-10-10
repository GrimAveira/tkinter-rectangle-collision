import tkinter as tk


class RectangleCollision:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("Rectangle Collision")
        self.canvas = tk.Canvas(
            self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        self.rectangles = []
        self.create_rectangle(50, 50, 100, 100, 4, [0.03, 0], "aqua")
        self.create_rectangle(400, 50, 450, 100, 1, [-0.02, 0], "black")

        self.main_menu = tk.Menu()
        self.main_menu.add_cascade(label="File")
        self.main_menu.add_cascade(label="Edit")
        self.main_menu.add_cascade(label="View")

        self.root.config(menu=self.main_menu)

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

    def run(self):
        while True:
            self.update_rectangles()
            self.check_collisions()
            self.draw_rectangles()


if __name__ == '__main__':
    app = RectangleCollision()
    app.run()
    app.root.mainloop()
