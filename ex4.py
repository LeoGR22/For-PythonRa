import random
lista = []

x = 0
y = 0
for i in range(1,9):
    lista.append(input("Digite 8 valores"))

x = random.choice(lista)
y = random.choice(lista)
soma = int(x)+int(y)
print(soma)
