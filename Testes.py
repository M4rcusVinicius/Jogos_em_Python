arquivo = open(arquivo, "r")
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

arquivo.close()

n = random.randrange(0, len(palavras))
palavra_secreta = palavras[n].upper()
return palavra_secreta