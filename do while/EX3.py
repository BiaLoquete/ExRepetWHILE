res = "S"
while res == "S":
    num = int (input("Digite: "))

    #quando o usuário digitar 999, a programação acaba
    if num == 999 or num < 0:
        print("Número muito grande!")
        break
        res = str(input("Deseja continuar? (S/N): "))
