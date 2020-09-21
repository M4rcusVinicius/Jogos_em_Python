print("="*50)
print(f"{'Bem vindo ao jogo de Adivinhação!':^50}")
print("="*50)

numero_secreto = 42

chute = int(input("Digite o seu número: "))
print("Você digitou: ", chute)

maior = chute > numero_secreto
menor = chute < numero_secreto

if (numero_secreto == chute):
    print("Você acertou!")
else:
    if chute > numero_secreto:
        print("O seu chute foi maior do que o número secreto!")
    elif chute < numero_secreto:
        print("O seu chute foi menor do que o número secreto!")

print("Fim do jogo")