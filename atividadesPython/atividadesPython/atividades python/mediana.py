def inicio():

    nota1 = float(input("informe a primeira nota: "))
    nota2 = float(input("informe a segunda nota: "))
    nota3 = float(input("informe a terceira nota: "))

    pesoNota1 = nota1 * 2
    pesoNota2 = nota2 * 3
    pesoNota3 = nota3 * 5

    resultadoFinal = (pesoNota1 + pesoNota2 + pesoNota3) / 10

    print("sua nota foi: ", resultadoFinal)
    if(resultadoFinal < 6.0):
        print("você foi reprovado")
    else:
        print("você foi aprovado!")

inicio()