import sys

def operaciones(lista):
    resultado = ''
    for i in range(0,2):
        for i in range(len(lista)):
            lista[i] = lista[i]*23
            lista[i] = lista[i]%64
            lista[i] = lista[i]+42

    for elemento in lista:
        if(elemento%2 == 0):
            resultado += chr(elemento+1)
        else:
            resultado += chr(elemento-1) 
            
    return resultado
def adaptacion(texto):
    caracteres = []
    for letra in texto:
        caracteres.append(ord(letra))

    if (len(caracteres) < 25):
        #aumentar cantidad de caracteres
        for i in range(0, 25-len(caracteres)):
            add = int((caracteres[i] + caracteres[0])/2)
            caracteres.append(add)
    #elif(len(caracteres) > 25):
        #disminuir la cantidad de caracteres
        
    #else:
        #cantidad de caracteres ajustada al largo

    resultado = operaciones(caracteres)
    return resultado

def hash(argumento, tipo):

    if(tipo == 'archivo'):
        #abrir y recorrer archivo
        return 0 

    elif(tipo == 'texto'):
        return adaptacion(argumento)

    return 0

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

if __name__ == '__main__':
    comprobar = comprobacion(sys.argv)

    if(comprobar == False):
        print(hash(sys.argv[1], 'texto'))

    elif(comprobacion == True):
        print(hash(sys.argv[1], 'archivo'))

    elif(comprobar == 'Error'):
        print('Error')