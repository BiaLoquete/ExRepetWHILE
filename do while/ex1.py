n = 0
qnt = 0


while True:
    nota = float( input("Digite uma nota: "))
    qnt +=1
    n += nota

    if nota < 0:
        media = n/ qnt
        print(f"A média é: {media}")
        break
    f = str (input("Deseja continuar? (N/S): "))
    if f == "N":
        media = n/qnt
        print(f"A média é {media}")
        break

