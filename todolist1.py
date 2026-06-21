import tkinter as tk
from tkinter import messagebox


def agregar_tarea():
    
    tarea = entrada_tarea.get() 
    
    if tarea != "": 
        lista_tareas.insert(tk.END, tarea)
        
        entrada_tarea.delete(0, tk.END) 
    else:
        
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def eliminar_tarea():
    try:
        
        indice_seleccionado = lista_tareas.curselection()[0]
        
        lista_tareas.delete(indice_seleccionado)
    except IndexError:
        
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")



ventana = tk.Tk()
ventana.title("Mi Lista de Tareas")
ventana.geometry("300x400") 




entrada_tarea = tk.Entry(ventana, font=("Arial", 12))
entrada_tarea.pack(pady=10, padx=10, fill=tk.X)

boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

lista_tareas = tk.Listbox(ventana, font=("Arial", 12), selectbackground="#a6a6a6")
lista_tareas.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)


boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

ventana.mainloop()