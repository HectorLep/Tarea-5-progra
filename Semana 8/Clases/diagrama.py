class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return f'Hola, soy {self.nombre} y tengo {self.edad} años'
        
class Empleado(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        return f'Hola, soy {self.nombre} y estudio {self.carrera}'
    

class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto
        
    def trabajar(self):
        return f'Hola, soy {self.nombre} y trabajo como {self.puesto}'