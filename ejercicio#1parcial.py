#1.	Desarrolle un programa en el cual permita registrar 10 alumnos con nombre y numero de carné
# y los almacene en una tupla, al finalizar el registro de los alumnos
# se deben mostrar por pantalla todos los alumnos registrados.

def cargar_alumnos():

    print()
    alumno = input("Nombre del alumno: ")
    carnet = int(input("Dame el numero de carnet del alumno: "))
    print()

    return (alumno, carnet)

nombre1=cargar_alumnos()
nombre2=cargar_alumnos()
nombre3=cargar_alumnos()
nombre4=cargar_alumnos()
nombre5=cargar_alumnos()
nombre6=cargar_alumnos()
nombre7=cargar_alumnos()
nombre8=cargar_alumnos()
nombre9=cargar_alumnos()
nombre10=cargar_alumnos()

print([nombre1], [nombre2], [nombre3], [nombre4], [nombre5], [nombre6], [nombre7], [nombre8], [nombre9], [nombre10])


