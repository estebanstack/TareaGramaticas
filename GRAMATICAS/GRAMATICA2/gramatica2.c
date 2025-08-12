#include <stdio.h>
#include <string.h>

int acepta_cadena(const char *cadena) {
    int n = 0;
    int len = strlen(cadena);

    while (n < len && cadena[n] == 'a') {
        n++;
    }
    for (int i = n; i < len; i++) {
        if (cadena[i] != 'b') return 0;
    }
    return (len - n) == (n + 1);
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

