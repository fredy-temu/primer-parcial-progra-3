#Desarrolle un programa que permita registrar 8 cursos con la respectiva nota entre 50 y 100 puntos,
#al finalizar el registro el sistema debe mostrar únicamente los cursos cuya nota representa
#aprobación del curso ( 61 o superior ). Si el numero ingresado es menor a 50 el programa debe
#mostrar mensaje de error y permitir volver a ingresar el registro

def ejercicio5():

    cont=0
    acum=0

    for x in range(8):
        curso=input("Ingrese el curso: ")
        curso1 = int(input("Ingrese nota del curso: "))

        if curso1 < 50:
            print ("error, nota baja, vuelva a ingresar nota")
            int(input("Ingrese nuevamente la nota del curso: "))

        elif curso1>=50 and curso1<61:
            acum+=1

        elif curso1>=61 and curso1<=100:
            cont += 1

    print('la cantidad de cursos aprobados son: ', cont)


ejercicio5()
