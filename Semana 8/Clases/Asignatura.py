class Asignatura():
    def __init__(self, nombre, codigo,creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos

    #mostrar_informacion(): Imprime la información detallada de la asignatura
    def mostrar_informacion(self):
        print('La asignatura {self.nombre} tiene el código {self.codigo} y {self.creditos} créditos')
    
    #nombre: Permite obtener y establecer el nombre de la asignatura.
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    #codigo: Permite obtener y establecer el código de la asignatura.
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
        
    #creditos: Permite obtener y establecer los créditos de la asignatura.
    @property
    def creditos(self):
        return self.__creditos
    
    @creditos.setter
    def creditos(self, creditos):
        self.__creditos = creditos
        
    