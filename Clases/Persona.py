class Persona():
    def __init__(self, nombre, apellido, fecha_de_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        
    def presentarse(self):
        print(f'Hola, soy {self.nombre} {self.apellido} y nací el {self.fecha_de_nacimiento}')
    
    #nombre: Permite obtener y establecer el nombre.
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    #apellido: Permite obtener y establecer el apellido.
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
        
    #fecha_de_nacimiento: Permite obtener y establecer la fecha de nacimiento.
    @property
    def fecha_de_nacimiento(self):
        return self.__fecha_de_nacimiento
    
    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, fecha_de_nacimiento):
        self.__fecha_de_nacimiento = fecha_de_nacimiento 
        
class Estudiante(Persona):
    #Atributos Privados:  matricula (str) carrera (str) semestre (int)
    def __init__(self, nombre, apellido, fecha_de_nacimiento,matricula, carrera, semestre):    
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        
    #estudiar(materia: str, horas: int): Imprime un mensaje indicando que el estudiante ha estudiado una materia durante cierta cantidad de horas
    def estudiar(self, materia, horas):
        print(f'El estudiante ha estudiado {materia} durante {horas} horas')
    
    #presentarse(): Sobrescribe el método de Persona para incluir información específica del estudiante
    def presentarse(self):
        return f'Hola, soy {self.nombre} {self.apellido} y nací el {self.fecha_de_nacimiento}. Mi matrícula es {self.matricula}, estudio {self.carrera} y estoy en el semestre {self.semestre}'
    
    #matricula: Permite obtener y establecer la matrícula.
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    #carrera: Permite obtener y establecer la carrera.
    @property
    def carrera(self):
        return self.__carrera
    
    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera
    
    #semestre: Permite obtener y establecer el semestre.
    @property
    def semestre(self):
        return self.__semestre
    
    @semestre.setter
    def semestre(self, semestre):
        self.__semestre = semestre
    
class Profesor(Persona):
    def __init__(self, nombre, apellido, fecha_de_nacimiento,n_empleado, departamento):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self.n_empleado = n_empleado
        self.departamento = departamento
        
    #enseñar(materia: str): Imprime un mensaje indicando que el profesor está enseñando una materia.
    def enseñar(self, materia):
        print(f'El profesor está enseñando la materia {materia}')
        
    #presentarse(): Sobrescribe el método de Persona para incluir información específica del profesor.
    def presentarse(self):
        return f'Hola, soy {self.nombre} {self.apellido} y nací el {self.fecha_de_nacimiento}. Mi número de empleado es {self.n_empleado}'
    
    #numero_empleado: Permite obtener y establecer el número de empleado.
    @property
    def n_empleado(self):
        return self.__n_empleado
    
    @n_empleado.setter
    def n_empleado(self, n_empleado):
        self.__n_empleado = n_empleado
        
    #departamento: Permite obtener y establecer el departamento.
    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento
        
