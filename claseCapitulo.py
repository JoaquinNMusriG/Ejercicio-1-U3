class Capitulo:
    __Titulo = ''
    __cantidadPaginas = 0

    def __init__ (self, titulo, cantPag):
        self.__Titulo = titulo
        self.__cantidadPaginas = cantPag

    def __str__ (self):
        return 'Titulo: ' + self.__Titulo + ' CantidadPaginas: ' + str(self.__cantidadPaginas)    

    def getTitulo (self):
        return self.__Titulo

    def getCantPag (self):
        return self.__cantidadPaginas
