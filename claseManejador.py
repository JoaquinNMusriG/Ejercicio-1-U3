from claseLibro import Libro
import csv

class ManejaLibros:
    __libros = []

    def __init__ (self):
        self.__libros = []

    def mostrarLibros (self):
        for libro in self.__libros:
            print(libro)

    def cargarLibros (self):
        archivo = open('libros.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for lista in reader:
            unLibro = Libro(lista[0],lista[1],lista[2],lista[3],lista[4],int(lista[5]))
            for i in range(int(lista[5])):
                row = next(reader)
                unLibro.agregarCapitulo(row[0],int(row[1]))
            self.__libros.append(unLibro)

    def mostrarTitCapCantPag (self, id):
        resultado = False
        indice = 0
        while (indice < len(self.__libros)) & (not resultado):
            if (self.__libros[indice].getId() == id):
                print(self.__libros[indice].getTit())  #titulo del libro
                self.__libros[indice].TitCap()  #titulo de capitulos
                print('Cantidad de Pag: '+ str(self.__libros[indice].getCantPagLibro()))  #cantidad de paginas
                resultado = True
            indice += 1
        return resultado

    def mostrarTitAut (self, palabra):
        resultado = False
        band = False
        for libro in self.__libros:
            if (libro.getTit().lower().find(palabra) != -1):
                band = True
                resultado = True
            elif (libro.evaluarCapitulos(palabra)):
                band = True
                resultado = True
            if band:
                print(libro.getTit())
                print(libro.getAutor())
            band = False
        return resultado
