import customtkinter as ctk
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
import re

# Importar clases necesarias
from Clases.Persona import *
from Clases.Asignatura import Asignatura
from Clases.Grupo import Grupo
from Clases.ProgramaAcademico import ProgramaAcademico
import Ventanas.util_ventana as util_ventana

class SistemaGestionUniversitaria(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.entries = {}
        self.title("Sistema de Gestión Universitaria")
        self.geometry("1600x900")
        util_ventana.centrar_ventana(self, 1600, 900)
        self.config_window()
        self.tabview = ctk.CTkTabview(self, width=600, height=500)
        self.tabview.pack(padx=20, pady=20)
        self.crear_pestanas()
        
        # Inicializar listas para almacenar objetos
        self.estudiantes = []
        self.profesores = []
        self.asignaturas = []
        self.grupos = []
        self.programas_academicos = []

    def config_window(self):
        self.iconbitmap('.\Ventanas\gato.ico')
        util_ventana.centrar_ventana(self, 1024, 600)

    def crear_pestanas(self):
        self.tab1 = self.tabview.add("Gestión de Estudiantes")
        self.tab2 = self.tabview.add("Gestión de Profesores")
        self.tab3 = self.tabview.add("Gestión de Asignaturas")
        self.tab4 = self.tabview.add("Grupos")
        self.tab5 = self.tabview.add("Programas Académicos")

        self.configurar_pestana1()
        self.configurar_pestana2()
        self.configurar_pestana3()
        self.configurar_pestana4()
        self.configurar_pestana5()

    def configurar_pestana1(self):
        self.configurar_formulario(self.tab1, "Estudiante", self.ingresar_estudiante)
        self.tree_estudiantes = self.configurar_treeview(self.tab1, ["Nombre", "Apellido", "Fecha nacimiento", "Matrícula", "Carrera", "Semestre"])

    def configurar_pestana2(self):
        self.configurar_formulario(self.tab2, "Profesor", self.ingresar_profesor)
        self.tree_profesores = self.configurar_treeview(self.tab2, ["Nombre", "Apellido", "Fecha nacimiento", "Número Empleado", "Departamento"])

    def configurar_pestana3(self):
        self.configurar_formulario(self.tab3, "Asignatura", self.ingresar_asignatura)
        self.tree_asignaturas = self.configurar_treeview(self.tab3, ["Nombre", "Código", "Créditos"])

    def configurar_pestana4(self):
        self.configurar_formulario(self.tab4, "Grupo", self.ingresar_grupo)
        self.tree_grupos = self.configurar_treeview(self.tab4, ["Nombre", "Número Grupo", "Asignatura", "Estudiante"])

    def configurar_pestana5(self):
        self.configurar_formulario(self.tab5, "Programa Académico", self.ingresar_programa_academico)
        self.tree_programas = self.configurar_treeview(self.tab5, ["Nombre", "Código"])

    def configurar_formulario(self, tab, tipo, command_func):
        frame_formulario = ctk.CTkFrame(tab)
        frame_formulario.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        if tipo == "Asignatura":
            label_nombre = ctk.CTkLabel(frame_formulario, text=f"Nombre de la {tipo}:")
        else:
            label_nombre = ctk.CTkLabel(frame_formulario, text=f"Nombre del {tipo}:")
            
        label_nombre.pack(pady=4)
        entry_nombre = ctk.CTkEntry(frame_formulario)
        entry_nombre.pack(pady=4)
        self.entries[tipo] = {"nombre": entry_nombre}

        if tipo in ["Estudiante", "Profesor"]:
            label_apellido = ctk.CTkLabel(frame_formulario, text=f"Apellido del {tipo}:")
            label_apellido.pack(pady=4)
            entry_apellido = ctk.CTkEntry(frame_formulario)
            entry_apellido.pack(pady=4)
            self.entries[tipo]["apellido"] = entry_apellido

        # Campos adicionales para Estudiante, Profesor, Asignatura, Grupo y Programa Académico
        if tipo == "Estudiante":
            self._crear_campos_estudiante(frame_formulario)
        elif tipo == "Profesor":
            self._crear_campos_profesor(frame_formulario)
        elif tipo == "Asignatura":
            self._crear_campos_asignatura(frame_formulario)
        elif tipo == "Grupo":
            self._crear_campos_grupo(frame_formulario)
        elif tipo == "Programa Académico":
            self._crear_campos_programa_academico(frame_formulario)

        boton_ingresar = ctk.CTkButton(frame_formulario, text=f"Ingresar {tipo}", command=command_func)
        boton_ingresar.pack(pady=10)

    def _crear_campos_estudiante(self, frame):
        labels_text = ["Fecha de Nacimiento:", "Matrícula:", "Carrera:", "Semestre:"]
        self.entry_fecha_nacimiento = self._crear_entry(frame, labels_text[0])
        self.entry_matricula = self._crear_entry(frame, labels_text[1])
        self.entry_carrera = self._crear_entry(frame, labels_text[2])
        self.entry_semestre = self._crear_entry(frame, labels_text[3])

    def _crear_campos_profesor(self, frame):
        labels_text = ["Fecha de Nacimiento:", "Número de Empleado:", "Departamento:"]
        self.entry_fecha_nacimiento_p = self._crear_entry(frame, labels_text[0])
        self.entry_num_empleado = self._crear_entry(frame, labels_text[1])
        self.entry_departamento = self._crear_entry(frame, labels_text[2])

    def _crear_campos_asignatura(self, frame):
        labels_text = ["Código:", "Créditos:"]
        self.entry_codigo = self._crear_entry(frame, labels_text[0])
        self.entry_creditos = self._crear_entry(frame, labels_text[1])

    def _crear_campos_grupo(self, frame):
        labels_text = ["Número de Grupo:", "Asignatura:", "Estudiante:"]
        self.entry_num_grupo = self._crear_entry(frame, labels_text[0])
        self.entry_asignatura = self._crear_entry(frame, labels_text[1])
        self.entry_estudiante = self._crear_entry(frame, labels_text[2])

    def _crear_campos_programa_academico(self, frame):
        labels_text = ["Código:"]
        self.entry_codigo_programa = self._crear_entry(frame, labels_text[0])

    def _crear_entry(self, frame, label_text):
        label = ctk.CTkLabel(frame, text=label_text)
        label.pack(pady=4)
        entry = ctk.CTkEntry(frame)
        entry.pack(pady=4)
        return entry

    def configurar_treeview(self, tab, columnas):
        frame_treeview = ctk.CTkFrame(tab)
        frame_treeview.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        tree = ttk.Treeview(frame_treeview, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=110, anchor="center")
        tree.pack(expand=True, fill="both", padx=10, pady=10)

        boton_eliminar = ctk.CTkButton(frame_treeview, text="Eliminar", fg_color="black", text_color="white", command=lambda: self.eliminar_elemento(tree))
        boton_eliminar.pack(pady=10)

        return tree
    def eliminar_elemento(self, tree):
        # Obtener el elemento seleccionado en el Treeview
        seleccionado = tree.selection()
        if not seleccionado:
            CTkMessagebox(title="Error", message="Debe seleccionar un elemento para eliminar.", icon="warning")
            return

        # Obtener los valores del elemento seleccionado
        valores = tree.item(seleccionado, 'values')
        
        # Determinar qué tipo de objeto es para eliminar de la lista correspondiente
        if tree == self.tree_estudiantes:
            matricula = valores[3]  # La matrícula está en la posición 3 de la fila
            self.estudiantes = [e for e in self.estudiantes if e.matricula != matricula]
            print(f"Estudiante con matrícula {matricula} eliminado.")
        elif tree == self.tree_profesores:
            num_empleado = valores[3]  # El número de empleado está en la posición 3 de la fila
            self.profesores = [p for p in self.profesores if p.numero_empleado != num_empleado]
            print(f"Profesor con número de empleado {num_empleado} eliminado.")
        elif tree == self.tree_asignaturas:
            codigo = valores[1]  # El código de la asignatura está en la posición 1 de la fila
            self.asignaturas = [a for a in self.asignaturas if a.codigo != codigo]
            print(f"Asignatura con código {codigo} eliminada.")
        elif tree == self.tree_grupos:
            num_grupo = valores[1]  # El número de grupo está en la posición 1 de la fila
            self.grupos = [g for g in self.grupos if g.numero_grupo != num_grupo]
            print(f"Grupo número {num_grupo} eliminado.")
        elif tree == self.tree_programas:
            codigo = valores[1]  # El código del programa está en la posición 1 de la fila
            self.programas_academicos = [p for p in self.programas_academicos if p.codigo != codigo]
            print(f"Programa académico con código {codigo} eliminado.")

        # Eliminar el elemento del Treeview
        tree.delete(seleccionado)
        CTkMessagebox(title="Éxito", message="Elemento eliminado correctamente.", icon="info")

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
        
    def es_duplicado(self, tree, valores):
        for item in tree.get_children():
            if tree.item(item, 'values') == valores:
                return True
        return False
    
    def ingresar_estudiante(self):
        nombre = self.entries["Estudiante"]["nombre"].get()
        apellido = self.entries["Estudiante"]["apellido"].get()
        fecha_nacimiento = self.entry_fecha_nacimiento.get()
        matricula = self.entry_matricula.get()
        carrera = self.entry_carrera.get()
        semestre = self.entry_semestre.get()
        
        if not self.validar_no_vacio(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre):
            return
        if not (self.validar_str(nombre) and self.validar_str(apellido) and self.validar_str(carrera)):
            return
        if not (self.validar_matricula(matricula) and self.validar_fechas(fecha_nacimiento)):
            return
        
        valores = (nombre, apellido, fecha_nacimiento, matricula, carrera, semestre)
        if self.es_duplicado(self.tree_estudiantes, valores):
            CTkMessagebox(title="Error", message="El estudiante ya está registrado.", icon="warning")
            return
        
        nuevo_estudiante = Estudiante(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre)
        self.estudiantes.append(nuevo_estudiante)
        self.tree_estudiantes.insert('', 'end', values=(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre))
        print(f"Estudiante ingresado: {nuevo_estudiante.nombre} {nuevo_estudiante.apellido}")

    def ingresar_profesor(self):
        nombre = self.entries["Profesor"]["nombre"].get()
        apellido = self.entries["Profesor"]["apellido"].get()
        fecha_nacimiento = self.entry_fecha_nacimiento_p.get()
        num_empleado = self.entry_num_empleado.get()
        departamento = self.entry_departamento.get()

        if not self.validar_no_vacio(nombre, apellido, fecha_nacimiento, num_empleado, departamento):
            return
        if not (self.validar_str(nombre) and self.validar_str(apellido) and self.validar_str(departamento)):
            return
        if not self.validar_fechas(fecha_nacimiento):
            return

        valores = (nombre, apellido, fecha_nacimiento, num_empleado, departamento)
        if self.es_duplicado(self.tree_profesores, valores):
            CTkMessagebox(title="Error", message="El profesor ya está registrado.", icon="warning")
            return

        nuevo_profesor = Profesor(nombre, apellido, fecha_nacimiento, num_empleado, departamento)
        self.profesores.append(nuevo_profesor)
        self.tree_profesores.insert('', 'end', values=(nombre, apellido, fecha_nacimiento, num_empleado, departamento))
        print(f"Profesor ingresado: {nuevo_profesor.nombre} {nuevo_profesor.apellido}")

    def ingresar_asignatura(self):
        nombre = self.entries["Asignatura"]["nombre"].get()
        codigo = self.entry_codigo.get()
        creditos = self.entry_creditos.get()

        if not self.validar_no_vacio(nombre, codigo, creditos):
            return
        if not (self.validar_str(nombre) and codigo.isalnum() and creditos.isdigit()):
            CTkMessagebox(title="Error de Validación", message="Datos de asignatura inválidos", icon="warning")
            return
        
        valores = (nombre, codigo, creditos)
        if self.es_duplicado(self.tree_asignaturas, valores):
            CTkMessagebox(title="Error", message="La asignatura ya está registrada.", icon="warning")
            return

        nueva_asignatura = Asignatura(nombre, codigo, creditos)
        self.asignaturas.append(nueva_asignatura)
        self.tree_asignaturas.insert('', 'end', values=(nombre, codigo, creditos))
        print(f"Asignatura ingresada: {nueva_asignatura.nombre} - Código: {nueva_asignatura.codigo}")

    def ingresar_grupo(self):
        nombre_grupo = self.entries["Grupo"]["nombre"].get()
        num_grupo = self.entry_num_grupo.get()
        asignatura_nombre = self.entry_asignatura.get()
        estudiante_nombre = self.entry_estudiante.get()

        if not self.validar_no_vacio(nombre_grupo, num_grupo, asignatura_nombre, estudiante_nombre):
            return
        if not (self.validar_str(nombre_grupo) and num_grupo.isdigit()):
            CTkMessagebox(title="Error de Validación", message="Datos de grupo inválidos", icon="warning")
            return

        # Buscar estudiante y asignatura normalizando a minúsculas para evitar problemas de comparación
        estudiante = next((p for p in self.estudiantes if f"{p.nombre.lower()} {p.apellido.lower()}" == estudiante_nombre.lower()), None)
        asignatura = next((a for a in self.asignaturas if a.nombre.lower() == asignatura_nombre.lower()), None)

        # Si no encuentra estudiante o asignatura, muestra un mensaje de error
        if not estudiante:
            CTkMessagebox(title="Error", message="Estudiante no encontrado", icon="warning")
            return

        if not asignatura:
            CTkMessagebox(title="Error", message="Asignatura no encontrada", icon="warning")
            return
        
        nuevo_grupo = Grupo(num_grupo, asignatura, estudiante)
        self.grupos.append(nuevo_grupo)
        self.tree_grupos.insert('', 'end', values=(nombre_grupo, num_grupo, asignatura_nombre, estudiante_nombre))
        print(f"Grupo ingresado: {nuevo_grupo.numero_grupo} - Asignatura: {nuevo_grupo.asignatura.nombre}")

    def ingresar_programa_academico(self):
        nombre = self.entries["Programa Académico"]["nombre"].get()
        codigo = self.entry_codigo_programa.get()

        if not self.validar_no_vacio(nombre, codigo):
            return
        if not (self.validar_str(nombre) and codigo.isalnum()):
            CTkMessagebox(title="Error de Validación", message="Datos de programa académico inválidos", icon="warning")
            return
        
        valores = (nombre, codigo)
        if self.es_duplicado(self.tree_programas, valores):
            CTkMessagebox(title="Error", message="El programa académico ya está registrado.", icon="warning")
            return

        nuevo_programa = ProgramaAcademico(nombre, codigo)
        self.programas_academicos.append(nuevo_programa)
        self.tree_programas.insert('', 'end', values=(nombre, codigo))
        print(f"Programa Académico ingresado: {nuevo_programa.nombre} - Código: {nuevo_programa.codigo}")

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = SistemaGestionUniversitaria()
    app.mainloop()
