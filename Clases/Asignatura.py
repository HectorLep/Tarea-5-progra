class Asignatura:
    def __init__(self, nombre, codigo, creditos):
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos

    def mostrar_informacion(self):
        if self._creditos <= 0:
            raise ValueError("La cantidad de créditos debe ser mayor que 0.")
        return f'La asignatura {self.nombre} tiene el código {self.codigo} y {self.creditos} créditos'
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
        
    @property
    def creditos(self):
        return self._creditos
    
    @creditos.setter
    def creditos(self, creditos):
        self._creditos = creditos