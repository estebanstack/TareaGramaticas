def acepta_cadena(cadena):
    # Contar cantidad de 'a' al inicio
    n = 0
    while n < len(cadena) and cadena[n] == 'a':
        n += 1
    
    # Lo que queda después de las 'a'
    resto = cadena[n:]
    
    # Debe haber exactamente n+1 'b' y nada más
    return resto == 'b' * (n + 1)

def main():
    archivo = input("Ingrese el nombre del archivo: ")
    try:
        with open(archivo, "r") as f:
            for linea in f:
                cadena = linea.strip()
                if acepta_cadena (cadena):
                    print("acepta")
                else:
                    print("no acepta")
    except FileNotFoundError:
        print("No se pudo abrir el archivo.")

if __name__ == "__main__":
    main()
