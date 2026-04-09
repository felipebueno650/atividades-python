def inicio():
    salario = float(input("Digite o valor do salário mínimo: "))
    quilowatts = float(input("Digite a quantidade de quilowatts consumida: "))

    valor_quilowatt = (salario / 7) / 100
    valor_total = valor_quilowatt * quilowatts

    print(f"Valor de cada quilowatt: R$ {valor_quilowatt:.2f}")
    print(f"Valor total a pagar: R$ {valor_total:.2f}")

inicio()