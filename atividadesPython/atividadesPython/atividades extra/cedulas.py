def inicio():
    valor = int(input("Digite o valor do saque: "))

    nota100 = valor // 100
    valor = valor % 100

    nota50 = valor // 50
    valor = valor % 50

    nota20 = valor // 20
    valor = valor % 20

    nota10 = valor // 10
    valor = valor % 10

    nota5 = valor // 5
    valor = valor % 5

    print(f"{nota100} cédulas de 100")
    print(f"{nota50} cédulas de 50")
    print(f"{nota20} cédulas de 20")
    print(f"{nota10} cédulas de 10")
    print(f"{nota5} cédulas de 5")

inicio()