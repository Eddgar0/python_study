
#Objects pueden ser medidos utilizando el metodo
# __len__
# cuando un objeto tiene este metodo es llamado por la funcion len(obj)
# Objetos pueden ser contenedores para esto deben utilizar el metodo
# __contains__
# ese metodos especial es llamado or in y not in
#debe retornar True o False

class Departamento:
    def __init__(self, astronautas, ingenieros):
        self.astronautas = astronautas
        self.ingenieros = ingenieros
    def __contains__(self, p):
        return p in self.astronautas or p in self.ingenieros
    def __len__(self):
        return len(self.astronautas) + len(self.ingenieros)
    def __iter__(self): # Ver iteratable protocol
        yield from self.astronautas
        yield from self.ingenieros
    def __reversed__(self): #ver iterable protocol
        yield from reversed(self.ingenieros)
        yield from reversed(self.astronautas)


    
nasa = Departamento(['Alicia'], ['Bob', 'Jose', 'Julia'])
len(nasa)
print('Alicia' in nasa)
print('Pedro' in nasa)
print('Pedro' not in nasa)

# Iterables protocols
# iteables son objetos que pueden ser iterados y un iterador son objetos que mantienen seguimiento a una iteracion. 
# Para que una clase sea un iterable o iterator, se se tiene que implementar los metodos
# __iter__: Este es llamado cuando un iterador es necesitado ej. llamado por iter() o un for loop
# __next_: llamado duarante la iteracin por nex(), debe retornar el sigiente elemento. 

print(list(nasa))

for persona in nasa:
    print(persona)

# El metodo especial __reversed__ es usado para retornar un iterador pero en orden reverso
print(reversed(nasa))
print(list(reversed(nasa)))


# Procolo Acceso customizado de elementos en la clase
# Para lograr el acceso customizado necesitamos 3 metodos:
#
# __getitem__: llamado para implentar 'inst[index]'
# __setitem__: Llamado para implementar 'inst[index] = value'
# __delitem__: llamado para implementar 'del inst[index]'

class Equipo:
    def __init__(self, miembros):
        self.miembros = miembros
    def __getitem__(self, index):
        return self.miembros[index]
    def __setitem__(self, index, value):
        # Los siguiente indica que nos asegure que los nombres esten capitalizados
        self.miembros[index] = value.title()
    def __delitem__(self, index):
        del self.miembros[index]

licey = Equipo(['Albert Pujols', 'Tito Rodriguez', 'Pedro Martinez'])

print(licey[2])
print(licey[:2])
print('Pedro Martinez' in licey)
licey[1] = 'alex rodriguez'
print(licey[1])
del(licey[2])
print(list(licey))

# Para mappings
# mappings es un contenedor que mapea key y valores, como por ejemplos dictionaries en python
# Para implementar acceso customizado en mappins solo implementamos los mismos tres metodos mas un 
# adicional :
# __missing__




# Context Manager
# Contex managers allows to use the 'with' sentence with our instance
# Like for example when we use with open as f
# For classes support context manager it must implement the specials method:
# __enter__ 
# __exit__
from datetime import datetime

class Timer:
    def __init__(self):
        self.start = self.stop = self.time = self.error = None
    def __enter__(self):
        print('__enter__ called')
        self.start = datetime.now()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ called')
        self.stop = datetime.now()
        self.time = self.stop - self.start
        if exc_type is not None:
            self.error = exc_type
        return True
    def print_results(self):
        print('The code took {}s to execute:'.format(self.time))
        print('    Start time:', self.start)
        print('    end   time:', self.stop)
        if self.error is not None:
            print('The code failed with a', self.error)

n = 1000000
with Timer() as timer:
    x = n**n

timer.print_results()

with Timer() as timer:
    x = 8 + '2'

timer.print_results()

