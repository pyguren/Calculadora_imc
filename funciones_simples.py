
def calcularIMC(peso, estaturaEnMetros):
    imc = peso / (estaturaEnMetros * estaturaEnMetros)
    return imc

def pedirIMC():

    peso = float(input("Ingrese su peso en KG: "))
    estaturaEnCentimetros = int(input("Ingrese su estatura en centímetros: "))
    estaturaEnMetros = estaturaEnCentimetros / 100
    imc = calcularIMC(peso, estaturaEnMetros)
    print("Tu indice de IMC es: " + str(imc))

    if imc < 20:
        print("Su estado de IMC es Delgadez")
    if imc >= 20 and imc < 26:
        print("Su estado de IMC es Normal")
    if imc >= 26 and imc < 30:
        print("Su estado de IMC es Sobrepeso")
    if imc > 30:
        print("Su estado de IMC es Obesidad")
        
print("Calcular el IMC de la primera persona")
pedirIMC()
print("Calcular el IMC de la segunda persona")
pedirIMC()
print("Calcular el IMC de la tercera persona")
pedirIMC()