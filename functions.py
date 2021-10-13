import sys
import random
import math
from datetime import datetime

#se cambia la semilla a utilizar por hora
random.seed(datetime.now().hour)

def entropia(texto):
    base = 128 #correspondiente a la cantidad de caracteres ASCII
    entropia = len(texto)*math.log(base, 2) #H = L*Log2(W)
    return entropia

#Funcion encargada de realizar el cambio según operaciones matemáticas
#En este caso se realizan multiplicaciones, funcion modulo y suma valor por valor
#Luego de realizadas las operaciones, según la posición del caracter en una lista, se le agrega o quita 1
#Para terminar se retorna el resultado como String
def operaciones(lista):
    resultado = ''
    for i in range(0,2):
        for j in range(len(lista)):
            lista[j] = lista[j]*random.randint(20, 25)
            lista[j] = lista[j]%random.randint(60, 65)
            lista[j] = lista[j]+random.randint(40, 45)

    for elemento in lista:
        if(elemento%2 == 0):
            resultado += chr(elemento+1)
        else:
            resultado += chr(elemento-1) 

    return resultado

#Función encargada de adaptar el texto de entrada según el largo correspondiente al hash
#En caso de ser menor al valor se agregan valores siguiendo la operacion: 
#(valor ordinal(ASCII) del caracter actual en el ciclo + valor ordinal del primer valor de la lista)/2
#Al valor anterior se le extrae solamente el entero correspondiente.
#Por otro lado, en caso de ser mayor al largo del hash se elimina el primer valor y el ultimo de forma alternada.
#Luego de tener el largo necesario se llama a la funcion operaciones()
def adaptacion(texto):
    caracteres = []
    if  (len(texto) == 0):
        return 'Linea vacía'

    for letra in texto:
        caracteres.append(ord(letra))

    #Se realiza un cambio en el primer valor para no obtener como resultado un patrón para la primera letra
    caracteres[0] = caracteres[0] + caracteres[-1]
    if (len(caracteres) < 25):
        #aumentar cantidad de caracteres
        for i in range(0, 25-len(caracteres)):
            add = int((caracteres[i] + caracteres[0])/2)
            caracteres.append(add)
    elif(len(caracteres) > 25):
        #disminuir la cantidad de caracteres
        for i in range(0, len(caracteres)-25):
            if(i%2 == 0):
                caracteres.pop(0)
            else: 
                caracteres.pop(-1)

    resultado = operaciones(caracteres)
    return resultado

#Funcion inicial del Hash, en caso de ser un archivo, se hace la llamada a adaptacion linea por linea
#Se utiliza 'errors = ignore' para que en caso de recibir una linea de texto vacia en el archivo (largo 0) se continue la ejecución
#En los archivos, los resultados se agregan a una lista.
def hash(argumento, tipo):

    if(tipo == 'archivo'):
        passw = []
        with open(argumento, "r", errors= 'ignore') as archivo:
            lista = [linea.rstrip() for linea in archivo]
        for pw in lista:
            passw.append(adaptacion(pw))
        return passw
    elif(tipo == 'texto'):
        return adaptacion(argumento)

#Funcion para verificar el tipo de entrada recibida
#Luego de verificar se retorna el tipo de entrada (archivo o texto), en caso de ser vacia retorna el string 'Error'
def comprobacion(entrada):

    if(len(entrada) < 2 | len(entrada) > 2):
        return 'Error'
        
    else: 
        try:
            with open(entrada[1], 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False
