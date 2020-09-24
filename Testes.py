import random
import os

erro = ""

def jogar():
    
    imprime_logo()
    tema = define_tema()

    arquivo = arquivo_do_tema(tema)
    palavra_secreta = sorteia_palavra(arquivo)

    print(f"\nA palavra secreta tem {len(palavra_secreta)} letras\n")
    loop_jogo_forca(palavra_secreta)

def loop_jogo_forca(palavra_secreta):
    letras = ["_" for letra in palavra_secreta]
    tentativa = 0
    while True:
        print_forca(tentativa, letras)
        chute = input("Letra escolhida : ").strip().upper()

        adciona_conquistas(chute, letras, palavra_secreta, tentativa)

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
    print("")
    print("|1| Frutas")
    print("|2| Objetos")
    print("|3| Animais")
    print("|4| Tudo")
    tema = int(input("Escolha um dos temas para jogar : "))
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

def adciona_conquistas(chute, letras, palavra_secreta, tentativa):
    if not bool(erro):
        if chute in palavra_secreta :
            marca_chute_correto(chute, letras, palavra_secreta)
        else:
            tentativa += 1
    else:
        erro = ""

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

def print_forca(tentativa, letras):
    imprime_logo()
    
    desenha_forca(tentativa)
    print_letras(letras)
    
    print_historico_letras(lista)
    print_erro()
    erro = ""

def print_letras(letras):
    print(" ", end = "")
    for cont, letra in enumerate(letras):
        if cont == (len(letras) - 1):
            print(f"{letra} \n")
        else:
            print(letra, end = " ")

def historico_de_letras(chute):
    lista = {}
    if chute not in lista:
        lista.append(chute)
    else:
        erro = "letra_repetida"
    return lista, erro

def print_historico_letras():
    historico_de_letrasta, erro = historico_de_letras()
    
    if bool(historico_de_letras):
        print("Letras digitadas :")
        print("| ", end = "")
        for cont, letra in enumerate(historico_de_letras):
            if cont == (len(historico_de_letras) - 1):
                print(f"{letra} |\n")
            else:
                print(letra, end = " - ")
        
    if erro == "letra_repetida":
        print("\033[31mEssa letra já foi digitada\033[m")
    erro = ""

def print_erro():
    if erro == "letra_repetida":
        print("\033[31mEssa letra já foi digitada\033[m")

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