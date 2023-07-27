numbers = list(map(int, input().split()))
n = numbers[0]
m = numbers[1]
lista = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happy = 0

for x in lista:
    if x in A:
        happy += 1
    elif x in B:
        happy -= 1


print(happy)