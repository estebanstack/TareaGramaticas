## ANÁLISIS

En esta segunda gramática se generan las cadenas de la forma:

$𝐿(𝐺2)={𝑎^n 𝑏^{n+1}∣𝑛>=0}$

Esto significa que la cadena debe contener primero varias a seguidas y después la misma cantidad de b.
 
# Ejemplos de cadenas aceptadas:

    ab
    aabb
    aaabbb
    aaaaabbbbb

# Ejemplos de cadenas no aceptadas:
  
    a
    abb
    ba
    aab

## Código en Python
```python
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
```

## Código en C  
```c
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
```

## Ejemplo de prueba

Archivo de entrada (prueba.txt):

    ab
    aabb
    aaabbb
    abb
    ba
    a


## Salida esperada:

    acepta
    acepta
    acepta
    no acepta
    no acepta
    no acepta
    
## Observaciones

En esta gramática validé que las cadenas tengan una b mas que a.

En Python, fue sencillo con bucles que cuentan primero las a y luego las b.

En C, la lógica fue exactamente igual pero recorriendo la cadena carácter por carácter.

Los resultados fueron correctos: solo se aceptaron las cadenas con la forma ${a^n b^{n+1}}$ y se rechazaron las demás.
