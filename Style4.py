import tkinter as tk

def on_button_click():
    print("Botón redondo presionado")

def on_enter(event):
    canvas.itemconfig(circle, fill="#FF5722")  # Cambia el color al pasar el mouse

def on_leave(event):
    canvas.itemconfig(circle, fill="#FFA12E")  # Cambia de nuevo al color original

root = tk.Tk()
root.geometry("300x200")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Dibujar el botón redondo
x0, y0, x1, y1 = 100, 50, 200, 150
circle = canvas.create_oval(x0, y0, x1, y1, fill="#FFA12E", outline="#FFA12E")

# Agregar texto sobre el botón
text = canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text="ENVIAR", fill="white", font=("Arial", 12, "bold"))

def button_click(event):
    # Verificar si el clic está dentro del círculo
    if canvas.type(circle) == 'oval':
        coords = canvas.coords(circle)
        if (event.x - (coords[0] + coords[2]) / 2) ** 2 + (event.y - (coords[1] + coords[3]) / 2) ** 2 <= ((coords[2] - coords[0]) / 2) ** 2:
            on_button_click()

# Vincular eventos de clic
canvas.tag_bind(circle, '<Button-1>', button_click)
canvas.tag_bind(text, '<Button-1>', button_click)

# Vincular eventos de entrada y salida del mouse para cambiar el color
canvas.tag_bind(circle, '<Enter>', on_enter)
canvas.tag_bind(circle, '<Leave>', on_leave)
canvas.tag_bind(text, '<Enter>', on_enter)
canvas.tag_bind(text, '<Leave>', on_leave)

root.mainloop()
