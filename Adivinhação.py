import random

def jogar():
    print("="*50)
    print(f"{'Bem vindo ao jogo de Adivinhação!':^50}")
    print("="*50)

    arquivo = open("Palavras.txt", "r")
    palavras = []

    for linhas in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    print(palavras)

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    dificuldade = int(input("""
    Escolha o nível de dificuldade :
    |1| Fácil
    |2| Médio
    |3| Difícil
    |4| Insano
    Defina o nível : """))

    if dificuldade == 1:
        tentativas = 20

    elif dificuldade == 2:
        tentativas = 10

    elif dificuldade == 3:
        tentativas = 5

    elif dificuldade == 4:
        tentativas = 1

    for rodada in range(1, tentativas + 1):
        print(f"\nTentativa {rodada} de {tentativas}")

        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("\033[31mVocê deve digitar um número entre 1 e 100!\033[m")
            continue

        if chute == numero_secreto:
            print(f"\033[32mVocê acertou e fez {pontos} pontos!\033[m")
            break
        else:
            if chute > numero_secreto:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif chute < numero_secreto:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos = (pontos - abs(numero_secreto - chute)) // dificuldade
        
        if rodada == (tentativas):
            print("\n\033[31mVocê errou todas a tentativas :/\033[m")
            print(f"Sua pontuação final é de {pontos} pontos")

    print("\nFim do jogo")
    if (__name__ == "__main__"):
        jogar()