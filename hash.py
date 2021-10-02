import sys


def hash_archivo(archivo):

    return 0

def hash_texto(string):

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


comprobar = comprobacion(sys.argv)

if(comprobar == False):

    print(hash_texto(sys.argv[1]))

elif(comprobacion == True):

    print(hash_texto(sys.argv[1]))

elif(comprobar == 'Error'):

    print('Error')