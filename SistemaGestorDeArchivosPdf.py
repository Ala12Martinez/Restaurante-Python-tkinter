import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, ttk

class GestorDocumentos:
    def __init__(self, master):
        self.master = master
        master.title("Sistema Gestor de Documentos")
        master.geometry("600x450")
        master.config(bg="#eaeaea")

        self.documentos = []  # Lista para almacenar los nombres de los documentos

        # Títulos
        self.label = tk.Label(master, text="Sistema Gestor de Documentos", font=("Helvetica", 18, 'bold'), bg="#eaeaea")
        self.label.pack(pady=10)

        # Frame para botones
        self.frame_botones = tk.Frame(master, bg="#eaeaea")
        self.frame_botones.pack(pady=10)

        # Botones
        self.boton_subir = ttk.Button(self.frame_botones, text="Subir Documento", command=self.subir_documento)
        self.boton_subir.grid(row=0, column=0, padx=5)

        self.boton_mostrar = ttk.Button(self.frame_botones, text="Mostrar Documentos", command=self.mostrar_documentos)
        self.boton_mostrar.grid(row=0, column=1, padx=5)

        self.boton_actualizar = ttk.Button(self.frame_botones, text="Actualizar Documento", command=self.actualizar_documento)
        self.boton_actualizar.grid(row=0, column=2, padx=5)

        self.boton_eliminar = ttk.Button(self.frame_botones, text="Eliminar Documento", command=self.eliminar_documento)
        self.boton_eliminar.grid(row=0, column=3, padx=5)

        self.boton_salir = ttk.Button(self.frame_botones, text="Salir", command=master.quit)
        self.boton_salir.grid(row=0, column=4, padx=5)

        # Lista de documentos
        self.lista_documentos = tk.Listbox(master, width=70, height=15, font=("Helvetica", 12))
        self.lista_documentos.pack(pady=20)

    def subir_documento(self):
        archivo = filedialog.askopenfilename(title="Seleccionar Documento",
                                              filetypes=(("Archivos PDF", "*.pdf"),
                                                         ("Archivos de Texto", "*.txt"),
                                                         ("Todos los archivos", "*.*")))
        if archivo:
            nombre_archivo = archivo.split('/')[-1]  # Obtener solo el nombre del archivo
            if nombre_archivo not in self.documentos:  # Verificar duplicados
                self.documentos.append(nombre_archivo)  # Agregar el nombre del archivo a la lista
                self.lista_documentos.insert(tk.END, nombre_archivo)  # Mostrar en la lista
                messagebox.showinfo("Éxito", f"Documento '{nombre_archivo}' subido con éxito.")
            else:
                messagebox.showwarning("Advertencia", "El documento ya ha sido subido.")
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún documento.")

    def mostrar_documentos(self):
        if self.documentos:
            documentos_texto = "Documentos Subidos:\n" + "\n".join(self.documentos)
            messagebox.showinfo("Lista de Documentos", documentos_texto)
        else:
            messagebox.showinfo("Lista de Documentos", "No se han subido documentos.")

    def actualizar_documento(self):
        try:
            seleccionado = self.lista_documentos.curselection()[0]  # Obtener el índice del elemento seleccionado
            nombre_documento = self.lista_documentos.get(seleccionado)
            nuevo_archivo = filedialog.askopenfilename(title="Seleccionar Nuevo Documento",
                                                        filetypes=(("Archivos PDF", "*.pdf"),
                                                                   ("Archivos de Texto", "*.txt"),
                                                                   ("Todos los archivos", "*.*")))
            if nuevo_archivo:
                nuevo_nombre = nuevo_archivo.split('/')[-1]  # Obtener el nuevo nombre del archivo
                # Reemplazar el documento en la lista
                self.documentos[seleccionado] = nuevo_nombre
                self.lista_documentos.delete(seleccionado)  # Eliminar el antiguo de la lista visual
                self.lista_documentos.insert(seleccionado, nuevo_nombre)  # Agregar el nuevo nombre
                messagebox.showinfo("Éxito", f"Documento actualizado de '{nombre_documento}' a '{nuevo_nombre}'.")
            else:
                messagebox.showwarning("Advertencia", "No se seleccionó ningún nuevo documento.")
        except IndexError:
            messagebox.showwarning("Error", "Por favor, selecciona un documento para actualizar.")

    def eliminar_documento(self):
        try:
            seleccionado = self.lista_documentos.curselection()[0]  # Obtener el índice del elemento seleccionado
            nombre_documento = self.lista_documentos.get(seleccionado)
            self.documentos.remove(nombre_documento)  # Eliminar de la lista
            self.lista_documentos.delete(seleccionado)  # Eliminar de la lista visual
            messagebox.showinfo("Éxito", f"Documento '{nombre_documento}' eliminado con éxito.")
        except IndexError:
            messagebox.showwarning("Error", "Por favor, selecciona un documento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    gestor_app = GestorDocumentos(root)
    root.mainloop()
