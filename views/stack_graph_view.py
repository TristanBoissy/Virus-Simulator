import tkinter as tk

import pandas as pd

from constants import constants
from controller import get_value_from_entry_list
import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.lines import Line2D


class stack_graph_view():



    legend_elements = [Line2D([0], [0], color=constants.NOT_INFECTED_COLOR, lw=4, label='Line'),
                       Line2D([0], [0], color=constants.INFECTED_COLOR, lw=4, label='Line'),
                       Line2D([0], [0], color=constants.IMMUNE_COLOR, lw=4, label='Line')]

    def __init__(self, graph_frame, entry):

        self.fig = Figure(figsize=(10,7))
        self.a = self.fig.add_subplot(111)
        self.fig.set_facecolor(constants.FRAME_BG)
        self.circle = int(get_value_from_entry_list.get_value(entry,constants.MAX_CIRCLES_STRING))
        self.time = int(get_value_from_entry_list.get_value(entry,constants.TIME_STRING))

        canvas = FigureCanvasTkAgg(self.fig, master=graph_frame)
        canvas.get_tk_widget().pack()
        canvas.draw()

        self.update_graph_data()




    def update_graph_data(self):
        data = pd.read_csv('data.csv')
        time = data["time"]
        not_infected = data["not_infected"]
        infected = data["infected"]
        immune = data["immune"]
        self.stack_plot(time, not_infected, infected, immune)
        self.fig.canvas.draw()


    def stack_plot(self, time, not_infected, infected, immune):
        self.a.cla()
        self.a.set_facecolor(constants.CANVAS_BG)
        self.a.set_title("Infection")
        self.a.set_ylabel("Number of : ")
        self.a.set_xlabel("Time (s)")
        self.a.set_ylim(self.circle)
        self.a.set_xlim(self.time)
        self.a.invert_xaxis()
        self.a.invert_yaxis()
        self.a.stackplot(time, not_infected, infected, immune, baseline="zero",
                         colors =[constants.NOT_INFECTED_COLOR, constants.INFECTED_COLOR, constants.IMMUNE_COLOR])
        self.a.legend(self.legend_elements, ["Not infected", "Infected", "Immune"])
