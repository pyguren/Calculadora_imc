# Un array es una variables que nos permite guardar muchos datos en un solo lugar

arreglo = ["pera", "melon", "banana", "sandia"]
arreglo.reverse()
arreglo.remove("melon")
arreglo.append("kiwi")


for fruta in arreglo:
    if fruta.endswith("a"):
        print("las frutas son: " + fruta)

    if fruta == "sandia":
        break
        print("las frutas son: " + fruta)

texto = "hola mundo"
for letra in texto:
    print("Letra: " + letra)

for numero in range(10):
    if numero > 4:
        print(numero)