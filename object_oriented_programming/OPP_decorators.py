# @property
# este decorador es usado para realizar getter y setter de una clase,
# @property automaticamente crea estos getters y setters sin sacrificar la lectura en el codigo
# tu accedes directamente a la propidedad y el decorador property lo redirige al getter/setter

class Producto:
    def __init__(self, cantidad):
        self._cantidad = cantidad
    @property
    def cantidad(self):
        print('Accediendo cantidad..')
        return self._cantidad
    
prod = Producto(10)
prod.cantidad

# prod.cantidad = 20
# en este caso si la clase solo tiene property para el getter, se asume que el atributo es solo lectura.
# para poder ser modificado se crear el setter con property.

class Producto:
    def __init__(self, cantidad):
        self._cantidad = cantidad
    def get_cantidad(self):
        print('Accediendo cantidad..')
        return self._cantidad
    def set_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError('Cantidad debe ser >= 0')
        self._cantidad = cantidad
    def del_cantidad(self):
        del self._cantidad
    cantidad = property(get_cantidad, set_cantidad) #Este caso usamos la forma la funcion y no como decorador

prod = Producto(10)
print(prod.cantidad)
prod.cantidad = 30
print(prod.cantidad)
print(prod.cantidad + 40)

# la otra forma mas pythonica de hacerlo es usando decoradores correspondientes

class Producto:
    def __init__(self, cantidad):
        self._cantidad = cantidad
    @property
    def cantidad(self):
        print('Accediendo cantidad..')
        return self._cantidad
    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError('Cantidad debe ser >= 0')
        self._cantidad = cantidad
    
prod = Producto(10)
print(prod.cantidad)
prod.cantidad = 30
print(prod.cantidad)
print(prod.cantidad + 40)


# @classmethod
# el decorador @classmethod the permite proveer constructores alternativos a una clase, ejemplo si tienes 
# una clase circulo, puedes calcular su area usando radio, o el perimetro. En el siguiente ejemplo utilizaremos
# este decorador para que la clase circulo pueda utilizar para construir tanto el radio como el perimetro.
# @classmethod recivira una clase en vez de la instancia como primer argumento.
from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def __repr__(self):
        return 'Circulo({})'.format(self.radio)
    @classmethod
    def from_circunferencia(cls, circunferencia):
        radio = circunferencia / (2*pi)
        return cls(radio)
    @property
    def area(self):
        return pi * self.radio**2
    @property
    def circunferencia(self):
        return 2 * pi * self.radio


c1 = Circulo(10)
print(repr(c1))
print(c1.radio)
print(c1.circunferencia)

# Notese que el decorador @classmethod nos permitio instaciar la clase sendo la circunferencia del circulo. 
c2 = Circulo.from_circunferencia(62.83185307179586)
print(repr(c2))
print(c2.radio)
print(c2.circunferencia)
print(c2.area)


