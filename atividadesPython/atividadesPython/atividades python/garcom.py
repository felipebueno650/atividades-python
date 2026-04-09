def inicio():
    valor_gasto = float(input("Informe o valor gasto no restaurante: "))

    taxa_garcom = valor_gasto * 0.10
    resultado = valor_gasto + taxa_garcom

    print(f"\nO valor da gorjeta do garçom ficou em: R$ {taxa_garcom}")
    print(f"E o valor total da conta foi: R$ {resultado}")

inicio()