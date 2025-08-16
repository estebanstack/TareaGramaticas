## ANALISIS

En esta tercera gramática se generan las cadenas de la forma:

  $𝐿(𝐺3)={𝑎^n 𝑏^{n+1}∣𝑛>0}$

Es decir, cadenas que comienzan con n letras a seguidas de n+1 letras b, con la condición de que n > 0.

## Ejemplos de cadenas aceptadas:

    abb
    aabbb
    aaabbb

## Ejemplos de cadenas no aceptadas:
    b
    aaabbb
    aabbbb
    aaab

## Código en Python
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



## Código en C
    #include <stdio.h>
    #include <string.h>
    
    int acepta_cadena(const char *cadena) {
      int n = 0;
      int len = strlen(cadena);

      // Contar 'a'
      while (n < len && cadena[n] == 'a') {
          n++;
      }
      // El resto deben ser 'b'
      for (int i = n; i < len; i++) {
          if (cadena[i] != 'b') return 0;
      }
      // Condición: n > 0 y cantidad de b's == n + 1
      return (n > 0) && ((len - n) == (n + 1));
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
          }   else {
              printf("no acepta\n");
          }
      }

      fclose(fp);
      return 0;
    }
    
## Ejemplo de prueba

Archivo de entrada (prueba.txt):

    b
    abb
    aabbb
    aaabbb
    aaabbbb

## Salida esperada:

    no acepta
    acepta
    acepta
    no acepta
    acepta

## Observaciones

La gramática G3 restringe las cadenas a que siempre exista al menos una a y que el número de b sea exactamente uno más que el número de a.

La condición n > 0 garantiza que no se aceptan cadenas sin a.

En la implementación en Python, se aprovecha la facilidad de manejo de cadenas y bucles para contar a y b.

En la versión en C, se requiere más detalle en la manipulación de índices y eliminación del salto de línea (\n), pero el funcionamiento es equivalente.

Ambas versiones retornan "acepta" cuando la cadena cumple la forma a^n b^(n+1) y "no acepta" en cualquier otro caso.

Se comprobó que cadenas como abb, aabbb, aaabbbb son aceptadas correctamente, mientras que ab, bbb, aabbbb no lo son.
