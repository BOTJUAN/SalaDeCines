def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()