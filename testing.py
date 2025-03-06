import tkinter as tk
from tkinter import ttk

def on_mousewheel(widget, func, modifier="Any") -> None:
    widget.bind(f'<{modifier}-Button-4>', func)
    widget.bind(f'<{modifier}-Button-5>', func)

# window
window = tk.Tk()
# window.title('Event Binding')
# window.geometry('600x500')

# # window.bind('<KeyPress>', lambda event: print('a button was pressed.'))
# # widgets
# # print 'mousewheel' when the user holds down shift and uses the mousewheel while the text is selected
# entry = ttk.Entry(window)
# entry.pack()

# text = tk.Text(window)
# text.pack()

on_mousewheel(window, lambda event: print(event))

# run
window.mainloop()
