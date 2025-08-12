def acepta_cadena(cadena):
    # Debe empezar con 'a' y terminar con 'b'
    if len(cadena) < 2 or cadena[0] != 'a' or cadena[-1] != 'b':
        return False

    # Caso base: "ab"
    if cadena == "ab":
        return True

    # Verificar el patrón a(ab)^n b
    # Desde el segundo carácter hasta el penúltimo deben repetirse "ab"
    i = 1
    while i < len(cadena) - 1:
        if i + 1 >= len(cadena) - 1:
            return False  # No hay pareja completa
        if cadena[i] != 'a' or cadena[i + 1] != 'b':
            return False
        i += 2
    return True
   
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

