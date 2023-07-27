import random as rd
from encodings import utf_8
def guesser():
    n = rd.randint(1,10)
    guess = int(input('write a number'))

    while guess!= n:
        print('Ups is not that') 
        guess = int(input('write a number'))
    else:
        print(f'You Got it is {guess}')

def test_lambda():
    cod_players=[
        {'name':'Ore', 'kills':24, 'deaths':3},
        {'name':'jabun', 'kills':10, 'deaths':9},
        {'name':'Ore', 'kills':19, 'deaths':7},
        {'name':'puffy', 'kills':5, 'deaths':8},
    ]

    print('Which is the player with max Kills?')
    print(max(cod_players, key=lambda x: x['kills'])['name'])

    print('Which is the player with More Deaths?')
    print(max(cod_players, key=lambda x: x['deaths'])['name'])

    print('Which is the player with better performance?')
    print(max(cod_players, key=lambda x: x['kills'] - x['deaths'])['name'])

    print('Which is the player with lowest performance?')
    print(min(cod_players, key=lambda x: x['kills'] - x['deaths'])['name'])

def sprint(*args, sep=' ', end='\n'):
    string = [str(x) for x in args]
    return sep.join(string) + end

def myabs(n):
    if n < 0: 
        return -n
    else:
        return n

def mypow(x,y,z=None):
    if z:
        return x**y % z
    else:
        return x**y

def todos(it):
    for i in it:
        if not i:
            return False
    return True

def alguno(it):
    for i in it:
        if  i:
            return True
    return False
_sentinel = object()
def minimo(it, *, key=None, default=_sentinel):
    if not it and default is not _sentinel:
        return default
    key = key or (lambda x: x)
    lkey, lval = key(it[0]), it[0]
    for v in it[1:]:
        kv = key(v)
        if lkey > kv :
            lkey,lval = kv, v
    return lval
            
def simple_calc(*args,operand):
    res=0
    if operand == '+':
        for v in args:
            res+= v
    return res



# PLAYGROUND
print(chr(0x1f40d))
print(bin(0x1f40d))

print(utf_8.encode('f'))
print(bin(ord('f')))