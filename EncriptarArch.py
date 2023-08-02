def encriptar(texto):
    print("El texto encrptado es: " +
          texto)
    textoFinal = ''
    for letra in texto:
        ascii = ord(letra)
        ascii += 1
        textoFinal += chr(ascii)
    return textoFinal


def desencriptar(texto):
    print("El texto a desencriptar-: " +
          texto)
    textoFinal = ''
    for letra in texto:
         ascii = ord(letra)
         ascii -= 1
         textoFinal += chr(ascii)
    return textoFinal



def encriptarArch(ruta):
    archivo = open(ruta, 'r')
    texto = archivo.read()
    archivo.close()
    textoE = encriptar(texto)

    archivo = open(ruta , "w")
    archivo.write(textoE)
    archivo.close()


def desencriptarArch(ruta):
    archivo = open(ruta, 'r')
    texto = archivo.read()
    archivo.close()
    textoE = desencriptar(texto)

    archivo = open(ruta , "w")
    archivo.write(textoE)
    archivo.close()


result = input("E o O : " )
ruta = input("Ruta: ")

if result == "E":
    encriptarArch(ruta)
else:
    desencriptarArch(ruta)
    