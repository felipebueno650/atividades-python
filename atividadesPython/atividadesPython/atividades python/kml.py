def inicio():
    capacidade_tanque = float(input("Informe a capacidade do tanque (litros): "))
    litros_abastecidos = float(input("Informe a quantidade de litros abastecidos: "))
    km_percorridos = float(input("Informe a quilometragem percorrida desde o último abastecimento: "))

    consumo_medio = km_percorridos / litros_abastecidos

    litros_restantes = capacidade_tanque - litros_abastecidos
    autonomia = consumo_medio * litros_restantes

    print(f"\nConsumo médio do veículo: {consumo_medio} km por litro")
    print(f"Autonomia antes do abastecimento: {autonomia} km")

inicio()