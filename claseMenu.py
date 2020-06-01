class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.porID,
                            2:self.porPalabra,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, lista):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(lista)
    def salir(self,lista):
        print('Salir')
    def porID(self,lista):
        id = input('Ingrese el id de libro a mostrar: ')
        resultado = lista.mostrarTitCapCantPag(id)
        if (not resultado):
            print('No hay libro con ese id.')
    def porPalabra(self,lista):
        palabra = input('Ingrese la palabra a buscar en los libros: ')
        resultado = lista.mostrarTitAut(palabra.lower())
        if (not resultado):
            print('No hay libro con esa palabra en su titulo o en alguno de sus capitulos.')
