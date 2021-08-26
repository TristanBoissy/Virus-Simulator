from objects import circle_object
import time


class map:

    circles_list = []

    def __init__(self, canvas, x_dimension, y_dimension, color):
        self.canvas = canvas
        self.x_dimension = x_dimension
        self.y_dimension = y_dimension
        self.color = color


    def get_x_dimension(self):
        return self.x_dimension


    def get_y_dimension(self):
        return self.y_dimension


    def get_circle_from_list(self, index):
        return self.circles_list[index]


    def get_circles_list(self):
        return self.circles_list


    def add_circle_to_map(self, position, size, color, infection_state, max_infection_time):
        drawn_circle = self.canvas.create_oval(position.get_x(),
                                        position.get_y(),
                                        position.get_x()+size,
                                        position.get_y()+size,
                                        fill = color)

        self.circles_list.append(circle_object.Circles(drawn_circle,
                                                       position,
                                                       size,
                                                       color,
                                                       infection_state,
                                                       max_infection_time))
        self.canvas.pack()


    def move_circle_on_map(self,circle):
        self.canvas.coords(circle.get_drawn_circle(), circle.get_x(),
                           circle.get_y(),
                           circle.get_x()+circle.get_size(),
                           circle.get_y()+circle.get_size())


    def change_circle_color(self, circle, color):
        self.canvas.itemconfig(circle.get_drawn_circle(), fill=color)


    def update_canvas(self):
        self.canvas.update()
