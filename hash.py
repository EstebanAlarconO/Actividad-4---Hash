import sys
from functions import *

if __name__ == '__main__':
    comprobar = comprobacion(sys.argv)
    flag = True
    if(comprobar == 'Error'):
        print('Error!! Debe ingresar un texto o archivo de texto')
        flag = False

    while(flag):
        print('\nQuede desea hacer con el texto/archivo de entrada?\n')
        print('1) Realizar Hash\n')
        print('2) Calcular entropia\n')
        print('3) Salir\n')
        opcion = input('Ingrese opcion:\n')
        if(opcion == '1'):
            if(comprobar == False):
                print(hash(sys.argv[1], 'texto'))

            elif(comprobar == True):
                #Se imprime resultado por resultado en consola
                for i in hash(sys.argv[1], 'archivo'):
                    print(i)

        elif(opcion == '2'):
            if(comprobar == False):
                print ("{:<10} {:<10}".format('Entropia','Texto entrada'))
                print ("{:<10} {:<10}".format(entropia(sys.argv[1]), sys.argv[1]))

            elif(comprobar == True):

                with open(sys.argv[1], "r", errors= 'ignore') as archivo:
                    lista = [linea.rstrip() for linea in archivo]
                print ("{:<10} {:<10}".format('Entropia','Texto entrada'))
                for texto in lista:
                    print ("{:<10} {:<10}".format(entropia(texto), texto))

        elif(opcion == '3'):
            flag = False

        else:
            print('Debe ingresar una opcion valida\n')   