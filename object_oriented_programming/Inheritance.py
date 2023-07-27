# Multiples Herencias
# En python una clase puede heredar de multiples superclases, heredando todas sus propiedades y metodos. 

class Pato:
    def grazna(self):
        print('Quack!')
    def nada(self):
        print('Nadando en superficie...')

class Castor:
    def construye_dique(self):
        print('Contruyendo dique...')
    def nada(self):
        print('Nadando bajo agua...')

class Ornitorrinco(Castor, Pato):
    def puya(self):
        print('Puyando enemigo...')

ferry = Ornitorrinco()
print(dir(ferry))
ferry.construye_dique()
ferry.grazna()
ferry.nada()
ferry.puya()

# Diamantes:
# Como en python todos los objetos heredan de object class una clase que hereda de dos superclases 
# y ambas superclases hereda de objeto al diagramar tendra forma de diamente

# Method Resolution Order (MRO):
# Las clases tiene un atributo especial llamado __mro_.
# __mro__ un tupla de clases, de cual muestra el orden que se hizo la resoluciond e atributos y metodos de la herencia. 

print(Ornitorrinco.__mro__)

# Usando super() con multiples herencias. 
# Cuando se usa super en un clase que hereda de varias superclases, la instuccion super() sigue el orden del MRO. super().metodo llamara 
# el metodo de la siguiente clase en el MRO. 
# Si la clase cual llamo super() tambien tiene otro super() el metodo de la clase siguiente del MRO tambien sera llamado.
#  
# dd
