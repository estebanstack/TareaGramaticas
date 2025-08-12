def acepta_cadena(cadena):
    n = 0
    length = len(cadena)

    # Contar 'a'
    while n < length and cadena[n] == 'a':
        n += 1

    # Verificar que el resto sean solo 'b'
    for i in range(n, length):
        if cadena[i] != 'b':
            return False

    # Condición: n > 0 y cantidad de b's = n + 1
    return n > 0 and (length - n) == (n + 1)

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

