class Grupo():
    def __init__(self, n_grupo, asignatura, profesor, estudiantes):
        self.n_grupo = n_grupo
        self.asignatura = asignatura
        self.profesor = profesor
        self.estudiantes = []
        
    #agregar_estudiante(estudiante: Estudiante): Agrega un estudiante al grupo con validación para evitar duplicados.
    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.append(estudiante)
        else:
            print(f'El estudiante {estudiante.nombre} ya está en el grupo')
        
    #eliminar_estudiante(matricula: str): Elimina un estudiante del grupo por su matrícula, asegurando que exista        
    def eliminar_estudiante(self, matricula):
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                self.estudiantes.remove(estudiante)
                return
        print(f'No se encontró un estudiante con la matrícula {matricula}')
        
    #mostrar_grupo(): Muestra la información completa del grupo, incluyendo asignatura, profesor y lista de estudiantes.
    def mostrar_grupo(self):
        print(f'Grupo {self.n_grupo} de la asignatura {self.asignatura.nombre} impartida por el profesor {self.profesor.nombre} {self.profesor.apellido}')
        print('Estudiantes:')
        for estudiante in self.estudiantes:
            print(estudiante.presentarse())
        print()
        
    
    #numero_grupo: Permite obtener y establecer el número del grupo.
    @property
    def n_grupo(self):
        return self.__n_grupo
    
    @n_grupo.setter
    def n_grupo(self, n_grupo):
        self.__n_grupo = n_grupo
        
    #asignatura: Permite obtener y establecer la asignatura del grupo.
    @property
    def asignatura(self):
        return self.__asignatura
    
    @asignatura.setter
    def asignatura(self, asignatura):
        self.__asignatura = asignatura
    
    #estudiantes: Solo permite obtener la lista de estudiantes (no se puede establecer directamente).        
    @property
    def estudiantes(self):
        return self.__estudiantes 
    
    @asignatura.setter
    def estudiantes(self, estudiantes):
        self.__estudiantes = estudiantes
        

    