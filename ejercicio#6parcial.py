#Desarrolle un programa que permita registrar 8 jugadores de videojuegos (gamers)
# con su respectiva edad, en cada registro se debe validar la edad del alumno para clasificarlo
# según la siguiente tabla de clasificación:
#•	Novato = entre 14 y 16 años
#•	Experto = entre 17 y 20 años
#•	Super Experto = mayores a 20 años
#Al finalizar el registro de los jugadores, el sistema deber permitir seleccionar una categoría
#para mostrar los jugadores registrados en dicha categoría.

def ejercicio6():

    print()
    print('JUGADORES DE VIDEOJUEGOS (GAMERS)')
    print('________________________________')

    cont=0
    conta=0
    contad=0

    for x in range(8):

        input('ingrese el nombre del jugador: ')
        edad=int(input('ingrese la edad del jugador: '))

        if edad < 14:
            print('INGRESO UNA EDAD NO VALIDA')
            return()

        elif edad >= 14  and edad<=16:
            cont+=1

        elif edad >16 and edad<=20:
            conta+=1

        elif edad > 20:
            contad+=1

    print('los jugadores Novato = entre 14 y 16 años son: ', cont)
    print('los jugadores Experto = entre 17 y 20 años son: ', conta)
    print('los jugadores Super Expertos= mayores de 20 años: ', contad)

ejercicio6()
