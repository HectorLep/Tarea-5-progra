
# ProgramaAcademico.py
class ProgramaAcademico:
    def __init__(self, nombre, codigo):
        self._nombre = nombre
        self._codigo = codigo
        self._grupos = []
    
    def agregar_grupo(self, grupo):
        if any(g.numero_grupo == grupo.numero_grupo for g in self._grupos):
            raise ValueError(f"El grupo {grupo.numero_grupo} ya está registrado en el programa académico.")
        self._grupos.append(grupo)
        return True
    
    def eliminar_grupo(self, numero_grupo):
        for grupo in self._grupos:
            if grupo.numero_grupo == numero_grupo:
                self._grupos.remove(grupo)
                return True
        raise ValueError(f"No se encontró el grupo {numero_grupo} en el programa académico.")
    
    def mostrar_programa(self):
        info = f'Programa Académico: {self.nombre} ({self.codigo})\n'
        for grupo in self._grupos:
            info += grupo.mostrar_grupo() + '\n'
        return info
    
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
    def grupos(self):
        return self._grupos