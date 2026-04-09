def inicio():
    reais = float(input("Informe o valor em reais: "))
    taxa_dolar = float(input("Informe a taxa de câmbio do dólar para reais: "))

    valor_em_dolar = reais / taxa_dolar

    print(f"\nValor convertido em dólar: {valor_em_dolar}")

inicio()