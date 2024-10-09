class Persona:
    def __init__(self, nombre, apellido, fecha_de_nacimiento):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_de_nacimiento = fecha_de_nacimiento
        
    def estudiar(self, materia, horas):
        if horas <= 0:
            raise ValueError("El número de horas debe ser mayor que 0.")
        return f'El estudiante ha estudiado {materia} durante {horas} horas'
    
    def presentarse(self):
        return f'{super().presentarse()}. Mi matrícula es {self.matricula}, estudio {self.carrera} y estoy en el semestre {self.semestre}'
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property
    def fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento
    
    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, fecha_de_nacimiento):
        self._fecha_de_nacimiento = fecha_de_nacimiento 

# Estudiante.py
class Estudiante(Persona):
    def __init__(self, nombre, apellido, fecha_de_nacimiento, matricula, carrera, semestre):    
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre
        
    def estudiar(self, materia, horas):
        return f'El estudiante ha estudiado {materia} durante {horas} horas'
    
    def presentarse(self):
        return f'{super().presentarse()}. Mi matrícula es {self.matricula}, estudio {self.carrera} y estoy en el semestre {self.semestre}'
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula
    
    @property
    def carrera(self):
        return self._carrera
    
    @carrera.setter
    def carrera(self, carrera):
        self._carrera = carrera
    
    @property
    def semestre(self):
        return self._semestre
    
    @semestre.setter
    def semestre(self, semestre):
        self._semestre = semestre

# Profesor.py
class Profesor(Persona):
    def __init__(self, nombre, apellido, fecha_de_nacimiento, numero_empleado, departamento):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._numero_empleado = numero_empleado
        self._departamento = departamento
        
    def enseñar(self, materia):
        if not materia:
            raise ValueError("La materia no puede estar vacía.")
        return f'El profesor está enseñando la materia {materia}'
            
    def presentarse(self):
        return f'{super().presentarse()}. Mi número de empleado es {self.numero_empleado} y pertenezco al departamento de {self.departamento}'
    
    @property
    def numero_empleado(self):
        return self._numero_empleado
    
    @numero_empleado.setter
    def numero_empleado(self, numero_empleado):
        self._numero_empleado = numero_empleado
        
    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento
