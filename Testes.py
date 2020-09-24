import random
import os

def jogar():
    
    imprime_logo()
    tema = define_tema()

    arquivo = arquivo_do_tema(tema)
    palavra_secreta = sorteia_palavra(arquivo)

    print(f"\nA palavra secreta tem {len(palavra_secreta)} letras\n")
    jogo_forca(palavra_secreta)

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

def jogo_forca(palavra_secreta):
    letras = ["_" for letra in palavra_secreta]
    tentativa = 0
    while True:
        if tentativa == 7:
            mensagem_perdedor(palavra_secreta)
            break
        elif "_" not in letras:
            mensagem_vencedor()
            break

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


if(__name__ == "__main__"):
    jogar()