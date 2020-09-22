import random


def jogar():

    Capa()
    palavra_secreta = palavra()
    print(palavra_secreta)
    letras_acertadas = letras(palavra_secreta)
    print_letras(letras_acertadas)

    erros = 0

    while True:
        chute = input("Qual letra? ").strip().upper()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        if erros == 7:
            mensagem_perdedor(palavra_secreta)
            break
        if "_" not in letras_acertadas:
            mensagem_vencedor()
            break

        print_letras(letras_acertadas)


# ==========================================================
# Funções referentes a exibição de imagens ou textos
# ==========================================================

def Capa():
    print("="*50)
    print(f"{'Bem vindo ao jogo de Adivinhação!':^50}")
    print("="*50)

def print_letras(letras_acertadas):
    print("|| ", end = "")
    for cont, letra in enumerate(letras_acertadas):
        if cont == (len(letras_acertadas) - 1):
            print(f"{letra} ||")
        else:
            print(letra, end = " - ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

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
    print("Puxa, você foi enforcado!")
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


# ==========================================================
# Funções referentes a formatação de strings
# ==========================================================

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def letras(palavra):
    return ["_" for letra in palavra]


# ==========================================================
# Funções de acesso ao banco de dados
# ==========================================================

def palavra():
    tema = int(input("""
    |1| Frutas
    |2| Objetos
    |3| Animais
    Escolha um dos temas para jogar : 
    """)).strip
    if tema == 1:
        arquivo_escolhido = "Frutas.txt"
    if tema == 2:
        arquivo_escolhido = "Objetos.txt"
    if tema == 3:
        arquivo_escolhido = "Animais.txt"
    arquivo = open("arquivo_escolhido", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if(__name__ == "__main__"):
    jogar()
