import customtkinter as ctk
from tkinter import messagebox, filedialog, END, Text
from PIL import Image, ImageTk
import json

cartelera_pelicula = ""
with open("info_peliculas", "r") as f:
    peliculas = json.load(f)

def eliminar_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def listado_peliculas(frame, menu_administrador, fondo):
    global cartelera_pelicula
    cartelera_pelicula = ""
    eliminar_widgets(frame)
    a = ctk.CTkLabel(frame, text="Catalogo", font=("Arial", 25, "bold"), pady=20)
    a.grid(row=0, column=0)
    menu_admin = ctk.CTkButton(frame, text="Regresar", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command= lambda fondo=fondo: menu_administrador(fondo))
    menu_admin.grid(row=0, column=1)
    for indice_pelicula in range(len(peliculas)):
        ruta = peliculas[indice_pelicula]["ruta"]
        nombre = peliculas[indice_pelicula]["nombre"]
        imagen = ctk.CTkImage(Image.open(ruta), size=(80,100))

        boton = ctk.CTkButton(frame, text=nombre, image=imagen, compound="top",fg_color="transparent", command= lambda indice_pelicula=indice_pelicula, nombre=nombre, frame=frame, ruta=ruta, menu_administrador=menu_administrador, fondo=fondo: info_pelicula(indice_pelicula, nombre, frame, ruta, menu_administrador, fondo))
        frame.grid_columnconfigure(indice_pelicula%2, weight=1)

        boton.grid(row=(indice_pelicula//2)+1, column=indice_pelicula%2)

def eliminar_pelicula(indice_pelicula, frame, m, f):
    messagebox.showinfo("Atencion", f"Se ha eliminado '{peliculas[indice_pelicula]["nombre"]}' exitosamente.")
    peliculas.remove(peliculas[indice_pelicula])
    with open("info_peliculas", "w") as f:
        json.dump(peliculas, f, indent=4)
    listado_peliculas(frame, m, f)


def cargar_imagen():
    global cartelera_pelicula
    cartelera_pelicula = filedialog.askopenfilename(
        filetypes=[
            ("Archivos de imagen JPEG", "*.jpg *.jpeg"),
            ("Archivos de imagen PNG", "*.png"),
            ("Archivos de imagen GIF", "*.gif"),
            ("Todos los archivos", "*.*")
        ]
    )
    cartel_pelicula = ctk.CTkImage(Image.open(cartelera_pelicula))

def confirmar_agregar_pelicula(entry1, entry2, entry3, frame, menu, fondo):
    try:
        salas_pelicula = int(entry3.get())
    except ValueError:
        messagebox.showerror("Atención", "Ha ocurrido un error.")
        return
    if cartelera_pelicula == "" or entry1.get() == "" or entry2.get("1.0", END) == "" or salas_pelicula<=0:
        messagebox.showerror("Atencion", "Ha ocurrido un error.")
        return
    nueva_pelicula = {
        "ruta": cartelera_pelicula,
        "nombre": entry1.get(),
        "sinopsis": entry2.get("1.0", END).strip(),
        "asientos": [[[{"text":"L", "fg_color":"#1f6aa5"} for _ in range(7)] for _ in range(7)] for _ in range(salas_pelicula)]
    }
    peliculas.append(nueva_pelicula)
    with open("info_peliculas", "w") as f:
        json.dump(peliculas, f, indent=4)
    menu(fondo)

def agregar_pelicula(frame, menu_administrador, fondo):
    eliminar_widgets(frame)

    f = ctk.CTkLabel(frame, text="Formulario", font=("Arial", 25, "bold"), pady=20)
    l_titulo = ctk.CTkLabel(frame, text="Ingrese el nombre de la pelicula", font=("Arial", 15, "bold"), pady=20)
    titulo = ctk.CTkEntry(frame)
    l_sinopsis = ctk.CTkLabel(frame, text="Ingrese la sinopsis de la pelicula", font=("Arial", 15, "bold"), pady=20)
    sinopsis = Text(frame,  wrap="word", bg="black", fg="white", font=("Arial", 15), height=6, width=45)
    l_numero_salas = ctk.CTkLabel(frame, text="Ingrese el numero de salas", font=("Arial", 15, "bold"), pady=20)
    numero_salas = ctk.CTkEntry(frame)
    l_cargar_cartelera = ctk.CTkLabel(frame, text="Seleccione la cartelera", font=("Arial", 15, "bold"), pady=20)
    cargar_cartelera = ctk.CTkButton(frame, text="Seleccionar cartelera", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4",command= cargar_imagen)
    confirmar = ctk.CTkButton(frame, text="Agregar pelicula", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command= lambda entry1=titulo, entry2=sinopsis, entry3=numero_salas, frame=frame, menu=menu_administrador, fondo=fondo: confirmar_agregar_pelicula(entry1, entry2, entry3, frame, menu, fondo))
    regresar_menu = ctk.CTkButton(frame, text="Cancelar", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command= lambda fondo=fondo: menu_administrador(fondo) )
    f.pack()
    l_titulo.pack()
    titulo.pack()
    l_sinopsis.pack()
    sinopsis.pack()
    l_numero_salas.pack()
    numero_salas.pack()
    l_cargar_cartelera.pack()
    cargar_cartelera.pack()
    confirmar.pack(pady=15)
    regresar_menu.pack(pady=10)

def guardar_cambios(indice_pelicula, entry_nombre, text_sinopsis, entry_asientos, frame, m, f):
    global cartelera_pelicula
    if cartelera_pelicula == "":
        cartelera_pelicula = peliculas[indice_pelicula]["ruta"]
    try:
        valor = int(entry_asientos.get())
    except ValueError:
        messagebox.showerror("Atención", "Por favor ingrese un valor de tipo entero.")
        return
    nueva_pelicula = {
        "ruta": cartelera_pelicula,
        "nombre": entry_nombre.get(),
        "sinopsis": text_sinopsis.get("1.0", END).strip(),
        "asientos": [[[{"text":"L", "fg_color":"#1f6aa5"} for _ in range(7)] for _ in range(7)]for _ in range(valor)]
    }
    peliculas[indice_pelicula] = nueva_pelicula
    with open("info_peliculas", "w") as f:
        json.dump(peliculas, f, indent=4)
    messagebox.showinfo("Atencion", "La pelicula ha sido editada exitosamente")
    listado_peliculas(frame, m, f)

def editar_peliculas(frame, indice_pelicula, imagen, menu_administrador, fondo):
    eliminar_widgets(frame)

    b = ctk.CTkLabel(frame, text="Editar Pelicula", font=("Arial", 25, "bold"), pady=15)
    c = ctk.CTkLabel(frame, text="Cambiar titulo", font=("Arial", 15, "bold"), pady=15)
    d = ctk.CTkLabel(frame, text="Cambiar sinopsis", font=("Arial", 15, "bold"), pady=15)
    e = ctk.CTkLabel(frame, text="Modificar numero de salas", font=("Arial", 15, "bold"), pady=15)
    cartelera = ctk.CTkButton(frame, image=imagen, text="Seleccionar imagen", fg_color="transparent", hover_color="#a4a4a4", compound="bottom", font=("Arial", 15, "bold"), command=cargar_imagen)
    entry_nombre = ctk.CTkEntry(frame, width=200)
    entry_nombre.delete(0, END)
    entry_nombre.insert(0, peliculas[indice_pelicula]["nombre"])
    text_sinopsis = Text(frame,  wrap="word", bg="black", fg="white", font=("Arial", 15), height=6, width=45)
    text_sinopsis.delete(1.0, END)
    text_sinopsis.insert(1.0, peliculas[indice_pelicula]["sinopsis"])
    entry_asientos = ctk.CTkEntry(frame)
    entry_asientos.delete(0, END)
    entry_asientos.insert(0, len(peliculas[indice_pelicula]["asientos"]))
    confirmar_cambios = ctk.CTkButton(frame, text="Guardar cambios", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command= lambda indice_pelicula=indice_pelicula, entry_nombre=entry_nombre, text_sinopsis=text_sinopsis, entry_asientos=entry_asientos, frame=frame, m=menu_administrador, f=fondo: guardar_cambios(indice_pelicula, entry_nombre, text_sinopsis, entry_asientos, frame, m, f))
    cancelar = ctk.CTkButton(frame, text="Cancelar", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command= lambda frame=frame: listado_peliculas(frame, menu_administrador, fondo))
    b.grid(row=0, column=0)
    cartelera.grid(row=1, column=0)
    c.grid(row=2, column=0)
    entry_nombre.grid(row=3, column=0)
    d.grid(row=4, column=0)
    text_sinopsis.grid(row=5, column=0)
    e.grid(row=6, column=0)
    entry_asientos.grid(row=7, column=0)
    confirmar_cambios.grid(row=8, column=0, pady=10)
    cancelar.grid(row=9, column=0, pady=10)

def eliminar_sala(sala, frame, indice_pelicula, f, m):
    peliculas[indice_pelicula]["asientos"].remove(sala)
    with open("info_peliculas", "w") as f:
        json.dump(peliculas, f, indent=4)
    gestion_salas(frame, m, f)

def añadir_sala(indice_pelicula, frame, m, f):
    nueva_sala = []
    nueva_sala = [[{"text":"L", "fg_color":"#1f6aa5"} for _ in range(7)] for _ in range(7)]
    peliculas[indice_pelicula]["asientos"].append(nueva_sala)
    with open("info_peliculas", "w") as f:
        json.dump(peliculas, f, indent=4)
    gestion_salas(frame, m, f)


def liberar_asientos(sala, aux_sala, indice_sala, indice_pelicula):
    for fila in range(len(sala)):
        for colum in range(len(sala[fila])):
            if sala[fila][colum]["text"] == "O":
                aux_sala[fila][colum].configure(text="L", fg_color="#1f6aa5")
                sala[fila][colum]["text"] = "L"
                sala[fila][colum]["fg_color"] = "#1f6aa5"
    peliculas[indice_pelicula]["asientos"][indice_sala] = sala
    with open("info_peliculas", "w") as f:
        json.dump(peliculas, f, indent=4)


def informacion_sala(sala, frame, indice_sala, indice_pelicula, f, m):
    eliminar_widgets(frame)
    aux_sala = []
    aux_sala = [[ctk.CTkButton(frame, text=bton["text"], fg_color=bton["fg_color"], width=40, height=20)for _, bton in enumerate(fila)] for _, fila in enumerate(sala)]
    for f, fila in  enumerate(aux_sala):
        for c, boton in enumerate(fila):
            boton.grid(row=f, column=c, padx=10, pady=5)

    eliminar = ctk.CTkButton(frame, text="Eliminar sala", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command=lambda sala=sala, frame=frame, indice_pelicula=indice_pelicula, f=f, m=m: eliminar_sala(sala, frame, indice_pelicula, f, m))
    liberar = ctk.CTkButton(frame, text="Liberar asientos", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command=lambda sala=sala, aux_sala=aux_sala, indice_sala=indice_sala, indice_pelicula=indice_pelicula: liberar_asientos(sala, aux_sala, indice_sala, indice_pelicula))
    salir = ctk.CTkButton(frame, text="Salir", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command= lambda frame=frame, m=m, f=f: gestion_salas(frame, m, f))
    eliminar.grid(row=7, column=2, columnspan=3, pady=5)
    liberar.grid(row=8, column=2, columnspan=3, pady=5)
    salir.grid(row=9, column=2, columnspan=3, pady=5)

def gestion_salas(frame, menu_administrador, fondo):
    eliminar_widgets(frame)
    l_s = ctk.CTkLabel(frame, text="Gestion de salas", font=("Arial", 25, "bold"), pady=20)
    boton_salir = ctk.CTkButton(frame, text="Salir", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command= lambda fondo=fondo: menu_administrador(fondo))
    l_s.pack()
    boton_salir.pack(pady=10)
    for indice in range(len(peliculas)):
        pelicula_actual = peliculas[indice]
        ruta = pelicula_actual["ruta"]
        nombre = pelicula_actual["nombre"]
        salas_disponibles = pelicula_actual["asientos"]
        cartelera = ctk.CTkImage(Image.open(ruta), size=(120,140))
        pelicula = ctk.CTkButton(frame, image=cartelera, fg_color="transparent", text=nombre, compound="top", font=("Arial", 15, "bold"))
        pelicula.pack()
        añadir = ctk.CTkButton(frame, text="Añadir sala", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command= lambda indice_pelicula=indice, frame=frame, m=menu_administrador, f=fondo: añadir_sala(indice_pelicula, frame, m, f))
        
        for i in range(len(salas_disponibles)):
            sala_actual = salas_disponibles[i]
            boton_sala = ctk.CTkButton(frame, text=f"Sala {i+1}", fg_color="transparent", hover_color="#a4a4a4", command= lambda sala=sala_actual, frame=frame, indice_sala=i, indice_pelicula=indice, f=fondo, m=menu_administrador: informacion_sala(sala, frame, indice_sala, indice_pelicula, f, m))
            boton_sala.pack()
        añadir.pack(pady=10)

def info_pelicula(indice_pelicula, nombre, frame, ruta, menu_administrador, fondo):
    eliminar_widgets(frame)
    sinopsis = peliculas[indice_pelicula]["sinopsis"]
    no_salas = len(peliculas[indice_pelicula]["asientos"])

    titulo = ctk.CTkLabel(frame, text=nombre, font=("Arial", 25 ,"bold"), pady=20)
    imagen_redimensionada = ctk.CTkImage(Image.open(ruta), size=(200, 220))
    cartelera = ctk.CTkLabel(frame, image=imagen_redimensionada, text="")
    sinopsis = ctk.CTkLabel(frame, text=sinopsis, wraplength=350, font=("Arial", 15), pady=20)
    salas = ctk.CTkLabel(frame, text=f"Salas disponibles: {no_salas}", font=("Arial", 20 ,"bold"))
    boton_eliminar = ctk.CTkButton(frame, text="Eliminar pelicula", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command= lambda indice_pelicula=indice_pelicula, frame=frame, m=menu_administrador, f=fondo: eliminar_pelicula(indice_pelicula, frame, m, f))
    boton_editar = ctk.CTkButton(frame, text="Editar informacion", fg_color="#50BC30", text_color="black", hover_color="#a4a4a4", command= lambda frame=frame, indice_pelicula=indice_pelicula, imagen=imagen_redimensionada, menu_administrador=menu_administrador, fondo=fondo: editar_peliculas(frame, indice_pelicula, imagen, menu_administrador, fondo))

    titulo.grid(row=0, column=0)
    cartelera.grid(row=1, column=0)
    sinopsis.grid(row=2, column=0)
    salas.grid(row=3, column=0)
    boton_eliminar.grid(row=4, column=0, pady=10)
    boton_editar.grid(row=5, column=0, pady=10)







