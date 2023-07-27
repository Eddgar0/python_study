from functools import wraps
# Decorators are a sintatics and are functions receive a funtion and output a function
# Is normally used to modify the behavior of the function, or make process before and/or after calling the funcion.
def powerup (func):
    print('Power Up')
    return func


@powerup
def get_item ():
    print('An Item')


# The same way to do it withouth decorators. 
# get_item = powerup(get_item)

def make_countdown(n):
    def count():
        nonlocal n #This is called a clousure, when a inner fuction has access to variable of the outerfunction.
        print(n)
        n -= 1
    return count


# Los decoradores pueden tambien ser utilizados para alterar completamente el resultado de la funcion, cuando la funcion posee  parametros
# debe tener la estructura con un una fucnion interna para poder dicha funcion aceptar los parametro de la funcion original, el ejemplo siguiente
# tenemos una funcion que suma los alumntos con numero infinto de parametros con resultado con un integer, con el decorador se cambia el resultado
# para que nos da el promedio y resultado nos da una tupla, (es mala practica cambiar el resultado de tipo de variable)

def promedio(func):
    def inner(*args):
        result = func(*args)
        promedio = result/len(args)
        return result,promedio
    return inner

@promedio
def total_alumnos(*colegios):
    result = 0 
    for c in colegios:
        result += c
    return result

print(total_alumnos(100,20,40))

# GENERADORES DE FUNCIONES
# El generador de funciones permite el decorador acepte parametros, se llama generador de decoradores ya que  con este puede crear otros 
# Decoradores segun los parametros establecidos.
# 
def repeat_for(times):
    def deco(func):
        def inner(*args, **kwargs):
            for x in range(times):
                func(*args)
        return inner
    return deco 
     
@repeat_for(5)
def eco(string):
    print(string)

eco("Hola")
# En el siguiente ejemplo es que le da honor a generador de decoradores, en el siguiente ejemplo generamos un decorador llamado 'dos_veces'
# basado en el generador repeat_for pero con un parametro diferentes. Asi mismo podemos crear los decoradores que queramos.

duplica = repeat_for(2)

@duplica
def eco2(string):
    print(string)

eco2("Tartamudo")

# El decorador  @wraps, copia los atributos de la funcion de origen al Decorador, por defecto cuando una funcion es sustituida por 
# otra los atributos como __name__, y otros estados son sustituidos por la funcion del decorador, @warp evita esto devolviendo los atributos
# de la funcion original. se debe importar este decorador importandolo de la libreria functools

def porcentaje(func):
    @wraps(func) 
    def inner(x,y):
        """
        Esto es el decorador
        """
        result = (func(x,y)) * 100
        return result
    return inner

@porcentaje
def proporcion (a,b):
    """
    Retorna la proporcion de dos numeros
    """
    return a/b

ejecuta = proporcion(15,50)
print(ejecuta)
print("nombre funcion", proporcion.__name__)
print("Modulo", proporcion.__module__)
print("Descripcion", proporcion.__doc__)
print("Funcion real", proporcion.__wrapped__)



#  Los decoradores se puden combinar y se aplican de abajo hacia arriba por ejemplo colocalmos @deco1 y @deco2, se ejecutara primero la funcion en 
#  @deco2 y el resultado de la deco2 se pasara a deco1 y deco 1 dara el ultimo resultado o cambio a la funcion seria algo asi deco1(deco2(func))



def deco1(func):
    def inner():
        print("Soy deco1 ")
        return func() + "Soy Deco1 "
    return inner


def deco2(func):
    def inner():
        print("Soy deco2 ")
        return func() + "Soy deco2 "
    return inner 

@deco1
@deco2
def la_funcion():
    return "Soy la funcion "


print(la_funcion())

#otras funciones de functools son 
#     @lru_cache : Crea un cache con los ultimos elementos usados de mayor tamaño, esta decorador tiene dos metodos 
#         - func.cache_info()
#         - func.cache_clear()  
#     @singledipatch: Define una funcion generica y despacha otras funciones dependiendo el tipo del primer argumento tiene metodos.
#          - @func.register(type): regista  las otras funciones y revise el tipo de argumento. 
#
#       
