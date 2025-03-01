import customtkinter as ctk
import pandas as pd
from datetime import datetime
from settings import *

# import in the data
insects = pd.read_csv("acnh_insect_data.csv")
fish = pd.read_csv("acnh_fish_data.csv")
sea_creatures = pd.read_csv("acnh_sea_creature_data.csv")

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = BG_COLOR)
        self.geometry('900x800')
        self.title('')

        # create setup info to gather data
        self.current_time = datetime.now().strftime('%a %d %b %Y, %I:%M%p')
        print(self.current_time, self.current_hour, self.current_month)

        # try and get current month and hour automagically
        self.date_string = ctk.StringVar(value = self.current_time)
        self.hour_string = ctk.IntVar(value = datetime.now().hour)
        self.month_string = ctk.IntVar(value = datetime.now().month)

        # default to NH...
        self.hemisphere_string = ctk.StringVar(value = HEMISPHERES[0])



        #self.mainloop()

App()
