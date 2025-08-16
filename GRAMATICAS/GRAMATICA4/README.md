## ANÁLISIS

En esta cuarta gramática se generan las cadenas de la forma:

$L(G4)={abb | ab}$

Es decir, cadenas compuestas unicamente por abb o ab.

## Ejemplos de cadenas aceptadas:
    abb
    ab

## Ejemplos de cadenas no aceptadas:
    abbb
    aaabbbb
    a
    b
    
## Código en Python:
    def acepta_cadena(cadena):
    # La gramática G4 solo acepta exactamente "abb" o "ab"
    return cadena == "abb" or cadena == "ab"

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

## Código en C: 
    #include <stdio.h>
    #include <string.h>
  
    int acepta_cadena(const char *cadena) {
      // La gramática G4 solo acepta exactamente "abb" o "ab"
      return (strcmp(cadena, "abb") == 0 || strcmp(cadena, "ab") == 0);
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

## Observaciones

La gramática G4 genera un lenguaje muy reducido, con solo dos cadenas posibles: "abb" y "ab".

No acepta ninguna otra combinación de a y b, ya que las producciones restringen la derivación.

En Python, la implementación se reduce a verificar si la cadena está en una lista de aceptadas.

En C, se realiza la comparación usando strcmp, evaluando directamente si la cadena coincide con "abb" o "ab".

Se probó que:

"abb" y "ab" → acepta.

"a", "b", "aabb", "aaabbb" → no acepta.

Esta gramática es un buen ejemplo de cómo algunas definiciones BNF pueden restringir al máximo el conjunto de cadenas válidas, contrastando con otras más generales como G2 o G3.
