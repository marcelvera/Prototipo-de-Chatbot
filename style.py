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

root = tk.Tk()
root.geometry("300x200")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Crear el rectángulo redondeado
round_rectangle(canvas, 50, 50, 250, 100, radius=20, fill="#FFDF5F", outline="black")


# Crear el Entry
entry = tk.Entry(root, bd=0, bg='#FFDF5F')
entry.place(x=55, y=60, width=190, height=30)



root.mainloop()
