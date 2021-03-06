import random

def jogar():

    Capa()
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    total_de_tentativas = dificuldade()

    for rodada in range(1, total_de_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if chute == numero_secreto:
            mensagem_vencedor(pontos)
            break
        else:
            if chute > numero_secreto:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif chute < numero_secreto:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos = pontos - abs(numero_secreto - chute)
        
            if total_de_tentativas == rodada:
                mensagem_perdedor(numero_secreto)

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
    return total_de_tentativas

def mensagem_vencedor(pontos):
    print("Parabéns, você ganhou!")
    print(f"Você acertou e fez {pontos} pontos!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(numero_secreto):
    print("Você perdeu")
    print(f"O número secreto era {numero_secreto}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
    jogar()
