import sys
def operaciones(texto):
    resultado = ''
    caracteres = []
    for letra in texto:
        caracteres.append(ord(letra))

    if (len(caracteres) < 25):
        #aumentar cantidad de caracteres
        for i in range(0, 24-len(caracteres)):
            caracteres.append()
    #elif(len(caracteres) > 25):
        #disminuir la cantidad de caracteres
        
    #else:
        #cantidad de caracteres ajustada al largo

    return resultado

def hash(argumento, tipo):

    if(tipo == 'archivo'):
        #abrir y recorrer archivo
        return 0 

    elif(tipo == 'texto'):
        return operaciones(argumento)

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