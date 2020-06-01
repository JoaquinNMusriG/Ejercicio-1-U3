from claseManejador import ManejaLibros
from claseMenu import Menu

if __name__ == '__main__':
    ListaLibros = ManejaLibros()
    ListaLibros.cargarLibros()

    menu= Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Ingresar ID y mostrar titulos y cantidad de paginas
              2 Ingresar palabra y mostrar titulos con autor""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op,ListaLibros)
        salir = op == 0
