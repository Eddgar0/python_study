# Subclases heredan todos los metodors y propiedades de la clase cual heredo. la ultima llamada tambien superclase

class Animal():
    def come(self, comida):
        print(f'Comiendo {comida}....')
    def duerme(self):
        print('Zzz...')

class Gato(Animal):
    def maulla(self):
        print('Miau!')

class Perro(Animal):
    def ladra(self):
        print('Guau!')

print(dir(Animal))
print(dir(Gato))
print(dir(Perro))

animal = Animal()
animal.come('Pizza')
animal.duerme()

misu = Gato()
misu.come('ratón')
misu.maulla()
misu.duerme()

bobi = Perro()
bobi.ladra()
bobi.duerme()

# Subclases pueden hacer override a los metodos heredados

class Chihuahua(Perro):
    def ladra(self):
        print('Guiu!')

cosita = Chihuahua()

cosita.ladra()
cosita.come('pollo')
cosita.duerme()

print(issubclass(Chihuahua, Perro))
print(issubclass(Chihuahua,Animal))
print(isinstance(cosita, Animal))


# Algunas veces queremos extender o modificar los metodos de la clase base o super clase
# para esto utilizamos super()

# En este primer ejemplo vemos como modificamos he hicimos override a __init__ pero duplicamos todo el codigo

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Astronauta(Persona):
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

print(vars(Persona('Juan', 'Perez')))
print(vars(Astronauta('Juan', 'Perez', 120000)))


# En este segundo ejemplo utilizamos super().metodo con esto no es necesario sobreescribir todo los atributos
# ni tampoco refernciar directamente a la clase base y funciona herencia de multiples clases. Ej:

class Astronauta(Persona):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        self.salario = salario

astro = Astronauta('Juan', 'Perez', 120000)
print(astro.nombre, astro.apellido, astro.salario)