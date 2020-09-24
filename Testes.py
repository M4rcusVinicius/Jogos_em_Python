import os

arquivo = open("Arquivo_Secreto//Animais.txt", "r")
palavras = []

for linha in arquivo:
    linha = linha.strip().upper()
    palavras.append(linha)

arquivo.close()

palavras_erradas = []

alfabeto = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'Ç')
for palavra in palavras:
    for letra in palavra:
        if letra not in alfabeto:
            palavras_erradas.append(palavra)

os.system('cls') or None
print(f"Palavras erradas : {palavras_erradas}")