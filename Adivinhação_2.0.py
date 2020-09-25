import random
import os


def jogar():
    numero_secreto = random.randrange(1,101)
    pontos = 1000
    rodada = 0
    erro = ""
    msg = ""

    n_nivel = define_dificuldade()
    tentativas, referencia = define_tentativas(n_nivel)

    while True:
        print_tentativas(rodada, referencia, tentativas)
        
        if erro == "n_invalido":
            print("\033[31mApenas digite números entre 1 e 100\033[m")
            msg = ""

        print_msg(msg)

        chute, erro = pergunta_chute()

        if erro == "":
            rodada += 1

            if chute == numero_secreto:
                print("Você ganhou")
                break
            
            else:
                if chute > numero_secreto:
                    msg = "maior" 
                elif chute < numero_secreto:
                    msg = "menor" 
                pontos -= abs(numero_secreto - chute)
                
                if tentativas == rodada:
                    print("Você perdeu")
                    break

def print_logo():
    os.system('cls') or None
    print("="*50)
    print(f"{'Bem vindo ao jogo de Adivinhação!':^50}")
    print("="*50)

def define_dificuldade():
    erro = ""
    while True:
        os.system('cls') or None
        print_logo()

        print("|1| Fácil")
        print("|2| Médio")
        print("|3| Difícil")

        if erro == "n_invalido":
            print("\033[31mDigite apenas |1|, |2| ou |3|\033[m")
        try:
            nivel = int(input("Escolha a dificuldade : "))
            if nivel == 1 or nivel == 2 or nivel == 3: 
                break
            else:
                erro = "n_invalido"
        except:
            erro = "n_invalido"
    return nivel

def define_tentativas(n_nivel):
    if(n_nivel == 1):
        tentativas = 20
        referencia = 1
    elif(n_nivel == 2):
        tentativas = 10
        referencia = 2
    else:
        tentativas = 5
        referencia = 4
    return tentativas, referencia

def pergunta_chute():
    erro = ""
    chute = ""
    try:
        chute = int(input("\nDigite um número : "))
        if 0 > chute or chute > 100:
            erro = "n_invalido"
    except:
        erro = "n_invalido"
    return chute, erro

def print_msg(msg):
    if msg != "":
        print("\033[31mVocê errou !\033[m")
        if msg == "maior":
            print("O seu chute foi MAIOR do que o número secreto.")
        if msg == "menor":
            print("O seu chute foi MENOR do que o número secreto.")

def print_tentativas(rodada, referencia, tentativas):
    print_logo()

    mtp_atual = (rodada*referencia*2)
    mtp_final = (tentativas*referencia*2) - mtp_atual

    print("\n[", end="")
    print("=" * mtp_atual, end="")
    print(" "*mtp_final, "]")

    print("[", end="")
    print("=" * mtp_atual, end="")
    print(" "*mtp_final, "]\n")

if(__name__ == "__main__"):
    jogar()
