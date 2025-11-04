from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import re
import random
from pyDolarVenezuela.pages import CriptoDolar
from pyDolarVenezuela import Monitor, currency_converter
import webbrowser
import os

global chatmini 
chatmini = None

global bg_image
bg_image = None

global entry
entry = None

global resultado_texto
resultado_texto = None

def open_link1(event):
    webbrowser.open("https://www.facebook.com/PSMMaracaiboOLD/?locale=es_LA")
    
def open_link2(event):
    webbrowser.open("https://www.instagram.com/psmmaracaibo?igsh=bXBlOWp4ZHRhMXlh")
    
def open_link3(event):
    webbrowser.open("https://www.tiktok.com/@psmmaracaibo?_t=8nzbrkceShC&_r=1")

# Función para obtener el precio del dólar
def obtener_precio_dolar():
    monitor = Monitor(CriptoDolar, 'USD')
    informacion_dolar = monitor.get_value_monitors('bcv')
    precio_en_bs = currency_converter(
        type='USD',
        value=1,
        monitor=informacion_dolar
    )
    return precio_en_bs

def cuota_precio():
    monitor = Monitor(CriptoDolar, 'USD')
    informacion_dolar = monitor.get_value_monitors('bcv')
    precio_en_bs = currency_converter(
        type='USD',
        value=95,
        monitor=informacion_dolar
    )
    return precio_en_bs

def inscripcion_precio():
    monitor = Monitor(CriptoDolar, 'USD')
    informacion_dolar = monitor.get_value_monitors('bcv')
    precio_en_bs = currency_converter(
        type='USD',
        value=105,
        monitor=informacion_dolar
    )
    return precio_en_bs

# Función para manejar las respuestas del bot
def get_resp(usuario_input):
    remover = re.split(r'\s|[,;:.¿?!-_]\s*', usuario_input.lower())  
    respuesta = ver_mensajes(remover)
    return respuesta

def mensajes_prob(usuario_mensajes, reconocer_palabras, solo_resp=False, requerir_palabra=[]):
    mensaje_correcto = 0
    debe_requerir_palabra = True
    
    for palabra in usuario_mensajes:
        if palabra in reconocer_palabras:
            mensaje_correcto += 1
    
    porcnX = float(mensaje_correcto) / float(len(reconocer_palabras))
    
    for palabra in requerir_palabra:
        if palabra not in usuario_mensajes:
            debe_requerir_palabra = False
            break
    if debe_requerir_palabra or solo_resp:
        return int(porcnX * 100)
    else:
        return 0
    
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

            
def ver_mensajes(mensaje):
    proba_mayor = {}
    precio_en_bs_ahora = obtener_precio_dolar()
    precio_cuota = cuota_precio()
    precio_inscripcion = inscripcion_precio()

    def respuesta(bot_respuestas, lista_palabras, requerir_palabra=[], solo_resp=False):
        nonlocal proba_mayor
        proba_mayor[random.choice(bot_respuestas)] = mensajes_prob(mensaje, lista_palabras, solo_resp, requerir_palabra)
    
    respuesta(['¡Hola! ¿En qué puedo ayudarte hoy?', '¡Hola! ¿Cómo puedo asistirte?', '¡Hola! ¿Qué necesitas?'], ['hola', 'buenas' ,'buenos', 'hello', 'hi', 'qlk', 'ho', 'holis'], solo_resp=True)
    
    respuesta(['¡Hola! Estoy aquí y listo para ayudarte. ¿En qué puedo asesorarte hoy?', 'Estoy aquí, listo para ayudarte. ¿En qué necesitas asistencia?', 'Aquí estoy, ¿cómo puedo ayudarte?'], ["estas", "estás","va", "encuentras", "sientes"], requerir_palabra=["como"])
    
    respuesta(['¡Hola! Estoy aquí y listo para ayudarte. ¿En qué puedo asesorarte hoy?', 'Estoy aquí, listo para ayudarte. ¿En qué necesitas asistencia?', 'Aquí estoy, ¿cómo puedo ayudarte?'], ["estas", "estás", "va", "encuentras", "sientes"], requerir_palabra=["comó"])

    respuesta(['Me alegro de haberte ayudado', 'No hay de que', 'Siempre a su orden', 'De nada, que tenga buen dia'], ['gracias', 'thanks'], solo_resp=True)
     
    respuesta([f'El precio en dolar es: {precio_en_bs_ahora}Bs', f'Claro! el precio en dolar hoy es: {precio_en_bs_ahora}Bs'], ['precio' , 'cuanto'], requerir_palabra=["dolar"])
    
    respuesta(['Nos encontramos ubicados en Av. 28 La Limpia 4001 Zulia', 'Nuestra dirección es Av. 28 La Limpia 4001 Zulia', 'Estamos en Av. 28 La Limpia 4001 Zulia'], ['direccion', "dirección" , 'ubicacion', "ubicación" , 'ubicados' , 'localizados', 'localizacion', "localización", 'sector'], solo_resp=True)
    
    respuesta(['Una cuota es la mensualidad que se paga cada mes para poder seguir viendo tus clases, ¿Quieres saber algo mas al respecto?'], ['cuota'],requerir_palabra=['que'])
    
    respuesta(['Una cuota es la mensualidad que se paga cada mes para poder seguir viendo tus clases, ¿Quieres saber algo mas al respecto?'], ['cuota'],requerir_palabra=['qué'])
    
    respuesta(['En que puedo ayudarte con respecto a las cuotas?', 'Que necesitas saber de la cuota?', 'Que informacion quieres acerca de la cuota?'], ['informacion', "información", 'ayuda'], requerir_palabra=['cuota'])

    respuesta([f'Por supuesto! el precio de la cuota hoy es de: {precio_cuota:.2f}Bs o 95$', f'El monto de la cuota hoy es de: {precio_cuota:.2f}Bs o 95$', f'El monto de la cuota a tasa BCV es de: {precio_cuota:.2f}Bs o 95$'], ['precio' , 'monto' , 'cuanto'], requerir_palabra=['cuota'])

    respuesta(['La inscripcion es el proceso que pasa todo estudiante cada 6 meses y que seguira pasando hasta finalizar su carrera, ya que se debe de inscribir cada nuevo semestre y si es tu primera ves necesitaras una serie de requisitos, los cuales serian:\n\n 1- Partida de Nacimiento (Original) \n\n 2- Notas Certificadas Del 1ro al 5to año (Original y Copia) \n\n 3- Titulo de Bachiller (Original y Copia Fondo Negro) \n\n 4- Constancia de Pre-Inscripcion CNU (Original) \n\n 5- Planilla de Prueba de Aptitud Academica \n\n 6- Carta de Buena Conducta - Original \n\n 7- Constancia de Inscripcion Militar'], ['informacion', 'ayuda'], requerir_palabra=['inscripcion'])
    
    respuesta(['La inscripcion es el proceso que pasa todo estudiante cada 6 meses y que seguira pasando hasta finalizar su carrera, ya que se debe de inscribir cada nuevo semestre y si es tu primera ves necesitaras una serie de requisitos, los cuales serian:\n\n 1- Partida de Nacimiento (Original) \n\n 2- Notas Certificadas Del 1ro al 5to año (Original y Copia) \n\n 3- Titulo de Bachiller (Original y Copia Fondo Negro) \n\n 4- Constancia de Pre-Inscripcion CNU (Original) \n\n 5- Planilla de Prueba de Aptitud Academica \n\n 6- Carta de Buena Conducta - Original \n\n 7- Constancia de Inscripcion Militar'], ['informacion', 'ayuda'], requerir_palabra=['inscripción'])

    respuesta(['Por supuesto los requisitos serian: \n\n 1- Partida de Nacimiento (Original) \n\n 2- Notas Certificadas Del 1ro al 5to año (Original y Copia) \n\n 3- Titulo de Bachiller (Original y Copia Fondo Negro) \n\n 4- Constancia de Pre-Inscripcion CNU (Original) \n\n 5- Planilla de Prueba de Aptitud Academica \n\n 6- Carta de Buena Conducta - Original \n\n 7- Constancia de Inscripcion Militar'], ['requisitos', 'datos'], requerir_palabra=['inscripcion'])
    
    respuesta(['Por supuesto los requisitos serian: \n\n 1- Partida de Nacimiento (Original) \n\n 2- Notas Certificadas Del 1ro al 5to año (Original y Copia) \n\n 3- Titulo de Bachiller (Original y Copia Fondo Negro) \n\n 4- Constancia de Pre-Inscripcion CNU (Original) \n\n 5- Planilla de Prueba de Aptitud Academica \n\n 6- Carta de Buena Conducta - Original \n\n 7- Constancia de Inscripcion Militar'], ['requisitos', 'datos'], requerir_palabra=['inscripción'])

    respuesta([f'El precio de la inscripcion a tasa BCV es: {precio_inscripcion:.2f}Bs o 105$', f'El monto de la inscripcion a tasa BCV es: {precio_inscripcion:.2f}Bs o 105$'], ['precio', 'monto', 'cuanto'], requerir_palabra=['inscripcion'])
    
    respuesta([f'El precio de la inscripcion a tasa BCV es: {precio_inscripcion:.2f}Bs o 105$', f'El monto de la inscripcion a tasa BCV es: {precio_inscripcion:.2f}Bs o 105$'], ['precio', 'monto', 'cuanto'], requerir_palabra=['inscripción'])
    
    respuesta(["Para matriculas y cuotas -> | Banco: Banco Nacional de Crédito (BNC) 01910032422132007676 |\n\n\t   Para pago de Seguro Estudiantil -> | Banco: SOFITASA CTA CORRIENTE 0137-0029-09-0000091981 |"] , ['cuentas', 'cuenta'], solo_resp=True)
    
    respuesta(['Puedas pagar por punto desde la caja en PSM o pagar por transferencia, si paga por transferencia entoces necesitara notificar el pago entregando el comprobante en caja'] , ['metodos', 'metodo'], solo_resp=True)
    
    respuesta(['Por supuesto!', 'Tenemos punto en caja'], ['punto'], solo_resp=True)
    
    respuesta(['Claro usted puede contactar con el area de admisión, Los numeros son: +58 0261-4122532 / +58 0412-5805278'], ['contactar', 'contacto', 'telefono', 'telefonos'], requerir_palabra=['admision'])

    respuesta(['Por supuesto! Los numeros de telefono son: +58 0261-4122532 / +58 0412-5805278'], ['numero', 'numeros'], requerir_palabra=['telefono'])
    
    respuesta(['Que informacion necesita? Recuerde que debe de estar relacionada con el pago o inscripcion del psm maracaibo'], [ 'informacion', "información", 'ayuda', 'consulta', 'consultar'], solo_resp= True)
    
    respuesta(['Claro! Usted puede consultar su nota en el siguiente link: http://ow.ly/XUtmr'], ['ver', 'verificar', 'consultar'], requerir_palabra=['notas'])
    
    respuesta(['Aqui estan las redes sociales: \n\n ~Instagram: https://www.instagram.com/psmmaracaibo?igsh=bXBlOWp4ZHRhMXlh \n\n ~Facebook: https://www.facebook.com/PSMMaracaiboOLD/?locale=es_LA'], ['redes', 'redes sociales', 'red social'], solo_resp=True)
    
    respuesta(['Qué requisitos necesita?', "Cuáles requisitos estas buscando?"], ["necesito", "quiero", "informacion", "información"], requerir_palabra=["requisitos"])
    
    mejor_resp = max(proba_mayor, key=proba_mayor.get)
    return desc() if proba_mayor[mejor_resp] < 1 else mejor_resp

def desc():
    respuesta = ['Lo siento mucho, no sé a qué se refiere, ¿puede decirlo de nuevo?', 'No entiendo su pregunta', 'No entiendo su pregunta'][random.randrange(3)]
    return respuesta

# Función para manejar la entrada del usuario y mostrar la respuesta
def pageweb():
        page = tk.Tk()
        page.title("www.psmmaracaibo.edu.ve")
        page.state('zoomed')
        
        fondoweb = Image.open(r"Web.png")
        fondoweb = ImageTk.PhotoImage(fondoweb)
        stateweb = tk.Canvas(page, width=2000, height=2000, borderwidth=-2)
        stateweb.place(x=0, y=0)
        stateweb.create_image(0, 0, image=fondoweb, anchor='nw')

        chatform = tk.Canvas(page, width=100, height=100, bg='#161616', borderwidth=-2, cursor='hand2')
        chatform.place(x=1270, y=720)
        chatform.create_oval(5, 5, 80, 80, fill='#b7d7e3')

        icon2 = Image.open(r"icon_send2.png")
        icon2 = ImageTk.PhotoImage(icon2)

        icon3 = Image.open(r"maximixar.png")
        icon3 = ImageTk.PhotoImage(icon3)

        icon4 = Image.open(r"chatimage.png")
        icon4 = ImageTk.PhotoImage(icon4)

        icon5 = Image.open(r"maximixar.png")
        icon5 = ImageTk.PhotoImage(icon5)

        chat = tk.Canvas(page, width=55, height=40, bg='#b7d7e3', borderwidth=-2, cursor='hand2')
        chat.place(x=1283, y=742)
        chat.create_image(29, 20, image=icon4)

        def chatbot_mini(event):
            global chatmini
            
            chatmini = tk.Toplevel()
            chatmini.title('Consultoria')
            chatmini.geometry('350x480+1078+341')
            chatmini.focus_force()
            chatmini.resizable(0, 0)
            chatmini.config(bg='#e2e7e3')

            def manejar_entrada(event):
                usuario_input = entry.get().strip()
                respuesta = get_resp(usuario_input)
                resultado_texto.config(state=tk.NORMAL)
                resultado_texto.insert(tk.END, f"\nTú: {usuario_input}\n\nConsultor: {respuesta}\n")
                resultado_texto.config(state=tk.DISABLED)
                entry.delete(0, tk.END)

            def on_entry_click(event):
                if entry.get() == 'Escriba aqui su pregunta...':
                    entry.delete(0, "end")
                    entry.insert(0, '')
                    entry.config(fg='black', font=('Consolas', 8))

            def on_focusout(event):
                if entry.get() == '':
                    entry.insert(0, 'Escriba aqui su pregunta...')
                    entry.config(fg='grey', font=('Consolas', 8))

            marco = tk.Frame(chatmini, width=100, height=60, borderwidth=2, relief='solid', border=-2, bg='#e2e7e3')
            marco.pack(fill='x', expand='true', side='bottom', anchor='s')

            bar_ask = tk.Canvas(marco, width=190, height=50, bg='#e2e7e3', borderwidth=-2)
            bar_ask.place(x=10, y=6)
            bar_ask = round_rectangle(bar_ask, 0, 0, 185, 40, radius=20, fill="#b7d7e3", outline="black")

            entry = tk.Entry(marco, width=120, bg='#b7d7e3', borderwidth=0)
            entry.place(x=14, y=12, width=160, height=25)
            entry.insert(0, 'Escriba aqui su pregunta...')
            entry.bind('<FocusIn>', on_entry_click)
            entry.bind('<FocusOut>', on_focusout)
            entry.bind('<Return>', manejar_entrada)

            resultado_texto = tk.Text(chatmini, height=32, width=78, state=tk.DISABLED, relief='sunken', border=2,)
            resultado_texto.place(x=11, y=60, width=310, height=350)
            
            scrollbary = ttk.Scrollbar(chatmini, orient=tk.VERTICAL, command=resultado_texto.yview)
            resultado_texto.config(yscrollcommand=scrollbary.set)
            scrollbary.place(x=322, y=60, height=350)
            
            buttons = tk.Canvas(marco, width=58, height=50, bg='#e2e7e3', borderwidth=-5)
            buttons.place(x=217, y=5)
            button = round_rectangle(buttons, 0, 0, 50, 40, radius=20, fill="#b7d7e3", outline="black")
            buttons.bind('<Button-1>', manejar_entrada)

            buttons2 = tk.Canvas(marco, width=58, height=50, bg='#e2e7e3', borderwidth=-5)
            buttons2.place(x=290, y=4)
            button = round_rectangle(buttons2, 0, 0, 50, 40, radius=20, fill='#b7d7e3', outline="black")
            buttons2.bind('<Button-1>', )

            icon_buttons = tk.Canvas(marco, bg='#b7d7e3', width=35, height=35, borderwidth=-2, border=-2)
            icon_buttons.place(x=225, y=10)
            icon_buttons.create_image(14, 13, image=icon2)
            icon_buttons.bind('<Button-1>', manejar_entrada)

            icon_buttons2 = tk.Canvas(marco, bg='#b7d7e3', width=35, height=35, borderwidth=-2, border=-2)
            icon_buttons2.place(x=300, y=8)
            icon_buttons2.create_image(14, 15, image=icon5)
            icon_buttons2.bind('<Button-1>', pagemain)
            
            bar = tk.Canvas(chatmini, width=350, height=40, bg='#e2e7e3', border=-2, borderwidth=-2)
            bar.place(x=5, y=10)
            bar1 = round_rectangle(bar, 5,5, 335, 35, radius=20, fill = '#b7d7e3', outline='Black')
            
            text = tk.Canvas(chatmini, width=275, height=21, bg="#b7d7e3", border=-2, borderwidth=-2)
            text.place(x = 45, y=20)
            text.create_text(135,10, text='Pago e inscripción', font=('Consolas', 16))

        chatform.bind('<Button-1>', chatbot_mini)
        chat.bind('<Button-1>', chatbot_mini)
        
        page.mainloop()
    
                  
def pagemain(event = None):
    global chatmini
    
    chatmini.destroy()
    
    global bg_image
     
    def manejar_entrada(event):
        usuario_input = entry.get().strip()
        respuesta = get_resp(usuario_input)
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.insert(tk.END, f"\nTú: {usuario_input}\n\nConsultor: {respuesta}\n")
        resultado_texto.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

    def on_entry_click(event):
        if entry.get() == 'Escriba aqui su pregunta...':
            entry.delete(0, "end")  # delete all the text in the entry
            entry.insert(0, '')  # Insert blank for user input
            entry.config(fg='black', font=('Consolas', 12))

    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, 'Escriba aqui su pregunta...')
            entry.config(fg='grey', font=('Consolas', 12))
    
    rootmain = tk.Toplevel()

    rootmain.title("PSM Maracaibo")
    rootmain.config(bg='#FFFFFF')
    rootmain.iconbitmap(r'images.ico')
    rootmain.state('zoomed')

    try:  
        bg_image = r"fondo.jpg"  # Ajusta la ruta según sea necesario  
        if not os.path.exists(bg_image):  
            raise FileNotFoundError(f"La imagen '{bg_image}' no se encuentra.")  
        
        bg_image = ImageTk.PhotoImage(Image.open(bg_image))  
    except Exception as e:  
        print(f"Error al cargar la imagen: {e}")  
        rootmain.quit()  # Cerrar la aplicación si hay un error  

    canvas = tk.Canvas(rootmain, width=2000, height=2000, borderwidth=-2)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    marco = tk.Frame(rootmain, relief='solid', borderwidth=-2, bg='#FFFFFF')
    marco.pack(fill='y', expand=True)
    marco.config(width=1000, height=720)

    marco2 = tk.Frame(marco, bg='#b7d7e3', width=1000, height=100, borderwidth=-2)
    marco2.place(x=0, y=0)

    marco3 = tk.Frame(marco, bg='#b7d7e3', width=1000, height=100, borderwidth=-2)
    marco3.place(x=0, y=750)

    imagen = Image.open(r"unnamed.png")
    imagen = ImageTk.PhotoImage(imagen)

    logo = tk.Canvas(marco2, width=996, height=100, bg='#b7d7e3', highlightthickness=0)
    logo.place(x=20, y=10)
    logo.create_image(0, 0, anchor='nw', image=imagen)

    info = tk.Canvas(marco2, width=400, height=70, bg='#b7d7e3', borderwidth=-2)
    info.place(x=620, y=25)
    info = round_rectangle(info, 0, 0, 800, 45, radius=20, fill="#e2e7e3", outline="black")

    info_text= tk.Canvas(marco2, width=350, height=30, bg='#e2e7e3', borderwidth=-5)
    info_text.place(x=625, y=33)
    info_text.create_text(180,14, text='Consultoria: Pago e Inscripcion', fill='Black', font=('Consolas', 14))

    marco4 = tk.Frame(marco, bg='#e2e7e3', width=1000, height=100)
    marco4.place(x=0, y=650)

    bar_ask = tk.Canvas(marco4, width=600, height=50, bg='#e2e7e3', borderwidth=-5)
    bar_ask.place(x=166, y=15)
    bar_ask = round_rectangle(bar_ask, 0, 0, 560, 40, radius=20, fill="#b7d7e3", outline="black")

    entry = tk.Entry(marco4, width=55, relief='groove', bg='#b7d7e3', font=('Consolas', 12), borderwidth=0)
    entry.place(x=200, y=25, height=20)
    entry.insert(0, 'Escriba aqui su pregunta...')
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)
    entry.bind('<Return>', manejar_entrada)

    buttons = tk.Canvas(marco4, width=100, height=68, bg='#e2e7e3', borderwidth=-5)
    buttons.place(x=745, y=14)
    button = round_rectangle(buttons, 0, 0, 78, 41, radius=20, fill="#b7d7e3", outline="black")
    buttons.bind('<Button-1>', manejar_entrada )

    image5 = Image.open(r"icon_send.png")
    image5 = ImageTk.PhotoImage(image5)

    send_buttons = tk.Canvas(marco4, width=40, height=40, bg="#b7d7e3", cursor='hand2', borderwidth=-5)
    send_buttons.place(x=766, y=19)
    send_buttons.create_image(14,13, image = image5)
    send_buttons.bind('<Button-1>', manejar_entrada)

    resultado_texto = tk.Text(marco, height=32, width=78, state=tk.DISABLED, relief='sunken', border=4,)
    resultado_texto.place(x=178, y=115)

    scrollbar = ttk.Scrollbar(rootmain, orient=tk.VERTICAL, command=resultado_texto.yview)
    resultado_texto.config(yscrollcommand=scrollbar.set)
    scrollbar.place(x=1035, y=100, height=550)

    retangulo1 = tk.Canvas(marco, bg='#e2e7e3', width=167, height=560, relief='solid', border=-2, borderwidth=-2)
    retangulo1.place(x=0, y=100)
    retangulo1.create_rectangle(0, 10, 0, 10)

    retangulo2 = tk.Canvas(marco, bg='#e2e7e3', width=180, height=560, relief='solid',border=-2, borderwidth=-2)
    retangulo2.place(x=822, y=100)
    retangulo2.create_rectangle(0, 10, 0, 10)

    bar_redes = tk.Canvas(marco3, width=200, height=100, bg='#b7d7e3', borderwidth=-5)
    bar_redes.place(x=20, y=15)
    bar_redes = round_rectangle(bar_redes, 0, 0, 180, 50, radius=20, fill="#e2e7e3", outline="black")

    image2 = Image.open(r'facebook (1).png')
    image2 =ImageTk.PhotoImage(image2)

    facebook = tk.Canvas(marco3, width=45, height=45, cursor='hand2', bg='#e2e7e3', borderwidth=-5)
    facebook.place(x=30, y= 20)
    facebook.create_image(20,20, image = image2)
    facebook.bind('<Button-1>', open_link1)

    image3 = Image.open(r'instagram.png')
    image3 = ImageTk.PhotoImage(image3)

    instagram = tk.Canvas(marco3, width=45, height=45, cursor='hand2', bg='#e2e7e3', borderwidth=-5)
    instagram.place(x=91, y= 20)
    instagram.create_image(20,20, image = image3)
    instagram.bind('<Button-1>', open_link2)

    image4 = Image.open(r'tik-tok.png')
    image4 = ImageTk.PhotoImage(image4)

    tiktok = tk.Canvas(marco3, width=45, height=45, cursor='hand2', bg='#e2e7e3', borderwidth=-5)
    tiktok.place(x=150, y= 20)
    tiktok.create_image(20,20, image = image4)
    tiktok.bind('<Button-1>', open_link3)

    #derechos = tk.Canvas(marco3, width=400, height=200, borderwidth=-5, bg='#00D9D9')
    #derechos.place(x=725, y=8)
    #derechos.create_text(120, 20, text='Derechos de autor por estudiantes\nMarcel Vera y Albert Cuenca', font=('Arial', 9), fill='white' )
    rootmain.mainloop()

pageweb()