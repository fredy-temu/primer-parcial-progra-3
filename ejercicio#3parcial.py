#Desarrolle un programa en el cual permita registrar 10 países
#con sus respectivas capitales, utilizando diccionarios

def cargar():
    print('PAISES')
    print('______')
    paises={}
    for x in range(10):

        pais=input("Ingrese el nombre de un pais: ")
        capital=input("Ingrese la capital: ")
        print()
        paises[pais] = capital
    return paises
def imprimir(paises):
    print("Listado del diccionario completo")
    print ()
    for pais in paises:
        print(pais, paises[pais])
paises=cargar()
imprimir(paises)
