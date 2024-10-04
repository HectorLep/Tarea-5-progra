import customtkinter as ctk
from tkinter import ttk
import sys
import os

# Importar las clases necesarias desde la carpeta Clases y Ventanas
from Clases.Asignatura import Asignatura
from Clases.ProgramaAcademico import ProgramaAcademico
from Clases.Persona import Persona  
from Clases.Grupo import Grupo
import Ventanas.util_ventana as util_ventana
from Ventanas.util_ventana import centrar_ventana  
from Ventanas.Ventana_nose import *

class SistemaGestionUniversitaria(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Sistema de Gestión Universitaria")
        self.geometry("1200x700")
        centrar_ventana(self, 1200, 700)  # Para centrar la ventana
        self.config_window()
        self.tabview = ctk.CTkTabview(self, width=600, height=500)
        self.tabview.pack(padx=20, pady=20)

        self.crear_pestanas()
        
    def config_window(self):
        self.iconbitmap('.\Ventanas\gato.ico') 
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)
        
    def crear_pestanas(self):
        # Crear y configurar las pestañas
        self.tab1 = self.tabview.add("Gestión de Estudiantes")
        self.tab2 = self.tabview.add("Gestión de Profesores")
        self.tab3 = self.tabview.add("Gestión de Asignaturas")
        self.tab4 = self.tabview.add("Grupos")

        # Configurar el contenido de cada pestaña
        self.configurar_pestana1()
        self.configurar_pestana2()
        self.configurar_pestana3()
        self.configurar_pestana4()

    def configurar_pestana1(self):
        # Formulario y Treeview para estudiantes
        self.configurar_formulario(self.tab1, "Estudiante", self.ingresar_estudiante)
        self.configurar_treeview(self.tab1, ["Nombre", "Apellido", "Matrícula", "Carrera", "Semestre"])

    def configurar_pestana2(self):
        # Formulario y Treeview para profesores
        self.configurar_formulario(self.tab2, "Profesor", self.ingresar_profesor)
        self.configurar_treeview(self.tab2, ["Nombre", "Apellido", "Número Empleado", "Departamento"])

    def configurar_pestana3(self):
        # Formulario y Treeview para asignaturas
        self.configurar_formulario(self.tab3, "Asignatura", self.ingresar_asignatura)
        self.configurar_treeview(self.tab3, ["Nombre", "Código", "Créditos"])

    def configurar_pestana4(self):
        # Formulario y Treeview para grupos
        self.configurar_formulario(self.tab4, "Grupo", self.ingresar_grupo)
        self.configurar_treeview(self.tab4, ["Nombre", "Número Grupo", "Asignatura"])

    def configurar_formulario(self, tab, tipo, command_func):
        # Formulario genérico basado en el tipo (Estudiante, Profesor, etc.)
        frame_formulario = ctk.CTkFrame(tab)
        frame_formulario.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        label_nombre = ctk.CTkLabel(frame_formulario, text=f"Nombre del {tipo}:")
        label_nombre.pack(pady=5)
        self.entry_nombre = ctk.CTkEntry(frame_formulario)
        self.entry_nombre.pack(pady=5)

        label_apellido = ctk.CTkLabel(frame_formulario, text=f"Apellido del {tipo}:")
        label_apellido.pack(pady=5)
        self.entry_apellido = ctk.CTkEntry(frame_formulario)
        self.entry_apellido.pack(pady=5)

        # Campos adicionales según el tipo
        if tipo == "Estudiante":
            label_matricula = ctk.CTkLabel(frame_formulario, text="Matrícula:")
            label_matricula.pack(pady=5)
            self.entry_matricula = ctk.CTkEntry(frame_formulario)
            self.entry_matricula.pack(pady=5)

            label_carrera = ctk.CTkLabel(frame_formulario, text="Carrera:")
            label_carrera.pack(pady=5)
            self.entry_carrera = ctk.CTkEntry(frame_formulario)
            self.entry_carrera.pack(pady=5)

            label_semestre = ctk.CTkLabel(frame_formulario, text="Semestre:")
            label_semestre.pack(pady=5)
            self.entry_semestre = ctk.CTkEntry(frame_formulario)
            self.entry_semestre.pack(pady=5)

        elif tipo == "Profesor":
            label_num_empleado = ctk.CTkLabel(frame_formulario, text="Número de Empleado:")
            label_num_empleado.pack(pady=5)
            self.entry_num_empleado = ctk.CTkEntry(frame_formulario)
            self.entry_num_empleado.pack(pady=5)

            label_departamento = ctk.CTkLabel(frame_formulario, text="Departamento:")
            label_departamento.pack(pady=5)
            self.entry_departamento = ctk.CTkEntry(frame_formulario)
            self.entry_departamento.pack(pady=5)

        elif tipo == "Asignatura":
            label_codigo = ctk.CTkLabel(frame_formulario, text="Código:")
            label_codigo.pack(pady=5)
            self.entry_codigo = ctk.CTkEntry(frame_formulario)
            self.entry_codigo.pack(pady=5)

            label_creditos = ctk.CTkLabel(frame_formulario, text="Créditos:")
            label_creditos.pack(pady=5)
            self.entry_creditos = ctk.CTkEntry(frame_formulario)
            self.entry_creditos.pack(pady=5)

        elif tipo == "Grupo":
            label_num_grupo = ctk.CTkLabel(frame_formulario, text="Número de Grupo:")
            label_num_grupo.pack(pady=5)
            self.entry_num_grupo = ctk.CTkEntry(frame_formulario)
            self.entry_num_grupo.pack(pady=5)

            label_asignatura = ctk.CTkLabel(frame_formulario, text="Asignatura:")
            label_asignatura.pack(pady=5)
            self.entry_asignatura = ctk.CTkEntry(frame_formulario)
            self.entry_asignatura.pack(pady=5)

        # Botón de ingreso
        boton_ingresar = ctk.CTkButton(frame_formulario, text=f"Ingresar {tipo}", command=command_func)
        boton_ingresar.pack(pady=10)

    def configurar_treeview(self, tab, columnas):
        # Treeview genérico para cada pestaña
        frame_treeview = ctk.CTkFrame(tab)
        frame_treeview.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        tree = ttk.Treeview(frame_treeview, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)
        tree.pack(expand=True, fill="both", padx=10, pady=10)

        boton_eliminar = ctk.CTkButton(frame_treeview, text="Eliminar", fg_color="black", text_color="white")
        boton_eliminar.pack(pady=10)

    # Métodos para ingresar datos
    def ingresar_estudiante(self):
        # Implementar la lógica para agregar un estudiante
        pass

    def ingresar_profesor(self):
        # Implementar la lógica para agregar un profesor
        pass

    def ingresar_asignatura(self):
        # Implementar la lógica para agregar una asignatura
        pass

    def ingresar_grupo(self):
        # Implementar la lógica para agregar un grupo
        pass


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = SistemaGestionUniversitaria()
    app.mainloop()
