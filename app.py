import tkinter as tk
from tkinter import ttk
import pandas as pd

from datetime import datetime
from settings import *

# app that gives you the best options for making money in your current time for ACNH

# first window is setup
# gather hemisphere
# automatically gather current month and time
def setup():
    # import in the data
    insects = pd.read_csv("acnh_insect_data.csv")
    fish = pd.read_csv("acnh_fish_data.csv")
    sea_creatures = pd.read_csv("acnh_sea_creature_data.csv")
    return insects, fish, sea_creatures

def main():
window = tk.Tk()
window.geometry('900x800')
window.title('ACNH Money Genie')

# create setup info to gather data
current_time = datetime.now().strftime('%a %d %b %Y, %I:%M%p')

# try and get current month and hour automagically
date_string = tk.StringVar(value = current_time)
hour_string = tk.IntVar(value = datetime.now().hour)
month_string = tk.IntVar(value = datetime.now().month)

# default to NH...
hemisphere_string = tk.StringVar(value = HEMISPHERES[0])
hemisphere_label_string = tk.StringVar(value = "Hemisphere: ")

items = HEMISPHERES
combo_label = tk.Label(window, textvariable = hemisphere_label_string)
combo = ttk.Combobox(window, textvariable = hemisphere_string)
combo['values'] = items
combo_label.pack()
combo.pack()

print(fish[["Name", "Sell"]])

window.mainloop()
