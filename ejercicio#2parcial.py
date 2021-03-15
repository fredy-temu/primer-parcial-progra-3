#2.	Desarrolle un programa en el cual permita registrar 10 marcas de productos,
# con nombre y código de producto, estos deben ser almacenados en listas. Al finalizar el
# registro debe mostrar todos los productos registrados.

def ejercicio2():
    marcas=[]
    codigos=[]
    for x in range(10):
        print()
        pro=input('Ingrese la marca del producto: ')
        marcas.append(pro)
        nompro=input('Ingrese Nombre del producto: ')
        codpro=input('Ingrese codigo de un producto: ')
        codigos.append([nompro,codpro])
        print()

    for x in range(10):

        print('LAS MARCAS REGISTRADAS SON: ', marcas[x], codigos[x][0], codigos[x][1])

ejercicio2()
