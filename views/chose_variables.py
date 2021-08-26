from tkinter import *
from views import simulation_view
from constants import constants


class chose_variables:

    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 200

    BUTTON_BG = "dark grey"

    DEFAULT_MAX_CIRCLES = 300
    DEFAULT_CIRCLE_SIZE = 10

    DEFAULT_MIN_SPEED = 1
    DEFAULT_MAX_SPEED = 5

    DEFAULT_CHANCE_OF_CHANGING_DIRECTION = 0.05
    DEFAULT_CHANCE_OF_CHANGING_SPEED = 0.3

    DEFAULT_NUMBER_OF_INFECTED_AT_START = 2
    DEFAULT_MAX_DISTANCE_FOR_INFECTION = 10
    DEFAULT_MAX_INFECTION_TIME = 10
    DEFAULT_INFECTION_PROBABILITY = 0.5

    DEFAULT_TIME = 60

    entry = []

    def __init__(self):

        root = Tk()
        self.setup_root(root)
        self.setup_views(root)
        root.mainloop()


    def setup_views(self, root):
        self.setup_main_frame_components(root)


    def setup_root(self, root):
        root.title("Virus Simulator")
        root.configure(background=constants.FRAME_BG)
        self.center_window(root)


    def center_window(self, root):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_location = int(screen_width/2 - self.WINDOW_WIDTH/2)
        y_location = int(screen_height/2 - self.WINDOW_HEIGHT/2)
        root.geometry('{}x{}+{}+{}'.format(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, x_location, y_location))


    def setup_main_frame_components(self, root):
        circle_frame = self.setup_circle_components(root)
        infection_frame = self.setup_infection_components(root)

        circle_frame.pack(side=LEFT, padx=1, pady=10)
        infection_frame.pack(side=RIGHT, padx=1, pady=10)

        start_button = Button(root, text="Start",bg=constants.FRAME_BG, command=lambda:self.go_to_simulation(root))
        start_button.pack(side=BOTTOM, padx=1, pady=10)



    def setup_circle_components(self, root):
        circle_frame = self.create_frame(root, constants.FRAME_BG)
        self.setup_circle_amount_components(circle_frame)
        self.setup_circle_size_components(circle_frame)
        self.setup_circle_min_speed_components(circle_frame)
        self.setup_circle_max_speed_components(circle_frame)
        self.setup_circle_chance_of_changing_direction_components(circle_frame)
        self.setup_circle_chance_of_changing_speed_components(circle_frame)
        return circle_frame


    def setup_circle_amount_components(self, circle_frame):
        self.max_circles_entry = StringVar(circle_frame, self.DEFAULT_MAX_CIRCLES)
        self.create_frame_for_components(circle_frame,
                                         "Number of Objects",
                                         constants.FRAME_BG,
                                         self.max_circles_entry,
                                         5,
                                         NORMAL)


    def setup_circle_size_components(self, circle_frame):
        self.circle_size_entry = StringVar(circle_frame, self.DEFAULT_CIRCLE_SIZE)
        self.create_frame_for_components(circle_frame,
                                         "Size of Objects",
                                         constants.FRAME_BG,
                                         self.circle_size_entry,
                                         5,
                                         NORMAL)


    def setup_circle_min_speed_components(self, parent_frame):
        self.min_speed_entry = StringVar(parent_frame, self.DEFAULT_MIN_SPEED)
        self.create_frame_for_components(parent_frame,
                                         "Minimum speed",
                                         constants.FRAME_BG,
                                         self.min_speed_entry,
                                         5,
                                         NORMAL)


    def setup_circle_max_speed_components(self, parent_frame):
        self.max_speed_entry = StringVar(parent_frame, self.DEFAULT_MAX_SPEED)
        self.create_frame_for_components(parent_frame,
                                         "Maximum speed",
                                         constants.FRAME_BG,
                                         self.max_speed_entry,
                                         5,
                                         NORMAL)


    def setup_circle_chance_of_changing_direction_components(self, parent_frame):
        self.chance_of_changing_direction_entry = StringVar(parent_frame, self.DEFAULT_CHANCE_OF_CHANGING_DIRECTION)
        self.create_frame_for_components(parent_frame,
                                         "Direction change probability",
                                         constants.FRAME_BG,
                                         self.chance_of_changing_direction_entry,
                                         5,
                                         DISABLED)


    def setup_circle_chance_of_changing_speed_components(self, parent_frame):
        self.chance_of_changing_speed_entry = StringVar(parent_frame, self.DEFAULT_CHANCE_OF_CHANGING_SPEED)
        self.create_frame_for_components(parent_frame,
                                         "Speed change probability",
                                         constants.FRAME_BG,
                                         self.chance_of_changing_speed_entry,
                                         5,
                                         DISABLED)


    def setup_infection_components(self, root):
        infection_frame = self.create_frame(root, constants.FRAME_BG)
        self.setup_number_of_infected(infection_frame)
        self.setup_max_distance_for_infection(infection_frame)
        self.setup_max_infection_time(infection_frame)
        self.setup_infection_probability(infection_frame)
        self.setup_time(infection_frame)
        return infection_frame


    def setup_number_of_infected(self, parent_frame):
        self.number_of_infected_at_start_entry = StringVar(parent_frame, self.DEFAULT_NUMBER_OF_INFECTED_AT_START)
        self.create_frame_for_components(parent_frame,
                                         "Infected object at start",
                                         constants.FRAME_BG,
                                         self.number_of_infected_at_start_entry,
                                         5,
                                         NORMAL)


    def setup_max_distance_for_infection(self, parent_frame):
        self.max_distance_for_infection_entry = StringVar(parent_frame, self.DEFAULT_MAX_DISTANCE_FOR_INFECTION)
        self.create_frame_for_components(parent_frame,
                                         "Infected max distance",
                                         constants.FRAME_BG,
                                         self.max_distance_for_infection_entry,
                                         5,
                                         NORMAL)


    def setup_max_infection_time(self, parent_frame):
        self.max_infection_time_entry = StringVar(parent_frame, self.DEFAULT_MAX_INFECTION_TIME)
        self.create_frame_for_components(parent_frame,
                                         "Infection time (s)",
                                         constants.FRAME_BG,
                                         self.max_infection_time_entry,
                                         5,
                                         NORMAL)


    def setup_infection_probability(self, parent_frame):
        self.infection_probability_entry = StringVar(parent_frame, self.DEFAULT_INFECTION_PROBABILITY)
        self.create_frame_for_components(parent_frame,
                                         "Infection probability",
                                         constants.FRAME_BG,
                                         self.infection_probability_entry,
                                         5,
                                         NORMAL)

    def setup_time(self, parent_frame):
        self.time_entry = StringVar(parent_frame, self.DEFAULT_TIME)
        self.create_frame_for_components(parent_frame,
                                         "Time (s)",
                                         constants.FRAME_BG,
                                         self.time_entry,
                                         5,
                                         NORMAL)


    def create_frame_for_components(self, parent_frame, text, bg, entry_reference, entry_size, state):
        new_frame = self.create_label_and_input_frame(parent_frame, text, bg, entry_reference, entry_size, state)
        new_frame.pack()


    def create_label_and_input_frame(self, parent_frame, label_text, bg, entry_reference, entry_width, entry_state):
        new_frame = self.create_frame(parent_frame, bg)
        new_frame.pack()

        new_label = self.create_label(new_frame, label_text, bg)
        new_label.pack(side=LEFT)

        entry = self.create_entry_box(new_frame, entry_reference, entry_width, state=entry_state)
        entry.pack(side=LEFT)

        return new_frame


    def create_frame(self, parent_frame, bg):
        return Frame(parent_frame, bg=bg)


    def create_label(self, parent_frame, text, bg):
        return Label(parent_frame, text=text, bg=bg)


    def create_entry_box(self, parent_frame, entry_reference, entry_width, state):
        return Entry(parent_frame, width=entry_width, textvariable=entry_reference, state=state)


    def get_entry(self):
        self.entry.append([constants.MAX_CIRCLES_STRING, self.max_circles_entry.get()])
        self.entry.append([constants.CIRCLE_SIZE_STRING, self.circle_size_entry.get()])
        self.entry.append([constants.MIN_SPEED_STRING, self.min_speed_entry.get()])
        self.entry.append([constants.MAX_SPEED_STRING, self.max_speed_entry.get()])
        self.entry.append([constants.CHANCE_OF_CHANGING_DIRECTION_STRING, self.chance_of_changing_direction_entry.get()])
        self.entry.append([constants.CHANCE_OF_CHANGING_SPEED_STRING, self.chance_of_changing_speed_entry.get()])
        self.entry.append([constants.NUMBER_OF_INFECTED_AT_START_STRING, self.number_of_infected_at_start_entry.get()])
        self.entry.append([constants.MAX_DISTANCE_FOR_INFECTION_STRING, self.max_distance_for_infection_entry.get()])
        self.entry.append([constants.MAX_INFECTION_TIME_STRING, self.max_infection_time_entry.get()])
        self.entry.append([constants.INFECTION_PROBABILITY_STRING, self.infection_probability_entry.get()])
        self.entry.append([constants.TIME_STRING, self.time_entry.get()])


    def go_to_simulation(self, root):
        root.destroy()
        self.get_entry()
        simulation_view.simulation_view(self.entry)
