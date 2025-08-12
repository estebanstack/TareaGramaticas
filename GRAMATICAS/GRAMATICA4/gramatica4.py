def acepta_cadena(cadena):
    # La gramática G4 solo acepta exactamente "abb" o "ab"
    return cadena == "abb" or cadena == "ab"

def main():
    archivo = input("Ingrese el nombre del archivo: ")

    try:
        with open(archivo, "r") as f:
            for linea in f:
                cadena = linea.strip()
                if acepta_cadena(cadena):
                    print("acepta")
                else:
                    print("no acepta")
    except FileNotFoundError:
        print("No se pudo abrir el archivo")

if __name__ == "__main__":
    main()

