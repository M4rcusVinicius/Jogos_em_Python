import random

def jogar():

    Capa()
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    dificuldade()

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

def Capa():
    print("="*50)
    print(f"{'Bem vindo ao jogo de Adivinhação!':^50}")
    print("="*50)

def dificuldade():
    print("|1| Fácil")
    print("|2| Médio")
    print("|3| Difícil")
    nível = int(input("Escolha o nível de dificuldade : "))

    if(nível == 1):
        total_de_tentativas = 20
    elif(nível == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

if(__name__ == "__main__"):
    jogar()
