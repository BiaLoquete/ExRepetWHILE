while True :
    ini = str (input("Digite seu gênero (M/F): "))

    #obriga o usuário a digitar começar
    if ini != "M" and ini != "F":
        print("Está errado!")
        ini = str(input("Digite seu gênero (M/F): "))
    else:
        break