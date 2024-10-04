import customtkinter as ctk
from tkinter import ttk
from .ventana_interfaz import New_ventana

class Nose(New_ventana):
    def __init__(self, parent):
        super().__init__(parent,color)
        self.parent = parent
        # Creación de pestañas
        self.tabview = ctk.CTkTabview(self.sub)
        self.tabview.pack(fill='both', expand=True)
        
        # Llamada para crear pestañas y contenido
        self.crear_pestanas()

    def crear_pestanas(self):
        # Crear y configurar las pestañas
        self.tab1 = self.tabview.add("Ingreso de Libros")

        # Configurar el contenido de la pestaña 1
        self.configurar_pestana1()

    def configurar_pestana1(self):
        # Dividir la pestaña en dos frames
        frame_formulario = ctk.CTkFrame(self.tab1)
        frame_formulario.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        frame_treeview = ctk.CTkFrame(self.tab1)
        frame_treeview.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Formulario en el primer frame
        label_nombre = ctk.CTkLabel(frame_formulario, text="Nombre del Libro:")
        label_nombre.pack(pady=5)
        self.entry_nombre = ctk.CTkEntry(frame_formulario)
        self.entry_nombre.pack(pady=5)

        label_autor = ctk.CTkLabel(frame_formulario, text="Autor:")
        label_autor.pack(pady=5)
        self.entry_autor = ctk.CTkEntry(frame_formulario)
        self.entry_autor.pack(pady=5)

        label_categoria = ctk.CTkLabel(frame_formulario, text="Categoría:")
        label_categoria.pack(pady=5)
        self.entry_categoria = ctk.CTkEntry(frame_formulario)
        self.entry_categoria.pack(pady=5)

        label_cantidad = ctk.CTkLabel(frame_formulario, text="Cantidad:")
        label_cantidad.pack(pady=5)
        self.entry_cantidad = ctk.CTkEntry(frame_formulario)
        self.entry_cantidad.pack(pady=5)

        # Botón para ingresar libro
        self.boton_ingresar = ctk.CTkButton(frame_formulario, text="Ingresar Libro", command=self.ingresar_libro)
        self.boton_ingresar.pack(pady=10)

        # Botón para eliminar libro arriba del Treeview
        self.boton_eliminar = ctk.CTkButton(frame_treeview, text="Eliminar Libro", fg_color="black", text_color="white", command=self.eliminar_libro)
        self.boton_eliminar.pack(pady=10)

        # Treeview en el segundo frame
        self.tree = ttk.Treeview(frame_treeview, columns=("Nombre", "Autor", "Categoría", "Cantidad"), show="headings")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Autor", text="Autor")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def ingresar_libro(self):
        # Obtener los datos de los campos de entrada
        nombre = self.entry_nombre.get()
        autor = self.entry_autor.get()
        categoria = self.entry_categoria.get()
        cantidad = self.entry_cantidad.get()

        # Insertar los datos en el Treeview
        self.tree.insert('', 'end', values=(nombre, autor, categoria, cantidad))

        # Limpiar los campos de entrada después de agregar
        self.entry_nombre.delete(0, 'end')
        self.entry_autor.delete(0, 'end')
        self.entry_categoria.delete(0, 'end')
        self.entry_cantidad.delete(0, 'end')

    def eliminar_libro(self):
        # Eliminar el elemento seleccionado del Treeview
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)

