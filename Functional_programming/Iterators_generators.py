


# Lazy objects retorna iterador, los iteradores no devuelven los valores
# hasta que son llamados y los devuelve uno a uno
# esto permite manejar secuencias infinitas
# algunos funciones lazy que son integradas (builtins )
#    map(func, iterables) recibe una funcion  y lo aplica a todos los elementos 
#    de un iterador
# 
#    filter(func, iterables): recibe una funcion y devuevle un lazy iterador
#    de los elementos que el resultado de la funcion sean verdaderos.
#    
#    zip(*iterables): devuelve una tupla con las cantidades de iterables
#    pasados como parametro
#
#    range(start, stop, secuence)
#
#    enumerate()

# iterable es un objeto capaz de retornar sus miembros uno a uno, todos lo
# que puedes usar en un for loop es un iterable. los iterables deben implementar
# uno de estos metodos __getitem__, __iter__.

# iterator: son objetos que mantienen o siguen la posicion durante la iteracion
# solo puedes iterar en un iterador una sola vez.
# los iterators deben implementar los siguientes metodos:
# __next__: retora el ultimo elemento
# __iter__: retorna el iterador mismo

# Generator: es una funcion qeu tiene por los moenos un yield, un generador
# devuelve un objeto generador. una ventaja de los decoradores que al iguale
# que los iterables solo mantienen na posicion en la memoria y soportan 
# secuencias infinitas.

print('\n############## Iterables ##############\n')

def gfibo(num):
    ''' Genera numero de fibonacci '''
    fst, snd = 0, 1
    for x in range(num):
        yield fst
        fst, snd = snd, fst + snd

for f in gfibo(15):
    print(f, end=' ')


# Los generadores se pueden combinar con otros generadores permitiendo
# Procesar multiples sentencias al mismo tiempo 
print('\n############# Generator objects #############\n')
from math import sqrt

def count(start=0):
    n = start
    while True:
        yield n
        n += 1

def is_even(num):
    return num%2 == 0

def is_square(num):
    return sqrt(num).is_integer()

nums = count() #representa secuencia infinita >0
squares = filter(is_square, nums) # solo los cuadrados
even_squares = filter(is_even, squares) # solo los cuadrados pares
for n, es in enumerate(even_squares):
    if n > 15:
        break
    print(es, end=' ')


# Los generadose tambien pueden ser generados por expresiones, y son
# llamados generator expression (genexpr), es similar a los list
#  comprehension pero encerrados en parentesis "()"

my_gene = (x**2 for x in range(10))
print("\n############## Generator expressions #############\n")
print("object", my_gene)
print("squares_numbers", list(my_gene)) 

# Python coroutines can receive multiple values and send multiples values
# The basic sintax of coroutine is:

# Generators usualmente generan valores, sin embargo las coroutines consumen
# valores, usan val = yield para recibir valores, y opcionalmente usan c.send(val)
# para enviar valores a otra rutina enlazada.

def coroutine():
    n = yield
    print('Received:', n)

# la corrutinas estan enlazadas unas a otras. 

# the @contextemanager decorator allows you to use the yiel to stop
# and point to a function. 
from contextlib import contextmanager
print('\n##############Contex Manager##############\n')
@contextmanager
def mycm():
    print('Start')
    try:
        yield
    finally:
        print('End')

with mycm():
    print('test')


