class Grupo:
    def __init__(self, numero_grupo, asignatura, profesor):
        self._numero_grupo = numero_grupo
        self._asignatura = asignatura
        self._profesor = profesor
        self._estudiantes = []
        
    def agregar_estudiante(self, estudiante):
        if estudiante in self._estudiantes:
            raise ValueError(f"El estudiante con matrícula {estudiante.matricula} ya está registrado en este grupo.")
        self._estudiantes.append(estudiante)
        return True
        
    def eliminar_estudiante(self, matricula):
        for estudiante in self._estudiantes:
            if estudiante.matricula == matricula:
                self._estudiantes.remove(estudiante)
                return True
        raise ValueError(f"No se encontró un estudiante con matrícula {matricula} en este grupo.")
        
    def mostrar_grupo(self):
        info = f'Grupo {self.numero_grupo} de la asignatura {self.asignatura.nombre} impartida por el profesor {self.profesor.nombre} {self.profesor.apellido}\n'
        info += 'Estudiantes:\n'
        for estudiante in self._estudiantes:
            info += f'- {estudiante.presentarse()}\n'
        return info

    @property
    def numero_grupo(self):
        return self._numero_grupo
    
    @numero_grupo.setter
    def numero_grupo(self, numero_grupo):
        self._numero_grupo = numero_grupo
        
    @property
    def asignatura(self):
        return self._asignatura
    
    @asignatura.setter
    def asignatura(self, asignatura):
        self._asignatura = asignatura
    
    @property
    def profesor(self):
        return self._profesor
    
    @profesor.setter
    def profesor(self, profesor):
        self._profesor = profesor
    
    @property
    def estudiantes(self):
        return self._estudiantes
