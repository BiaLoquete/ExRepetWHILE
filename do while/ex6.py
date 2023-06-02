while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    menu = int(input("Escolha:\num1 - Somar\num2 - Multiplicar\num3 - Subtrair\num4 - Divisão\num5 - Sair do Programa\nR:"))
    if menu == 1:
        soma = num1 +num2
        print(f"Soma: {soma}")
    if menu == 2:
        m = num1 * num2
        print(f"Multiplicar: {m}")
    if menu == 3:
        sub = num1 - num2
        print(f"Subtrair: {sub}")
    if menu == 4:
        div = num1 / num2
        print(f"Divisão: {div}")
    if menu == 5:
        break