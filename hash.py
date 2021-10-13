import sys
from functions import *

#Funcion principal o Main
#En primera instancia se llama a la función conprobacion para identificar el tipo de archivo
#Si es True corresponde a un archivo, si es False a texto y 'Error' en caso de que falte un parámetro de entrada
if __name__ == '__main__':
    comprobar = comprobacion(sys.argv)
    flag = True
    if(comprobar == 'Error'):
        print('Error!! Debe ingresar un texto o archivo de texto')
        flag = False

    #Ciclo principal para mantener en ejecución el menú
    while(flag):
        print('\nQuede desea hacer con el texto/archivo de entrada?\n')
        print('1) Realizar Hash\n')
        print('2) Calcular entropia\n')
        print('3) Salir\n')
        opcion = input('Ingrese opcion:\n')
        if(opcion == '1'):
            if(comprobar == False):
                #Realización del proceso de Hash para el texto ingresado
                print(hash(sys.argv[1], 'texto'))

            elif(comprobar == True):
                #Se imprime resultado por resultado en consola correspondientes a cada linea del archivo
                for i in hash(sys.argv[1], 'archivo'):
                    print(i)

        #Presentación de resultados de la forma Entropia | Texto entrada, por consola (STDOUT)
        elif(opcion == '2'):
            if(comprobar == False):
                print ("{:<10} {:<1} {:<10}".format('Entropia','|','Texto entrada'))
                print ("{:<10} {:<1} {:<10}".format(entropia(sys.argv[1]),'|', sys.argv[1]))

            elif(comprobar == True):
                #Se enlista cada linea para luego calcular la entropía de cada una de ellas.
                with open(sys.argv[1], "r", errors= 'ignore') as archivo:
                    lista = [linea.rstrip() for linea in archivo]
                print ("{:<10} {:<1} {:<10}".format('Entropia','|', 'Texto entrada'))
                for texto in lista:
                    print ("{:<10} {:<1} {:<10}".format(entropia(texto), '|', texto))

        elif(opcion == '3'):
            flag = False

        else:
            print('Debe ingresar una opcion valida\n')   