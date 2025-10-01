print("Loop com for: quadrado de cada numero da lista")
numeros = [0,1,2,3,4,5,6,7,8,9]
for numero_for in numeros:
    numero_for = numero_for**2
    print(numero_for)

print()

print("Loop com while: soma dos numeros de 0 a 10")
soma = 0
numero_while = 1
while numero_while <= 10:
    soma += numero_while
    numero_while += 1
print(soma)