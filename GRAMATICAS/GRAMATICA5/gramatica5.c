#include <stdio.h>
#include <string.h>

int acepta_cadena(const char *cadena) {
    int len = strlen(cadena);

    // Debe empezar con 'a' y terminar con 'b'
    if (len < 2 || cadena[0] != 'a' || cadena[len - 1] != 'b') {
        return 0;
    }

    // Caso base: "ab"
    if (len == 2 && cadena[0] == 'a' && cadena[1] == 'b') {
        return 1;
    }

    // Verificar el patrón a(ab)^n b
    // Desde el segundo carácter hasta el penúltimo deben repetirse "ab"
    for (int i = 1; i < len - 1; i += 2) {
        if (i + 1 >= len - 1) return 0; // No hay pareja completa
        if (cadena[i] != 'a' || cadena[i + 1] != 'b') {
            return 0;
        }
    }
    return 1;
}

int main() {
    char archivo[100], linea[100];
    FILE *fp;

    printf("Ingrese el nombre del archivo: ");
    scanf("%s", archivo);

    fp = fopen(archivo, "r");
    if (!fp) {
        perror("No se pudo abrir el archivo");
        return 1;
    }

    while (fgets(linea, sizeof(linea), fp)) {
        // Eliminar salto de línea
        linea[strcspn(linea, "\n")] = '\0';

        if (acepta_cadena(linea)) {
            printf("acepta\n");
        } else {
            printf("no acepta\n");
        }
    }

    fclose(fp);
    return 0;
}
