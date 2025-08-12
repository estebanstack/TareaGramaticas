def capicua(cadena):
    # Verifica que solo contenga 0 y 1
    if not all(ch in '01' for ch in cadena):
        return False
    # Verifica si es capicua
    return cadena == cadena[::-1]

def main():
    archivo = input("Ingrese el nombre del archivo: ")
    try:
        with open(archivo, "r") as f:
            for linea in f:
                palabra = linea.strip()
                if capicua (palabra):
                    print("acepta")
                else:
                    print("no acepta")
    except FileNotFoundError:
        print("No se pudo abrir el archivo.")

if __name__ == "__main__":
    main()

