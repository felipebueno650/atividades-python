def inicio():

    lata = int(input("Quantas latas de refri você deseja(350ml): "))
    garrafa = int(input("Quantas garrafas de refri você deseja(600ml): "))
    garrafaLitro = int(input("Quantas garrafas de refri você deseja(2l): "))

    # calculoLata = (lata * 350) / 1000
    # calculoGarrafa = (garrafa * 600) / 1000
    # calculoGarrafaLitro = garrafaLitro * 2

    # calculoTotal = calculoLata + calculoGarrafa + calculoGarrafaLitro
    
    calculoTotal = ((lata * 350) / 1000) + ((garrafa * 600) / 1000) + (garrafaLitro * 2)

    print(f"A quantidade em litros que voce comprou foi: {calculoTotal} litros")
    
    
    

inicio()