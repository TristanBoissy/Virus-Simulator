from constants import constants, csv_data_file
from objects import circle_object
from objects import position
import random
import time, threading
import math
from controller import get_value_from_entry_list
import csv

global instance

class controller:

    TIMER = 0.1

    NOT_INFECTED_STATE = "not_infected"
    INFECTED_STATE = "infected"
    IMMUNE_STATE = "immune"

    map_list = []
    infection_list = []

    global graph_view

    def __init__(self, maps, entry):
        self.map_list = maps

        self.max_circles = int(get_value_from_entry_list.get_value(entry, constants.MAX_CIRCLES_STRING))

        self.circle_size = int(get_value_from_entry_list.get_value(entry, constants.CIRCLE_SIZE_STRING))

        self.min_speed = int(get_value_from_entry_list.get_value(entry, constants.MIN_SPEED_STRING))

        self.max_speed = int(get_value_from_entry_list.get_value(entry, constants.MAX_SPEED_STRING))

        self.chance_of_changing_a_direction = float(get_value_from_entry_list.get_value(
            entry, constants.CHANCE_OF_CHANGING_DIRECTION_STRING))

        self.chance_of_changing_the_speed= float(get_value_from_entry_list.get_value(
            entry, constants.CHANCE_OF_CHANGING_SPEED_STRING))

        self.number_of_infected_at_start = int(get_value_from_entry_list.get_value(
            entry, constants.NUMBER_OF_INFECTED_AT_START_STRING))

        self.max_distance_for_infection = int(get_value_from_entry_list.get_value(
            entry, constants.MAX_DISTANCE_FOR_INFECTION_STRING))

        self.max_infection_time = int(get_value_from_entry_list.get_value(
            entry, constants.MAX_INFECTION_TIME_STRING)) / self.TIMER

        self.infection_probability = float(get_value_from_entry_list.get_value(
            entry, constants.INFECTION_PROBABILITY_STRING))

        self.time_remaining = float(get_value_from_entry_list.get_value(
            entry, constants.TIME_STRING))

        self.time_at_start = self.time_remaining

        self.not_infected_circles = self.max_circles - self.number_of_infected_at_start
        self.infected_circles = self.number_of_infected_at_start
        self.immune_circles = 0

        csv_data_file.setup_csv_data_file(self.not_infected_circles, self.infected_circles, self.immune_circles)

        self.instance = self


    def get_instance(self):
        return self


    def start_game(self, graph_view):
        self.graph_view = graph_view
        self.add_circles_to_map()
        self.play_game()


    def play_game(self):
        while True:
            time.sleep(self.TIMER)
            self.play_circles_turn()
            self.time_remaining -= self.TIMER
            #self.update_graph()
            if(self.check_time()):
                break


    def check_time(self):
        return math.ceil(self.time_remaining) == 0


    def infection_at_start(self, map):
        for i in range(self.number_of_infected_at_start):
            self.change_circle_state(map,
                                     map.get_circle_from_list(self.random_int(0, self.max_circles-1)),
                                     self.INFECTED_STATE,
                                     constants.INFECTED_COLOR)


    def add_circles_to_map(self):
        for i in range(0, self.max_circles):
            self.map_list[0].add_circle_to_map(self.random_position(),
                                               self.circle_size,
                                               constants.NOT_INFECTED_COLOR,
                                               str(self.NOT_INFECTED_STATE),
                                               self.max_infection_time)
        self.infection_at_start(self.map_list[0])
        self.map_list[0].update_canvas()


    def play_circles_turn(self):
        self.reset_infection_info()
        for i in self.map_list:
            circles_list = i.get_circles_list()
            for y in circles_list:
                self.move_and_verify_circle_movement(i, y)
                self.update_infection_info(y)
                if(y.get_infection_state() == self.INFECTED_STATE):
                    if(y.get_infection_time() != y.get_max_infection_time()):
                        y.set_infection_time(y.get_infection_time() + 1)
                    else:
                        self.change_circle_state(i, y, self.IMMUNE_STATE, constants.IMMUNE_COLOR)

            self.verify_infection(i)
            i.update_canvas()
        self.update_csv_file_data()
        self.update_graph_view()


    def circle_motion(self, circle):

        if(self.check_if_first_circle_movement(circle)): # sets the value for the first turn
            self.play_first_circle_movement(circle)
            return

        if(self.chance_of_changing_direction()):
            self.change_circle_x_direction(circle) # changes x direction

        if (self.chance_of_changing_direction()):
            self.change_circle_y_direction(circle)  # changes y direction

        if (self.chance_of_changing_speed()):
            self.change_random_circle_x_speed(circle) # changes x speed

        if (self.chance_of_changing_speed()):
            self.change_random_circle_y_speed(circle) # changes y speed




    def play_first_circle_movement(self, circle):
        circle.set_x_direction(self.random_direction())
        circle.set_y_direction(self.random_direction())
        circle.set_x_speed(self.random_int(self.min_speed, self.max_speed))
        circle.set_y_speed(self.random_int(self.min_speed, self.max_speed))


    def check_if_first_circle_movement(self, circle):
        return (circle.get_x_direction() == 0)


    def chance_of_changing_direction(self):
        return (self.random_float() < self.chance_of_changing_a_direction)


    def change_circle_x_direction(self,circle):
        if(circle.get_x_direction() == 1):
            circle.set_x_direction(-1)
        else:
            circle.set_x_direction(1)


    def change_circle_y_direction(self, circle):
        if (circle.get_y_direction() == 1):
            circle.set_y_direction(-1)
        else:
            circle.set_y_direction(1)


    def chance_of_changing_speed(self):
        return (self.random_float() < self.chance_of_changing_the_speed)


    def change_random_circle_x_speed(self, circle):
        circle.set_x_speed(self.random_int(self.min_speed, self.max_speed))


    def change_random_circle_y_speed(self, circle):
        circle.set_y_speed(self.random_int(self.min_speed, self.max_speed))


    def random_position(self):
        return position.position_2D(self.random_int(0,self.map_list[0].get_x_dimension()), # x position
                                    self.random_int(0,self.map_list[0].get_y_dimension())) # y position


    def random_int(self, min, max):
        return random.randint(min, max)


    def random_float(self):
        return random.uniform(0,1)


    def random_direction(self):
        rand = random.randint(0,1)
        if rand == 0:
            return -1
        else:
            return 1


    def move_and_verify_circle_movement(self, map, circle):

        self.circle_motion(circle)
        new_x_value = self.verify_circle_one_axis_position(circle.get_x() + circle.get_x_movement(),
                                                                 map.get_x_dimension())
        new_y_value = self.verify_circle_one_axis_position(circle.get_y() + circle.get_y_movement(),
                                                                 map.get_y_dimension())
        circle.set_x(new_x_value)
        circle.set_y(new_y_value)
        map.move_circle_on_map(circle)


    def verify_circle_one_axis_position(self, value, boundary):
        if (value < 0):
            return value + boundary
        elif (value > boundary):
            return value % boundary
        else:
            return value


    def change_circle_state(self, map, circle, infection_state, state_color):
        circle.set_infection_state(infection_state)
        circle.set_color(state_color)
        map.change_circle_color(circle, circle.get_color())


    def verify_infection(self, map):
        for i in map.get_circles_list():
            if(i.get_infection_state() == self.INFECTED_STATE):
                self.check_if_other_circle_is_close(map, i)


    def check_if_other_circle_is_close(self, map, circle):

        x = circle.get_x()
        y = circle.get_y()

        for i in map.get_circles_list():
            if i is not circle and i.get_infection_state() == self.NOT_INFECTED_STATE:
                    if(self.check_if_distance_is_close(self.calculate_distance(x, y, i.get_x(), i.get_y()))):
                        if(self.chance_of_getting_infected()):
                            self.change_circle_state(map, i, self.INFECTED_STATE, constants.INFECTED_COLOR)


    def chance_of_getting_infected(self):
        return self.random_float() < self.infection_probability


    def check_if_distance_is_close(self, distance):
        return distance <= self.max_distance_for_infection


    def calculate_distance(self, x1, y1, x2, y2):
        return (math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2)))


    def update_csv_file_data(self):
        csv_data_file.update_csv_file(self.get_duration(),
                                      self.not_infected_circles,
                                      self.infected_circles,
                                      self.immune_circles)


    def reset_infection_info(self):
        self.not_infected_circles = 0
        self.infected_circles = 0
        self.immune_circles = 0


    def update_infection_info(self, circle):
        if(circle.get_infection_state() == self.NOT_INFECTED_STATE):
            self.not_infected_circles += 1
        if(circle.get_infection_state() == self.INFECTED_STATE):
            self.infected_circles += 1
        if(circle.get_infection_state() == self.IMMUNE_STATE):
            self.immune_circles += 1


    def update_graph_view(self):
        self.graph_view.update_graph_data()

    def get_duration(self):
        return self.time_at_start - self.time_remaining