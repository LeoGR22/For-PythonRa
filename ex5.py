lista = []
contador = 0
for i in range(1,11):
    lista.append(int(input("Digite 10 valores")))

for j in lista:
    if j % 2 == 0:
        contador += 1

print(contador)