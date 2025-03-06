import tkinter as tk

def on_mousewheel(widget, func, modifier="Any"):
    widget.bind(f'<{modifier}-Button-4>', func)
    widget.bind(f'<{modifier}-Button-5>', func)

# window
window = tk.Tk()

on_mousewheel(window, lambda event: print(event))

# run
window.mainloop()
