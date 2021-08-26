from tkinter import *
from views import simulation_view, chose_variables
from constants import constants


class start_menu:

    WINDOW_WIDTH = 300
    WINDOW_HEIGHT = 340

    FRAME_BG = "dark grey"


    def __init__(self):
        root = Tk()
        self.setup_root(root)
        self.setup_views(root)
        root.mainloop()


    def setup_views(self, root):
        main_frame = self.create_main_frame(root)
        self.setup_main_frame_components(main_frame, root)


    def setup_root(self, root):
        root.title('Virus Simulator')
        self.center_frame(root)


    def center_frame(self, root):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_location = int(screen_width/2 - self.WINDOW_WIDTH/2)
        y_location = int(screen_height/2 - self.WINDOW_HEIGHT/2)
        root.geometry('{}x{}+{}+{}'.format(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, x_location, y_location))


    def create_main_frame(self, root):
        main_frame = Frame(root, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT, bg=constants.FRAME_BG)
        main_frame.pack()
        return main_frame


    def setup_main_frame_components(self, frame, root):
        self.setup_simulation_button(frame, root)
        self.setup_other_button(frame)
        self.setup_exit_button(frame, root)


    def setup_simulation_button(self, frame, root):
        simulation_button = Button(frame, bg="dark grey", text="Simulation",
                                   command=lambda:self.go_to_simulation_variables(root), width=15, height=3)
        simulation_button.pack(side=TOP, padx=100, pady=30)


    def setup_other_button(self, frame):
        other_button = Button(frame, bg="dark grey", text="Not yet",
                                   width=15, height=3, state=DISABLED)
        other_button.pack(padx=100, pady=30)


    def setup_exit_button(self, frame, root):
        exit_button = Button(frame, bg="dark grey", text="Exit", command=root.destroy,
                                   width=15, height=3)
        exit_button.pack(side=BOTTOM, padx=100, pady=30)


    def go_to_simulation_variables(self, root):
        root.destroy()
        chose_variables.chose_variables()