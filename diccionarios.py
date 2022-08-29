diccionario= {
    "poo": "Programacion orientada a objetos",
    "mvc": "Modelo vista controlador",
    "programar": "El arte de convertir el café en comida"

}
print(diccionario["poo"])

numero = {
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve"
}

texto = input("Introduce un numero: ")
textoFinal = ""
for letra in texto:
    textoFinal += numero[letra] + " "
print(textoFinal)