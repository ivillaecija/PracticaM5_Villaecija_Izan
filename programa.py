menu = "1) Introdueix una frase" + "\n" + "2) Elimina les vocals" + "\n" + \
    "3) Elimina les consonants" + "\n" + "4) Ordena la frase al reves i printala por pantalla" + \
    "\n" + "Ordena les paraules de la frase en orde ascendent i printales per pantalla"

frase = ""
while True:
    opc = input("Opcio: ")
    if not opc.isdigit() and not int(opc) in range(1,6):
        print("Opcio incorrecta\n")
    else:
        opc = int(opc)
        resultado = ""
        opc = int(opc)
        if opc == 1:
            while frase == "":
                frase = input("Introdueix una frase:\n")
                if frase == "":
                    print("La frase no pot ser buida")

        elif opc == 2 and frase != "":
            vocales = "aeiou"
            for letra in range(len(frase)):
                if not frase[letra].lower() in vocales:
                    resultado += str(frase[letra])
            print(resultado)

        elif opc == 2 and frase == "":
            print("Primer has d'introduir la frase per utilitzar aquesta opció.\n")

        if opc == 3 and frase == "":
            print("Primer has d'introduir la frase per poder utilitzar aquesta funció.")

        elif opc == 3 and frase != "":
            vocales = "aeiou"
            for letra in frase:
                if letra.lower() in vocales:
                    resultado += letra
            print(resultado)
            print()

        elif opc == 4 and frase != "":
            print(frase[-1:0:-1])

        elif opc == 4 and frase == "":
            print("Primer has d'introduir la frase per utilitzar aquesta opció.\n")



        elif opc == 5:
            for letra in frase:
                print(letra + "\n")