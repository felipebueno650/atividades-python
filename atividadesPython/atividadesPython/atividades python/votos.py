def inicio():
    votos_brancos = int(input("Informe o número de votos brancos: "))
    votos_nulos = int(input("Informe o número de votos nulos: "))
    votos_validos = int(input("Informe o número de votos válidos: "))

    total_eleitores = votos_brancos + votos_nulos + votos_validos

    perc_brancos = (votos_brancos * 100) / total_eleitores
    perc_nulos = (votos_nulos * 100) / total_eleitores
    perc_validos = (votos_validos * 100) / total_eleitores

    print(f"\nTotal de eleitores: {total_eleitores}")
    print(f"Percentual de votos brancos: {perc_brancos}%")
    print(f"Percentual de votos nulos: {perc_nulos}%")
    print(f"Percentual de votos válidos: {perc_validos}%")

inicio()