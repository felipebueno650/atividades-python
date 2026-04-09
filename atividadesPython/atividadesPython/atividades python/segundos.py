def inicio():
    horas = int(input("Informe a hora: "))
    minutos = int(input("Informe os minutos: "))
    segundos = int(input("informe os segundos: "))

    resultado = segundos + minutos * 60 + horas * 3600

    print(f"Deu um total de: {resultado} segundos")

inicio()