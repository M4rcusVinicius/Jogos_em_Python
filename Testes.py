while True:
    while True:
        alfabeto = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', 'Ç')
        try:
            chute = input("Letra escolhida : ").strip().upper()
            if chute in alfabeto:
                break
            else:
                print("\033[31mDigite apenas letras de alfabeto\033[m")
        except:
            print("\033[31mDigite apenas letras de alfabeto\033[m")
    print("\033[32mAprovado\033[m")
    if chute == "Z":
        break