import random

def jogar():
    print("="*50)
    print(f"{'Bem vindo ao jogo de Forca!':^50}")
    print("="*50)

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    print(palavras)

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)
    erros = 0

    while True:
        chute = input("Qual letra? ").strip().upper()
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    print(f"Letra {letra} encontrada na posição {index}")
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        if (erros == 6):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)

    if("_" not in letras_acertadas):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
    
    print("Fim do jogo")
    
if (__name__ == "__main__"):
    jogar()