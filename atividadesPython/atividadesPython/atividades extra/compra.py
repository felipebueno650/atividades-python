def inicio():
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    desconto = preco * 0.10
    valor_final = preco - desconto

    print(f"Você comprou um produto ({produto}) por R$ {preco:.2f} e acaba de ganhar um desconto de 10%.")
    print(f"Assim você vai pagar apenas R$ {valor_final:.2f} pelo seu produto. Volte sempre!")

inicio()