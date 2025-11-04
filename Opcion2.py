from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser

def open_link1(event):
    webbrowser.open("https://www.facebook.com/PSMMaracaiboOLD/?locale=es_LA")
    
def open_link2(event):
    webbrowser.open("https://www.instagram.com/psmmaracaibo?igsh=bXBlOWp4ZHRhMXlh")
    
def open_link3(event):
    webbrowser.open("https://www.tiktok.com/@psmmaracaibo?_t=8nzbrkceShC&_r=1")

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
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def on_entry_click(event):
    if entry.get() == 'Escriba aqui su pregunta...':
        entry.delete(0, "end")
        entry.insert(0, '')
        entry.config(fg='black', font=('Consolas', 12))

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Escriba aqui su pregunta...')
        entry.config(fg='grey', font=('Consolas', 12))

def manejar_entrada(event):
    usuario_input = entry.get().strip()
    resultado_texto.config(state=tk.NORMAL)
    resultado_texto.insert(tk.END, f"\nTú: {usuario_input}\n\nConsultor: {usuario_input}\n")
    resultado_texto.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

rootmain = tk.Tk()

rootmain.title("PSM Maracaibo")
rootmain.config(bg='#FFFFFF')
rootmain.iconbitmap(r'images.ico')
rootmain.state('zoomed')

bg_image = Image.open(r"fondo.jpg")
bg_image = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(rootmain, width=2000, height=2000, borderwidth=-2)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

marco = tk.Frame(relief='solid', borderwidth=-2, bg='#FFFFFF')
marco.pack(fill='y', expand=True)
marco.config(width=1000, height=720)

marco2 = tk.Frame(marco, bg='#3498db', width=1000, height=100, borderwidth=-2)  
marco2.place(x=0, y=0)

marco3 = tk.Frame(marco, bg='#3498db', width=1000, height=100, borderwidth=-2)  
marco3.place(x=0, y=750)

imagen = Image.open(r"unnamed.png")
imagen = ImageTk.PhotoImage(imagen)

logo = tk.Canvas(marco2, width=996, height=100, bg='#00BFFF', highlightthickness=0)
logo.place(x=20, y=10)
logo.create_image(0, 0, anchor='nw', image=imagen)

info = tk.Canvas(marco2, width=400, height=70, bg='#00BFFF', borderwidth=-2)
info.place(x=620, y=25)
info = round_rectangle(info, 0, 0, 800, 45, radius=20, fill="#00008B", outline="black")

info_text= tk.Canvas(marco2, width=350, height=30, bg='#00008B', borderwidth=-5)
info_text.place(x=625, y=33)
info_text.create_text(180,14, text='Consultoria: Pago e Inscripcion', fill='#00BFFF', font=('Consolas', 14))

marco4 = tk.Frame(marco, bg='#2980b9', width=1000, height=100)  
marco4.place(x=0, y=650)

bar_ask = tk.Canvas(marco4, width=600, height=50, bg='#00008B', borderwidth=-5)
bar_ask.place(x=165, y=15)
bar_ask = round_rectangle(bar_ask, 0, 0, 560, 40, radius=20, fill="#00BFFF", outline="black")

entry = tk.Entry(marco4, width=55, relief='groove', bg='#00BFFF', font=('Consolas', 12), borderwidth=0)
entry.place(x=200, y=25, height=20)
entry.insert(0, 'Escriba aqui su pregunta...')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.bind('<Return>', manejar_entrada)

buttons = tk.Canvas(marco4, width=100, height=68, bg='#00008B', borderwidth=-5)
buttons.place(x=745, y=14)
button = round_rectangle(buttons, 0, 0, 78, 40, radius=20, fill="#00BFFF", outline="black")
buttons.bind('<Button-1>', manejar_entrada )

image5 = Image.open(r"icon_send.png")
image5 = ImageTk.PhotoImage(image5)

send_buttons = tk.Canvas(marco4, width=40, height=40, bg="#00BFFF", cursor='hand2', borderwidth=-5)
send_buttons.place(x=766, y=19)
send_buttons.create_image(14,13, image = image5)
send_buttons.bind('<Button-1>', manejar_entrada)

resultado_texto = tk.Text(marco, height=32, width=78, state=tk.DISABLED, relief='sunken', border=4)
resultado_texto.place(x=178, y=115)

retangulo1 = tk.Canvas(marco, bg='#00008B', width=167, height=560, relief='solid', border=-2, borderwidth=-2)
retangulo1.place(x=0, y=100)
retangulo1.create_rectangle(0, 10, 0, 10)

retangulo2 = tk.Canvas(marco, bg='#00008B', width=180, height=560, relief='solid',border=-2, borderwidth=-2)
retangulo2.place(x=822, y=100)
retangulo2.create_rectangle(0, 10, 0, 10)

bar_redes = tk.Canvas(marco3, width=200, height=100, bg='#00BFFF', borderwidth=-5)
bar_redes.place(x=20, y=15)
bar_redes = round_rectangle(bar_redes, 0, 0, 180, 50, radius=20, fill="#00008B", outline="black")

image2 = Image.open(r'facebook (1).png')
image2 =ImageTk.PhotoImage(image2)

facebook = tk.Canvas(marco3, width=45, height=45, cursor='hand2', bg='#00008B', borderwidth=-5)
facebook.place(x=30, y= 20)
facebook.create_image(20,20, image = image2)
facebook.bind('<Button-1>', open_link1)

image3 = Image.open(r'instagram.png')
image3 = ImageTk.PhotoImage(image3)

instagram = tk.Canvas(marco3, width=45, height=45, cursor='hand2', bg='#00008B', borderwidth=-5)
instagram.place(x=91, y= 20)
instagram.create_image(20,20, image = image3)
instagram.bind('<Button-1>', open_link2)

image4 = Image.open(r'tik-tok.png')
image4 = ImageTk.PhotoImage(image4)

tiktok = tk.Canvas(marco3, width=45, height=45, cursor='hand2', bg='#00008B', borderwidth=-5)
tiktok.place(x=150, y= 20)
tiktok.create_image(20,20, image = image4)
tiktok.bind('<Button-1>', open_link3)

rootmain.mainloop()
