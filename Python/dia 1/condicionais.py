numero = input("Digite um numero inteiro: ")
numero_digitado = int(numero)

if numero_digitado > 0:
    print("Numero positivo.")
elif numero_digitado < 0:
    print("Numero negativo.")
elif numero_digitado == 0:
    print("Seu numero é zero.")
else:
    print("Seu numero n se encaixa em nenhuma das condicoes.")