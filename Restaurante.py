import tkinter as tk
from tkinter import messagebox, simpledialog

class Restaurante:
    def __init__(self, master):
        self.master = master
        master.title("Sistema Gestor de Restaurante")

        self.menu = {}  # Diccionario para almacenar el menú

        # Títulos
        self.label = tk.Label(master, text="Gestor de Restaurante", font=("Arial", 16))
        self.label.pack(pady=10)

        # Botones
        self.boton_agregar = tk.Button(master, text="Agregar Platillo", command=self.agregar_platillo)
        self.boton_agregar.pack(pady=5)

        self.boton_actualizar = tk.Button(master, text="Actualizar Platillo", command=self.actualizar_platillo)
        self.boton_actualizar.pack(pady=5)

        self.boton_eliminar = tk.Button(master, text="Eliminar Platillo", command=self.eliminar_platillo)
        self.boton_eliminar.pack(pady=5)

        self.boton_mostrar = tk.Button(master, text="Mostrar Menú", command=self.mostrar_menu)
        self.boton_mostrar.pack(pady=5)

        self.boton_salir = tk.Button(master, text="Salir", command=master.quit)
        self.boton_salir.pack(pady=5)

    def agregar_platillo(self):
        platillo = simpledialog.askstring("Agregar Platillo", "Ingresa el nombre del platillo:")
        precio = simpledialog.askfloat("Agregar Precio", "Ingresa el precio del platillo:")
        
        if platillo and precio is not None:
            if platillo not in self.menu:
                self.menu[platillo] = precio
                messagebox.showinfo("Éxito", f"Platillo '{platillo}' agregado con éxito.")
            else:
                messagebox.showwarning("Advertencia", "El platillo ya existe en el menú.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un nombre y precio válidos.")

    def actualizar_platillo(self):
        platillo = simpledialog.askstring("Actualizar Platillo", "Ingresa el nombre del platillo a actualizar:")
        
        if platillo in self.menu:
            nuevo_precio = simpledialog.askfloat("Actualizar Precio", "Ingresa el nuevo precio del platillo:")
            if nuevo_precio is not None:
                self.menu[platillo] = nuevo_precio
                messagebox.showinfo("Éxito", f"Platillo '{platillo}' actualizado con éxito.")
            else:
                messagebox.showwarning("Advertencia", "Por favor, ingresa un precio válido.")
        else:
            messagebox.showwarning("Error", "El platillo no se encuentra en el menú.")

    def eliminar_platillo(self):
        platillo = simpledialog.askstring("Eliminar Platillo", "Ingresa el nombre del platillo a eliminar:")
        
        if platillo in self.menu:
            del self.menu[platillo]
            messagebox.showinfo("Éxito", f"Platillo '{platillo}' eliminado con éxito.")
        else:
            messagebox.showwarning("Error", "El platillo no se encuentra en el menú.")

    def mostrar_menu(self):
        if self.menu:
            menu_texto = "Menú del Restaurante:\n"
            for platillo, precio in self.menu.items():
                menu_texto += f"{platillo}: ${precio:.2f}\n"
            messagebox.showinfo("Menú", menu_texto)
        else:
            messagebox.showinfo("Menú", "El menú está vacío.")

if __name__ == "__main__":
    root = tk.Tk()
    restaurante_app = Restaurante(root)
    root.mainloop()
