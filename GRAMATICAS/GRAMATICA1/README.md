## ANÁLISIS

En esta primera gramática se definen los números capicúas formados por 0 y 1.
La regla básica es que la cadena debe ser igual al leerla de izquierda a derecha y de derecha a izquierda.

La gramática es:

    S → 0S0 | 1S1 | 0 | 1


Esto significa que se aceptan cadenas como:

    0
    1
    101
    1001
    00100

Y no se aceptan cadenas como:

    0
    1100
    010

## Código en Python
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

## Código en C
    #include <stdio.h>
    #include <string.h>
  
    int capicua(const char *cadena) {
        int len = strlen(cadena);
        for (int i = 0; i < len; i++) {
          if (cadena[i] != '0' && cadena[i] != '1') {
              return 0; // contiene caracteres inválidos
          }
          if (cadena[i] != cadena[len - i - 1]) {
              return 0; // no es palíndromo
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

# Ejemplo de prueba

Archivo de entrada (prueba.txt):

    0
    101
    1001
    00100
    010


Salida esperada en ambos programas:

    acepta
    acepta
    acepta
    acepta
    no acepta


# Observaciones

En este ejercicio pude implementar la gramática en Python y en C. En ambos casos la lógica fue la misma:

Validar que la cadena solo tenga 0 y 1.

Revisar que sea capicua.

La diferencia es que en Python se aprovechó la simplicidad del slicing ([::-1]), mientras que en C se recorrió la cadena manualmente y se compararon caracteres en posiciones opuestas.

El resultado fue el esperado, confirmando que la gramática genera los números capicúas en binario.
