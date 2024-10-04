class ProgramaAcademico():
    #Atributos Privados: nombre (str) codigo (str) grupos (Lista protegida de objetos Grupo)
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.__grupos = []
    
    
    #agregar_grupo(grupo: Grupo): Agrega un grupo al programa académico con validación para evitar duplicados.
    def agregar_grupo(self, grupo):
        if grupo not in self.__grupos:
            self.__grupos.append(grupo)
        else:
            print(f'El grupo {grupo.n_grupo} ya está en el programa académico')
    
    
    #eliminar_grupo(numero_grupo: int): Elimina un grupo del programa académico por su número, asegurando que exista.
    def eliminar_grupo(self, numero_grupo):
        for grupo in self.__grupos:
            if grupo.n_grupo == numero_grupo:
                self.__grupos.remove(grupo)
                return
        print(f'No se encontró un grupo con el número {numero_grupo}')
    
    
    
    #mostrar_programa(): Muestra la información completa del programa académico, incluyendo todos los grupos asociados.
    def mostrar_programa(self):
        print(f'Programa Académico: {self.nombre} ({self.codigo})')
        for grupo in self.__grupos:
            grupo.mostrar_grupo()
        print()