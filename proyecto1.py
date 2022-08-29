

def encriptar(texto):
    textoFinal = ""
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    return textoFinal

def desencriptar(texto):

    textoFinal = ""
    for letra in texto:
        ascii = ord(letra)
        ascii -= 1
        textoFinal += chr(ascii)
    return textoFinal


def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, "w")
    archivo.write(textoEncriptado)
    archivo.close()
    print("El archivo se encripto correctamente")


def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, "r")
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, "w")
    archivo.write(textoDesencriptado)
    archivo.close()
    print("El archivo se desencripto correctamente")


respuestaEoD = input("Presione la letra e para encriptar un archivo o d para desencriptar: ")
rutaArchivo = input("Ingrese la ruta del archivo que desea encriptar: ")

if respuestaEoD == "e":
    encriptarArchivo(rutaArchivo)

else:
    desencriptarArchivo(rutaArchivo)
