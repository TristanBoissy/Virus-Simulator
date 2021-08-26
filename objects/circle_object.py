from tkinter import Canvas

class Circles:

    CIRCLE_DEFAULT_SIZE = 10

    def __init__(self, drawn_circle, position, size, color, infection_state, max_infection_time):
        self.drawn_circle = drawn_circle
        self.position = position
        self.x_direction = 0
        self.y_direction = 0
        self.x_speed = 0
        self.y_speed = 0
        self.size = size
        self.color = color
        self.infection_state = infection_state
        self.infection_time = 0
        self.max_infection_time = max_infection_time


    def get_drawn_circle(self):
        return self.drawn_circle


    def get_x(self):
        return self.position.get_x()


    def get_y(self):
        return self.position.get_y()


    def get_x_direction(self):
        return self.x_direction


    def get_y_direction(self):
        return self.y_direction


    def get_x_speed(self):
        return self.x_speed


    def get_y_speed(self):
        return self.y_speed


    def get_size(self):
        return self.size


    def get_color(self):
        return self.color


    def get_infection_state(self):
        return self.infection_state


    def get_x_movement(self):
        return (self.x_speed * self.x_direction)


    def get_y_movement(self):
        return (self.y_speed * self.y_direction)


    def get_infection_time(self):
        return self.infection_time


    def get_max_infection_time(self):
        return self.max_infection_time


    def set_x(self, x):
        self.position.set_x(x)


    def set_y(self, y):
        self.position.set_y(y)


    def set_x_direction(self, value):
        self.x_direction = value


    def set_y_direction(self, value):
        self.y_direction = value


    def set_x_speed(self, value):
        self.x_speed = value


    def set_y_speed(self, value):
        self.y_speed = value


    def set_size(self, new_size):
        self.size = new_size


    def set_color(self, new_color):
        self.color = new_color


    def set_infection_state(self, new_state):
        self.infection_state = str(new_state)


    def set_infection_time(self, value):
        self.infection_time = value


    def set_max_infection_time(self, value):
        self.max_infection_time = value