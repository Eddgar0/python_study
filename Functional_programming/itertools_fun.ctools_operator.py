# Userful tools in itertools
from itertools import chain, accumulate, count,cycle, repeat, starmap, product, permutations, combinations, combinations_with_replacement

#  chain(*iterables)
#  Entrada: 1 o mas iterables
#  Salida: Todos los elementos del iterable
print('Ejemplos chain')
res = chain('ABC', [1,2,3])
print(list(res))

# con el metodo .from_iterable podermos recibir un iterable con iterables
# en su interior
print('Ejemplos de chain.from_iterable()')
res = chain.from_iterable(['ABC', [1, 2, 3], 'DEF', (4, 5, 6)])
print(list(res))


# accumulate(iterable, func=add)
# Entrada: Iterable
# Salida: los totales obtenidos de aplicar la funcion al iterable, por
# defecto aplica la funcion sum()
print('Ejemplo de accumulate')
suma_accumulada = accumulate([1,2,3,4,5])
producto_accumulado = accumulate([1,2,3,4,5], lambda x,y: x * y)
print(list(suma_accumulada), '\n', list(producto_accumulado))

# count(start=0, step=1)
# genera numeros infinitos segun los parametros.
print(' Ejemplo de count')
infinito = count(start=100, step=50)
for i in range(10):
    print(next(infinito))

# cycle(iterable)
# Entrada: Iterable
# Salida: repetidamente genera los elementos del iterable

print("Ejemplo con Cicle")
marcha = cycle([1,2,3,4])
for pasos in range(20):
    print(next(marcha), end='..')

# Repeat(obj, times=None)
# entrada: un objeto para ser repetidos opcionalmente cantidad de veces
# Salida: Generador del objeto infefinidamente o las veces puestas en times

print('\nEjemplo de Repeat')

cargando = repeat('!', 10)
print(*cargando, sep='')

# starmap(function, iterable)
# Entrada: funcion e iterable
# Salida: El resultado de aplicar la funciona al iterable
print('Ejemplo de starmap')
potencias = starmap(lambda x,y: x ** y, [(2,4), (3,2), (10,3)])
print(list(potencias))

# tools combinatorios de itertools
# Estos son operaciones matematicas de combinaciones y permutaciones
# product(*iterables, repeat=1)
# permutations(iterable, r=None) ! r es la cantidad de elementos a permutar
# combinations(iterable, r) ! r es la cantidad de elementos a combinar
# combinations_with_replacement(iterable, r) ! r es la cantidad de elementos a combinar

##### functools ######
print('######### functools ########')
from functools import reduce, partial

# reduce(function, iterable)
# entrada: una funcion de dos argumentos y un iterable
# Salida: Un solo valor obtenido de aplicar la funcion a los elementos 
# del iterable.
print('ejemplo de reduce')

def suma (x, y):
    return x + y 
sumatoria = reduce(suma, [1,2,3,4,5])
print(sumatoria)

# partial(function, *args, **kwargs)
# Retorna una funcion nueva pero ya con los parametros establecidos de
# de la funcion receptora
 
print('Ejemplo de Partial')

suma5 = partial(suma,5)
print(suma5(4))
print(suma5(3))

print_log =partial(print, 'Log:')
print_log('iniciando log')

###### OPERATOR MODULES ##########
from operator import add, pow, is_
# todo lo referido a operadoes en python hay de todos tipos.