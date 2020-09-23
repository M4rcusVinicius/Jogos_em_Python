import Forca
import Adivinhação

print("="*50)
print(f"{'Escolha o seu Jogo':^50}")
print("="*50)

while True:
    jogo = int(input("""
    Escolha um dos jogos disponíveis :
    |1| Forca
    |2| Adivinhação 
    Defina o jogo : """))

    if (jogo == 1):
        print("\nIniciando jogo da Forca ...\n\n")
        Forca.jogar()

    elif (jogo == 2):
        print("\nIniciando jogo d Adivinhação ...\n\n")
        Adivinhação.jogar()
    
    c = input("Digite qualquer letra para continuar : ").strip()
    if bool(c):
        print("Reiniciando o jogo...")
    else:
        break

    