from tkinter import *
from objects import map
from controller import manager
from views import stack_graph_view
from constants import constants

class simulation_view:

    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 720

    map_list = []
    entry = []

    global animation_canvas
    global new_manager
    global graph_view

    def __init__(self, entry):
        root = Tk()
        self.entry = entry
        self.setup_root(root)
        self.setup_views(root)
        root.mainloop()


    def create_animation_canvas(self,animation_frame):
        animation_canvas = Canvas(animation_frame, width=960, height=720, bg=constants.CANVAS_BG)
        animation_canvas.pack()
        self.map_list.append(map.map(animation_canvas, 960, 720, constants.FRAME_BG))
        self.create_manager()


    def get_animation_canvas(self):
        return self.animation_canvas


    def create_graph_frame(self,main_frame):
        graph_frame = Frame(main_frame, bg=constants.FRAME_BG, width=self.WINDOW_WIDTH / 2,
                            height=self.WINDOW_HEIGHT, highlightbackground="black", highlightthickness=1, bd=2)
        graph_frame.pack(side=LEFT)
        button = Button(graph_frame, text="button", command=self.start_simulation)
        button.pack()
        self.graph_view = stack_graph_view.stack_graph_view(graph_frame, self.entry)




    def create_animation_frame(self, main_frame):
        animation_frame = Frame(main_frame, bg=constants.FRAME_BG, width=self.WINDOW_WIDTH / 2,
                                height=self.WINDOW_HEIGHT, highlightbackground="black", highlightthickness=1, bd=2)
        animation_frame.pack(side=RIGHT)
        self.create_animation_canvas(animation_frame)


    def create_main_frame(self,root):
        main_frame = Frame(root, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        self.center_frame(root)
        main_frame.pack()
        return main_frame


    def center_frame(self, root):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_location = int(screen_width/2 - self.WINDOW_WIDTH/2)
        y_location = int(screen_height/2 - self.WINDOW_HEIGHT/2)
        root.geometry('{}x{}+{}+{}'.format(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, x_location, y_location))

    def setup_views(self, root):
        main_frame = self.create_main_frame(root)
        self.create_animation_frame(main_frame)
        self.create_graph_frame(main_frame)


    def setup_root(self, root):
        root.title("Virus Simulator")
        root.geometry("1920x720")

    def create_manager(self):
        self.new_manager = manager.controller(self.map_list, self.entry)

    def start_simulation(self):
        self.new_manager.start_game(self.graph_view)