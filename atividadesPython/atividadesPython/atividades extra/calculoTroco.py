def inicio():
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    dinheiro = float(input("Digite o valor entregue ao vendedor: "))

    troco = dinheiro - preco

    print(f"Você comprou um produto ({produto}) por R$ {preco:.2f} e entregou ao vendedor R$ {dinheiro:.2f} em dinheiro.")
    print(f"Você vai receber R$ {troco:.2f} de troco. Volte sempre!")

inicio()