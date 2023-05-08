try:
    numero_1 = float(input("Pone un numero: "))

    numero_2 = float(input("Pone otro numero: "))

    operador = input("Que operador vas a usar?: ")

    if operador == "+":
        print(numero_1 + numero_2)

    elif operador == "-":
        print(numero_1 - numero_2)

    elif operador == "/":
        print(numero_1 / numero_2)

    elif operador == "%":
        print(numero_1 % numero_2)

    elif operador == "*":
        print(numero_1 * numero_2)

    elif operador == "**":
        print(numero_1 ** numero_2)

    else:
        print("Invalido.")
except:
    print("Invalido")