import random
import os

def jogar():

    tema = define_tema()

    arquivo = arquivo_do_tema(tema)
    palavra_secreta = sorteia_palavra(arquivo)

    loop_jogo_forca(palavra_secreta)

def loop_jogo_forca(palavra_secreta):
    lista_historico = []

    print(f"\nA palavra secreta tem {len(palavra_secreta)} letras\n")
    letras = ["_" for letra in palavra_secreta]
    chute = ""
    erro = ""
    tentativa = 0

    while True:
        print_forca(tentativa, letras)
        print(f"Tentativa {tentativa + 1} de 7\n")

        if bool(chute) and erro == "":
            erro = print_historico_letras(lista_historico)
        
        print_erro(erro)
        
        chute, erro = pergunta_chute()
        lista_historico, erro = historico_de_letras(chute, lista_historico)

        if erro == "":
            if chute in palavra_secreta :
                index = 0
                for letra in palavra_secreta:
                    if chute == letra:
                        letras[index] = letra
                    index += 1
            else:
                tentativa = tentativa + 1

        if tentativa == 7:
            mensagem_perdedor(palavra_secreta)
            break
        elif "_" not in letras:
            mensagem_vencedor()
            break

def imprime_logo():
    os.system('cls') or None
    print("="*50)
    print(f"{'Bem vindo ao jogo de Forca!':^50}")
    print("="*50)

def define_tema():
    erro = ""
    while True:
        os.system('cls') or None
        print("="*50)
        print(f"{'Bem vindo ao jogo de Forca!':^50}")
        print("="*50)
        print("")
        print("|1| Frutas")
        print("|2| Objetos")
        print("|3| Animais")
        print("|4| Tudo")
        if erro == "n_invalido":
            print("\033[31mDigite apenas |1|, |2|, |3| ou |4|\033[m")
        try:
            tema = int(input("Escolha um dos temas para jogar : "))
            if tema == 1 or tema == 2 or tema == 3 or tema == 4: 
                break
            else:
                erro = "n_invalido"
        except:
            erro = "n_invalido"
    return tema

def arquivo_do_tema(tema):
    if tema == 4:
        tema = random.randrange(1,4)
    if tema == 1:
        arquivo = "Arquivo_Secreto//Frutas.txt"
    if tema == 2:
        arquivo = "Arquivo_Secreto//Objetos.txt"
    if tema == 3:
        arquivo = "Arquivo_Secreto//Animais.txt"
    return arquivo

def sorteia_palavra(arquivo):
    arquivo = open(arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    n = random.randrange(0, len(palavras))
    palavra_secreta = palavras[n].upper()
    return palavra_secreta

def print_forca(tentativa, letras):
    imprime_logo()
    
    desenha_forca(tentativa)
    print_letras(letras)

def pergunta_chute():
    alfabeto = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'Ç')
    erro = ""
    try:
        chute = input("Letra escolhida : ").strip().upper()
        if chute not in alfabeto:
            erro = "letra_invalida"
    except:
        erro = "letra_invalida"
    return chute, erro

def print_letras(letras):
    print(" ", end = "")
    for cont, letra in enumerate(letras):
        if cont == (len(letras) - 1):
            print(f"{letra} \n")
        else:
            print(letra, end = " ")

def print_erro(erro):
    if erro == "letra_repetida":
        print("\033[31mEssa letra já foi digitada\033[m\n")
    if erro == "letra_invalida":
        print("\033[31mDigite apenas letras de alfabeto\033[m")
    erro = ""
    
def historico_de_letras(chute, lista_historico):
    erro = ""
    if chute not in lista_historico:
        lista_historico.append(chute)
    else:
        erro = "letra_repetida"
    return (lista_historico, erro)

def print_historico_letras(lista_historico):
   
    if bool(lista_historico):
        print("Letras digitadas :")
        print("| ", end = "")
        for cont, letra in enumerate(lista_historico):
            if cont == (len(lista_historico) - 1):
                print(f"{letra} |\n")
            else:
                print(letra, end = " - ")

def mensagem_vencedor():
    print("Parabéns, você ganhou!")
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

def mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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

def desenha_forca(tentativa):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativa == 0):
        print (" |            ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(tentativa == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(tentativa == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(tentativa == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(tentativa == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(tentativa == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(tentativa == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (tentativa == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___  ", end="")

if(__name__ == "__main__"):
    jogar()