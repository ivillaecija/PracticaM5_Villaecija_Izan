menu = "1) Introdueix una frase" + "\n" + "2) Elimina les vocals" + "\n" + \
    "3) Elimina les consonants" + "\n" + "4) Ordena la frase al reves i printala por pantalla" + \
    "\n" + "Ordena les paraules de la frase en orde ascendent i printales per pantalla"

while True:
    opc = input("Opcio: ")
    if not opc.isdigit() and not int(opc) in range(1,6):
        print("Opcio incorrecta\n")
    else:
        opc = int(opc)
