menu = "1) Introdueix una frase" + "\n" + "2) Elimina les vocals" + "\n" + \
    "3) Elimina les consonants" + "\n" + "4) Ordena la frase al reves i printala por pantalla" + \
    "\n" + "Ordena les paraules de la frase en orde ascendent i printales per pantalla"

while True:
    opc = input("Opcio: ")
    if not opc.isdigit() and not int(opc) in range(1,6):
        print("Opcio incorrecta\n")
    else:
        resultado = ""
        frase = ""
        opc = int(opc)
        if opc == 3 and frase == "":
            print("Primer has d'introduir la frase per poder utilitzar aquesta funció.")

        elif opc == 3 and frase != "":
            vocales = "aeiou"
            for letra in frase:
                if letra.lower() in vocales:
                    resultado += letra
            print(resultado)
            print()

        elif opc == 5:
            for letra in frase:
                print(letra + "\n")

