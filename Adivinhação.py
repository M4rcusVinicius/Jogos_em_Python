print("="*50)
print(f"{'Bem vindo ao jogo de Adivinhação!':^50}")
print("="*50)

numero_secreto = 42

chute = int(input("Digite o seu número: "))
print("Você digitou: ", chute)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")
