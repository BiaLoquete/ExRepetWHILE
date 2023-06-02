par = 0

while True:
    ini = int(input("Digite um número (digite 0 para parar): "))
    if ini % 2 == 0:
        par += ini
    if ini == 0:
        print(f"A soma dos números pares é: {par}")
        break