from operaciones.suma import *
from operaciones.resta import *
from sys import argv, exit

def calcula():
    try:
        a = int(argv[2]), int(argv[3])
    except ValueError as e:
        exit(f'Error: {e}')
        

    if argv[1] == 'suma':
        print(suma(argv[2],argv[3]))
    elif argv[1] == 'resta':
        print(resta(argv[2],argv[3]))

if __name__ == '__main__':
    calcula()