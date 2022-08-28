# Calculadora de indice de masa corporal

# Necesitaría que el usuario ingrese por teclado su peso en KG y su estatura en CMS

# Si el imc es menoir a 19 : Delgadez
# Si el imc esta entre 20 y 25: Normal
# Si el imc esta entre 26 y 30: Sobrepeso
# Si el imc esta superior a 30: Obesidad

peso = int(input("Ingrese su peso en KG: "))
estaturaEnCentimetros = int(input("Ingrese su estatura en centímetros: "))
estaturaEnMetros = estaturaEnCentimetros / 100
imc = peso / (estaturaEnMetros * estaturaEnMetros)
print("Tu indice de IMC es: " + str(imc))

if imc < 20:
    print("Su estado de IMC es Delgadez")
if imc >= 20 and imc < 26:
    print("Su estado de IMC es Normal")
if imc >= 26 and imc < 30:
    print("Su estado de IMC es Sobrepeso")
if imc > 30:
    print("Su estado de IMC es Obesidad")
