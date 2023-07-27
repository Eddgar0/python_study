# Las excepciones tienen una jerarquiar la cuspide de la jerarquia de execpciones es BaseExcepcion, y todas las Excepciones heredan de esta
'''
BaseException
|--- SystemExit
|--- KeyboardInterrupt
|--- GeneratorExit
|--- Execption
|    |--- StopIteration
|    |--- ArithmeticError
|    |    |--- FloatingPointError
|    |    |--- OverflowError
|    |    |--- ZeroDivisionError
|    |--- AssertionError
|    |--- AttributeError
|    |--- BufferError
|    |--- EOFError
|    |--- ImportError
|    |--- LookupError
|    |    |--- IndexError
|    |    |--- KeyError 

'''
# Try/except atrapara todas las excepciones de la clase y todas las subclases de esta
#
# Es posible definir nuevas excepciones, las excepciones es como cualquier otra clase. Todas las excepciones definidas por el usuario
# deben heredar de la clase Exception o una de sus subclases. 

class MyExcepcion(Exception):
    pass
e = MyExcepcion('Error!') 
print(repr(e))
print(e.args)

# Mejor ejemplo

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class SalarioMuyBajitoError(ValueError):
    pass
class Astronauta(Persona):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        if salario < 15000:
            raise SalarioMuyBajitoError('El salario es muy bajito')
        self.salario = salario

# astro = Astronauta('Juan', 'Palotes', 9000)

# En el primer ejemplo creamos la clase de error con el cuerpo pass, podemos hacerlo mas complejo e interesante
# sobreescribiendo los metodos __init__ y __str__

class SalarioMuyBajitoError(ValueError):
    def __init__(self, salario):
        super().__init__(salario)
        self.salario = salario
    def __str__(self):
        return ('El minimo de salario anual debe ser sobre los ${}'.format(self.salario))
    
e = SalarioMuyBajitoError(9000)
print(e.args)
print(e)
raise e