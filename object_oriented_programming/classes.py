# Clases son el modelo de un objeto y las instancias son los objetos basados en estos modelos
# Atributos: son caracteristicas de una Clase u objeto y crean dentro de la Clase. 

class Gato:
    nombre_cientifico = 'Felis Silvestris Catus'

# Las instancias se crean a partir de la clase y heredan todos sus atributos:

gato1 = Gato()
gato2 = Gato()

print('Instancia gato1:', gato1)
print('Instancia gato2:', gato2)
print('Se observa claramente que gato1 y gato2 son dos instancias diferentes')

print('nombre_cientifico gato1', gato1.nombre_cientifico)
print('nombre_cientifico gato2', gato2.nombre_cientifico)

# Se pueden agrear atributos directamente a la clase, y seran heredaras por las demas instancias:

Gato.nombre_comun = 'Gato'

print('gato1 nombre comun:', gato1.nombre_comun)
print('gato2 nombre comun:', gato2.nombre_comun)

# A cada una de las instancias podemos agregarles propiedades unicas, cual pueden ser diferentes a las clases o a otras instancias:
gato1.nombre = 'Michi'
print('Atributo nombre en gato1', gato1.nombre)

# si intentamos usar el atributo en la Clase Gato o gato2 nos dara un attribute Error
print('Imprimiendo atributos en instalacia gato2')
try: 
    print(gato2.name)
except AttributeError as e:
    print(e)

print('Imprimiendo atributos en Clase gato')
try: 
    print(gato2.name)
except AttributeError as e:
    print(e)

# Metodos son funciones que se crean dentro de una Clase.

class Perro:
    def ladra(self): 
        print('Guau')
    def multiladrido(self, veces):
        for x in range(veces):
            print('Guau')

perro1 = Perro()
perro1.ladra() # Los metodos estan atados a las instancias, y deben ser llamados()
perro1.multiladrido(3)

# Metodos no pueden ser llamados desde la Clase. 
try:
    Perro.ladra()
except TypeError as e:
    print(e)

# self es declarado como primer parametro en los metodos
# nunca es passado cuando se llaman los metodos
# self es una variable que hace referencia a las instancias

# self es usado para acceder otros atributos dentro de la clase

class Perro:
    def ladra(self): 
        print(self.nombre, 'dice Guau')
    def multiladrido(self, veces):
        for x in range(veces):
            self.ladra()

bobi = Perro()
bobi.nombre = 'bobi'
bobi.ladra()
bobi.multiladrido(3)

# El memto __init__ es un metodo especial para inicializar el instancias y es llamado automaticamente cuando una nueva instacia es creada

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre #define los atributos de la instancia
    def ladra(self): 
        print(self.nombre, 'dice Guau')
    def multiladrido(self, veces):
        for x in range(veces):
            self.ladra()

bobi = Perro('Bobi')
print(bobi.nombre)
bobi.ladra()
lassy = Perro('Lassy')
lassy.ladra()

# Instrospeccion de clase, se puede usar dir() y var para hacer instronspeccion de clase

class Gato:
    '''Representa un Gato'''
    nombre_cientifico = 'Felis Silvestris Catus'
    def maulla(self):
        '''Haz el gato maullar.'''
        print('Miau!')

gato = Gato()
print(dir(Gato))
print(dir(gato))
print(vars(Gato)) 
help(Gato)

# Python no tiene metodos privados, en python se utiliza como convencion que los metodos y propiedades privados comienzan con _underscore

class Gato:
    '''Representa un Gato'''
    nombre_cientifico = 'Felis Silvestris Catus'
    def maulla(self):
        '''Haz el gato maullar.'''
        print('Miau!')
    def _plan_conquista(self):
        print('Cargando plan...')

gato = Gato()
gato._plan_conquista()
help(Gato)

# Python usa las propiedades __repr__ y __str__, el primero es usado para realziar una representacion de la Clase de manera formal y __str__ de manera
# mas informal, cuando se usa print imprimira la rept, y cuando se usa str() dara la informal

class Gato:
    '''Representa un Gato'''
    def __init__(self,nombre):
        self.nombre = nombre
    def __repr__(self):
        return 'Gato({!r})'.format(self.nombre)
    def __str__(self):
        return self.nombre
    def maulla(self):
        '''Haz el gato maullar.'''
        print('Miau!')

gato = Gato('Pintas')
print(str(gato))
print(gato)

 #### otros metodos especiales ####
 # __bytes__
 # __format__
 # __bool__

 # Sobrecarga de operadores, operadors overloading
 # La sobrecarga de operadores es simplemente reutilziar los metedos\
 # Especiales de los operadores sobre tu clase
 # Por ejemplo, el metodo __add__ es el metodos especial cual python
 # utiliza para sumar si implementamos este metodo en la clase
 # podemos utilizar '+' para sumar:

class Gato():
    def __init__(self, nombre, peso):
       self.nombre = nombre
       self.peso = peso
    def __str__(self):
        return self.nombre
    def __add__(self, otro):
        if hasattr(otro,'peso'):        
            return self.peso + otro.peso
        return self.peso + otro
    def maulla():
        print('Miau')

misu = Gato('Misu', 20)
felix = Gato('Felix', 13)
total_peso = misu + felix
print('{} pesa {} libras y {} pesa {}, ambos gatos pesan {}'.format(misu, misu.peso, felix, felix.peso, total_peso))

