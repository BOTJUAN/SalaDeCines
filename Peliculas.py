import customtkinter as ctk
from PIL import Image, ImageTk
import json
from ModificarSalas import seleccionar_asiento, asiento_recomendado, reservar_asientos

with open("info_peliculas", "r") as f:
    peliculas = json.load(f)

def cargar_posters(frame):
    for i in range(len(peliculas)):
        pelicula = peliculas[i]
        ruta_imagen = pelicula["ruta"]
        fila = (i//4)*2
        columna = i%4
        imagen_tk = ctk.CTkImage(Image.open(ruta_imagen), size=(180,200))

        boton_cartelera = ctk.CTkButton(frame, text=pelicula["nombre"], fg_color="transparent", hover_color="#1a1a4a", image=imagen_tk, compound="top", command=lambda frame=frame, indice=i: mostrar_info_pelicula(frame, indice))
        boton_cartelera.grid(row=fila, column=columna, padx=5)

def mostrar_info_pelicula(frame,indice_pelicula):
    limpiar_ventana(frame)
    pelicula = peliculas[indice_pelicula]
    for j in range(len(pelicula["asientos"])):
        boton = ctk.CTkButton(frame, text=f"Sala {j+1}", command= lambda frame=frame, indice_pelicula=indice_pelicula, indice_sala=j: mostrar_matrices(frame, indice_pelicula, indice_sala))
        boton.grid(row=(j//2)+5, column=j%2, pady=10)

    imagen_tk = ctk.CTkImage(Image.open(pelicula["ruta"]), size=(380,400))
    poster = ctk.CTkLabel(frame, image=imagen_tk, text="")
    # Boton para regresar al catalogo de peliculas
    boton_regresar = ctk.CTkButton(frame, text="Regresar al catalogo", command= lambda frame= frame: regresar_catalogo(frame))
    boton_regresar.grid(row=3, column=0, columnspan=4, pady=10)

    # Insertar informacion acerca de la pelicula
    info_peli = ctk.CTkLabel(frame, text=pelicula["sinopsis"], wraplength=350, fg_color="transparent", font=("Arial", 20))
    titulo_peli = ctk.CTkLabel(frame, text=pelicula["nombre"], fg_color="transparent", font=("Arial", 25, "bold"))

    poster.grid(row=1, column=0)
    titulo_peli.grid(row=0, column=0, columnspan=4)
    info_peli.grid(row=1, column=1)

def regresar_catalogo(frame):
    limpiar_ventana(frame)
    cargar_posters(frame)

def mostrar_matrices(frame, indice_pelicula, indice_sala):
    limpiar_ventana(frame)
    sala = peliculas[indice_pelicula]["asientos"][indice_sala]
    aux_botones = []
    aux_botones = [[ctk.CTkButton(frame, text=cell["text"], fg_color=cell["fg_color"], width=100)for _, cell in enumerate(fila)] for _, fila in enumerate(sala)]
    for f, fila in  enumerate(aux_botones):
        for c, boton in enumerate(fila):
            boton.grid(row=f, column=c, padx=5, pady=5)
    
    salir_sala = ctk.CTkButton(frame, text="Regresar a la pelicula", command= lambda frame=frame, indice_pelicula=indice_pelicula: regresar_pelicula(frame, indice_pelicula))
    salir_sala.grid(row=9, column=0, columnspan=7)

    label_fila = ctk.CTkLabel(frame, text="Fila:", pady=10, fg_color="transparent")
    label_fila.grid(row=10, column=0)
    entry_fila = ctk.CTkEntry(frame)
    entry_fila.grid(row=10, column=1, columnspan=2)

    label_columna = ctk.CTkLabel(frame, text="Columna:", pady=10, fg_color="transparent")
    label_columna.grid(row=12, column=0)
    entry_columna = ctk.CTkEntry(frame)
    entry_columna.grid(row=12, column=1, columnspan=2)

    seleccionar = ctk.CTkButton(frame, text="Seleccionar aiento", command= lambda boton_fila=entry_fila, boton_columna=entry_columna, aux_botones=aux_botones, sala=sala: seleccionar_asiento(entry_fila, entry_columna, aux_botones, sala))
    seleccionar.grid(row=13, column=0, columnspan=2, pady=10)

    recomendar = ctk.CTkButton(frame, text="Reservar mejor asiento", command= lambda sala=sala, aux_botones=aux_botones: asiento_recomendado(sala, aux_botones))
    recomendar.grid(row=14, column=0, columnspan=2, pady=10)

    reservar = ctk.CTkButton(frame, text="Confirmar reserva", command= lambda sala=sala, indice_pelicula=indice_pelicula, indice_sala=indice_sala, aux_botones=aux_botones: reservar_asientos(sala, indice_pelicula, indice_sala, aux_botones))
    reservar.grid(row=14, column=2, columnspan=2, padx=10)

def regresar_pelicula(frame, indice_pelicula):
    limpiar_ventana(frame)
    mostrar_info_pelicula(frame, indice_pelicula)

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.grid_forget()
