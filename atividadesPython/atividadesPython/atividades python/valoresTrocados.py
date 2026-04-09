def inicio():
    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))

    aux = num1
    num1 = num2
    num2 = aux

    print("\nValores após a troca:")
    print(f"Primeiro número: {num1}")
    print(f"Segundo número: {num2}")

inicio()