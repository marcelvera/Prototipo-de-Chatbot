import tkinter as tk
from tkinter import ttk

def round_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def on_entry_click(event):
    """Function that gets called whenever entry is clicked"""
    if entry.get() == 'Escriba aquí su pregunta':
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')

def on_focusout(event):
    """Function that gets called whenever entry loses focus"""
    if entry.get() == '':
        entry.insert(0, 'Escriba aquí su pregunta')
        entry.config(fg='grey')

root = tk.Tk()
root.geometry("300x200")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Crear el rectángulo redondeado
round_rectangle(canvas, 50, 50, 250, 100, radius=20, fill="#f0f0f0", outline="black")

# Crear el Entry
entry = tk.Entry(root, bd=0, fg='grey')
entry.insert(0, 'Escriba aquí su pregunta')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.place(x=55, y=60, width=190, height=30)

root.mainloop()
