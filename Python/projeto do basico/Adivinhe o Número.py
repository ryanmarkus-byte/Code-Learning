import random
numero_secreto = random.randint(1,100)
tentativas = 0
acertou = False

print("Bem vindo ao Adivinhe o Número!")
print("O programa gerou um numero inteiro aleatório entre 1 e 100, vc deve adivinha-lo.")

while not acertou:
    palpite_str = input("Qual o seu palpite? ")
    try:
        palpite = int(palpite_str)
        tentativas += 1

        if palpite > numero_secreto:
            print(f"Número alto! Tente novamente.")
            print()
        elif palpite < numero_secreto:
            print(f"Número baixo! Tente novamente.")
            print()
        else:
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas!")
            acertou = True
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        print()