def apresentar_usuario(nome, idade , cidade):
    print(f"Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}")

def calcular_media(nota1, nota2, nota3):
    resultado = (nota1 + nota2 + nota3)/3
    return resultado

apresentar_usuario("Ryan", 19, "Sao Paulo")

print()

media = calcular_media(1, 2, 3)
print(f"A média das notas é: {media}")