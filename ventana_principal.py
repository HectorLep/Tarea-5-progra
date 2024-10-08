import customtkinter as ctk
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
import sys
import os
import re

# Importar las clases necesarias desde la carpeta Clases y Ventanas
from Clases.Asignatura import Asignatura
from Clases.ProgramaAcademico import ProgramaAcademico
from Clases.Persona import Persona  
from Clases.Persona import *
from Clases.Grupo import Grupo
import Ventanas.util_ventana as util_ventana
from Ventanas.util_ventana import centrar_ventana  
from Ventanas.Ventana_nose import *

class SistemaGestionUniversitaria(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.entries = {}  
        # Configuración de la ventana principal
        self.title("Sistema de Gestión Universitaria")
        self.geometry("1600x900")
        centrar_ventana(self, 1600, 900)
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
        self.configurar_treeview(self.tab1, ["Nombre", "Apellido","Fecha nacimiento" ,"Matrícula", "Carrera", "Semestre"])

    def configurar_pestana2(self):
        # Formulario y Treeview para profesores
        self.configurar_formulario(self.tab2, "Profesor", self.ingresar_profesor)
        self.configurar_treeview(self.tab2, ["Nombre", "Apellido","Fecha nacimiento" ,"Número Empleado", "Departamento"])

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
        
        # Condición especial para la asignatura
        if tipo == "Asignatura":
            label_nombre = ctk.CTkLabel(frame_formulario, text=f"Nombre de la {tipo}:")
        else:
            label_nombre = ctk.CTkLabel(frame_formulario, text=f"Nombre del {tipo}:")
            
        label_nombre.pack(pady=4)
        entry_nombre = ctk.CTkEntry(frame_formulario)
        entry_nombre.pack(pady=4)

        self.entries[tipo] = {"nombre": entry_nombre,}
        
        # Solo mostrar "Apellido" para Estudiante y Profesor
        if tipo in ["Estudiante", "Profesor"]:
            label_apellido = ctk.CTkLabel(frame_formulario, text=f"Apellido del {tipo}:")
            label_apellido.pack(pady=4)
            entry_apellido = ctk.CTkEntry(frame_formulario)
            entry_apellido.pack(pady=4)

            # Agregar apellido al diccionario de entries
            self.entries[tipo]["apellido"] = entry_apellido

        # Campos adicionales según el tipo
        if tipo == "Estudiante":
            label_fecha_nacimiento = ctk.CTkLabel(frame_formulario, text="Fecha de Nacimiento:")
            label_fecha_nacimiento.pack(pady=4)
            self.entry_fecha_nacimiento = ctk.CTkEntry(frame_formulario)
            self.entry_fecha_nacimiento.pack(pady=4)
            
            label_matricula = ctk.CTkLabel(frame_formulario, text="Matrícula:")
            label_matricula.pack(pady=5)
            self.entry_matricula = ctk.CTkEntry(frame_formulario)
            self.entry_matricula.pack(pady=4)

            label_carrera = ctk.CTkLabel(frame_formulario, text="Carrera:")
            label_carrera.pack(pady=4)
            self.entry_carrera = ctk.CTkEntry(frame_formulario)
            self.entry_carrera.pack(pady=4)

            label_semestre = ctk.CTkLabel(frame_formulario, text="Semestre:")
            label_semestre.pack(pady=4)
            self.entry_semestre = ctk.CTkEntry(frame_formulario)
            self.entry_semestre.pack(pady=4)

        elif tipo == "Profesor":
            label_fecha_nacimiento_p = ctk.CTkLabel(frame_formulario, text="Fecha de Nacimiento:")
            label_fecha_nacimiento_p.pack(pady=5)
            self.entry_fecha_nacimiento_p = ctk.CTkEntry(frame_formulario)
            self.entry_fecha_nacimiento_p.pack(pady=5)
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
        
    def validar_no_vacio(self, *campos):
        for campo in campos:
            if not campo.strip(): 
                CTkMessagebox(title="Error de Validación", message="Todos los campos deben estar llenos.", icon="warning")
                return False
        return True
    def validar_str(self, texto):
        if re.match(r"^[A-Za-z\s]+$", texto):
            return True
        else:
            CTkMessagebox(title="Error de Validación", message="Este campo solo debe contener letras y espacios.", icon="warning")
            return False
    def validar_fechas(self, fecha):
        if re.match(r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$", fecha):
            return True
        else:
            CTkMessagebox(title="Error de Validación", message="La fecha debe contener el formato dd/mm/yyyy.", icon="warning")
            return False
    def validar_matricula(self, matricula):
        if re.match(r"^[A-Za-z][A-Za-z0-9]{4,}$", matricula):
            return True
        else:
            CTkMessagebox(title="Error de Validación", message="La matrícula debe comenzar con una letra y contener al menos 5 caracteres alfanuméricos.", icon="warning")
            return False
        
    def configurar_treeview(self, tab, columnas):
        # Treeview genérico para cada pestaña
        frame_treeview = ctk.CTkFrame(tab)
        frame_treeview.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        tree = ttk.Treeview(frame_treeview, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=110, anchor="center")
        tree.pack(expand=True, fill="both", padx=10, pady=10)

        boton_eliminar = ctk.CTkButton(frame_treeview, text="Eliminar", fg_color="black", text_color="white")
        boton_eliminar.pack(pady=10)

    def ingresar_estudiante(self):
        nombre = self.entries["Estudiante"]["nombre"].get()
        apellido = self.entries["Estudiante"]["apellido"].get()
        fecha_nacimiento = self.entry_fecha_nacimiento.get()
        matricula = self.entry_matricula.get()
        carrera = self.entry_carrera.get()
        semestre = self.entry_semestre.get()
        
        # Verificar que no haya campos vacíos
        if not self.validar_no_vacio(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre):
            return
        # Validar que el nombre, apellido y carrera solo contengan letras y espacios
        if not self.validar_str(nombre):
            return
        if not self.validar_str(apellido):
            return
        if not self.validar_str(carrera):
            return
        if not self.validar_matricula(matricula):
            return
        if not self.validar_fechas(fecha_nacimiento):
            return

        # Crear un objeto Estudiante con los datos ingresados
        estudiante = Estudiante(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre)

        # Agregar los datos del estudiante al Treeview
        tree = self.tab1.winfo_children()[1].winfo_children()[0]  # Acceder al Treeview
        tree.insert("", "end", values=(estudiante.nombre, estudiante.apellido, estudiante.fecha_de_nacimiento, estudiante.matricula, estudiante.carrera, estudiante.semestre))

    def ingresar_profesor(self):
        nombre = self.entries["Profesor"]["nombre"].get()
        apellido = self.entries["Profesor"]["apellido"].get()
        fecha_nacimiento = self.entry_fecha_nacimiento_p.get()
        n_empleado = self.entry_num_empleado.get()
        departamento = self.entry_departamento.get()
        
        # Verificar que no haya campos vacíos
        if not self.validar_no_vacio(nombre, apellido, fecha_nacimiento, n_empleado, departamento):
            return
        # Validar que el nombre, apellido y departamento solo contengan letras y espacios
        if not self.validar_str(nombre):
            return
        if not self.validar_str(apellido):
            return
        if not self.validar_str(departamento):
            return
        try:
            n_empleado = int(n_empleado)
        except ValueError: 
            CTkMessagebox(title="Error de Validación", message="El número de empleado debe ser un número entero.", icon="warning")
            return
        if not self.validar_fechas(fecha_nacimiento):
            return

        # Crear un objeto Profesor con los datos ingresados
        profesor = Profesor(nombre, apellido, fecha_nacimiento, n_empleado, departamento)

        # Agregar los datos del profesor al Treeview
        tree = self.tab2.winfo_children()[1].winfo_children()[0]
        tree.insert("", "end", values=(profesor.nombre, profesor.apellido, profesor.fecha_de_nacimiento, profesor.n_empleado, profesor.departamento))

    def ingresar_asignatura(self):
        nombre = self.entries["Asignatura"]["nombre"].get()
        codigo = self.entry_codigo.get()
        creditos = self.entry_creditos.get()
        
        # Verificar que no haya campos vacíos
        if not self.validar_no_vacio(nombre, codigo, creditos):
            return

        
        asignatura = Asignatura(nombre, codigo, creditos)
        tree = self.tab3.winfo_children()[1].winfo_children()[0]
        tree.insert("", "end", values=(asignatura.nombre, asignatura.codigo, asignatura.creditos))

    def ingresar_grupo(self):
        nombre = self.entries["Grupo"]["nombre"].get()
        num_grupo = self.entry_num_grupo.get()
        asignatura = self.entry_asignatura.get()
        
        # Verificar que no haya campos vacíos
        if not self.validar_no_vacio(nombre, num_grupo, asignatura):
            return
        
        grupo = Grupo(nombre, num_grupo, asignatura)
        tree = self.tab4.winfo_children()[1].winfo_children()[0]
        tree.insert("", "end", values=(grupo.nombre, grupo.num_grupo, grupo.asignatura))

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = SistemaGestionUniversitaria()
    app.mainloop()
