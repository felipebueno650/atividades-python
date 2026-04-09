def inicio():
    distancia = float(input("Digite a distância percorrida em km: "))
    litros = float(input("Digite a quantidade de combustível gasta: "))
    preco = float(input("Digite o preço do litro do combustível: "))

    consumo = distancia / litros
    custo = litros * preco

    print(f"Consumo médio: {consumo:.2f} km/l")
    print(f"Custo total da viagem: R$ {custo:.2f}")

inicio()