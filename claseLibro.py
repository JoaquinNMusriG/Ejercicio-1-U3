from claseCapitulo import Capitulo

class Libro:
    __idLibro = ''
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = ''
    __cantidadCapitulos = 0
    __capitulos = None

    def __init__(self, id, tit, aut, edit, isbn, cantC):
        self.__idLibro = id
        self.__titulo = tit
        self.__autor = aut
        self.__editorial = edit
        self.__isbn = isbn
        self.__cantidadCapitulos = cantC
        self.__capitulos = []

    def __str__ (self):
        for capitulo in self.__capitulos:
            print(capitulo)
        return 'id: ' + self.__idLibro + ' titulo: '+self.__titulo+' autor: '+self.__autor+' editorial: '+self.__editorial+' isbn: '+self.__isbn+' cant Cap: '+str(self.__cantidadCapitulos)

    def __del__(self):
        del self.__capitulos

    def agregarCapitulo (self, tituloCAP, cantPagCAP):
        unCapitulo = Capitulo(tituloCAP, cantPagCAP)
        self.__capitulos.append(unCapitulo)

    def getId (self):
        return self.__idLibro

    def getTit (self):
        return self.__titulo

    def TitCap (self):
        i = 1
        for capitulo in self.__capitulos:
            print(str(i)+'. '+capitulo.getTitulo())
            i += 1

    def getCantPagLibro (self):
        total = 0
        for capitulo in self.__capitulos:
            total += capitulo.getCantPag()
        return total

    def getAutor (self):
        return self.__autor

    def evaluarCapitulos (self, palabra):
        resultado = False
        indice = 0
        while (indice < len(self.__capitulos)) & (not resultado):
            if (self.__capitulos[indice].getTitulo().lower().find(palabra) != -1):
                resultado = True
            indice += 1
        return resultado
