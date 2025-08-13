#include <stdio.h>
#include <string.h>

int capicua(const char *cadena) {
    int len = strlen(cadena);
    for (int i = 0; i < len; i++) {
        if (cadena[i] != '0' && cadena[i] != '1') {
            return 0; // contiene caracteres invalidos
        }
        if (cadena[i] != cadena[len - i - 1]) {
            return 0; // no es capicua
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

        if (capicua(linea)) {
            printf("acepta\n");
        } else {
            printf("no acepta\n");
        }
    }

    fclose(fp);
    return 0;
}

