## ANÁLISIS

En esta quinta gramática se generan las cadenas de la forma:

$L(G4)={a(ab)^nb | n>=0}$

Es decir, cadenas que comienzan con a y terminan con b pero que contengan la mayor combinación posible de ab.

## Ejemplos de cadenas aceptadas:
    ab
    aabb
    aababb
    aabababb

## Ejemplos de cadenas no aceptadas:
    a
    b
    aabbb
    aaaabb

## Código en Python
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

## Código en C:
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

## Ejemplo de prueba:

Archivo de entrada (prueba.txt):

    ab
    aabb
    aababb
    aabababb
    aaabbbaab

## Salida esperada:
    acepta
    acepta
    acepta
    acepta
    no acepta

## Observaciones
La gramática G5 define cadenas que:

Deben empezar con 'a'.

Deben terminar con 'b'.

En el medio solo pueden aparecer repeticiones del patrón "ab".

En el código en Python:

Primero valida que la cadena empiece con 'a' y termine en 'b'.

Si la cadena es "ab", se acepta inmediatamente como caso base.

Luego recorre desde el segundo carácter hasta el penúltimo en pasos de 2, asegurando que cada par sea "ab".

Si en algún momento no encuentra el patrón correcto o hay un desbalance de caracteres, devuelve no acepta.

En el código en C:

Sigue la misma lógica: primero verifica inicio y final.

Acepta el caso base "ab".

Luego con un bucle for, va comparando de dos en dos para validar el patrón "ab".

Si encuentra una pareja inválida o falta de pareja (longitud impar en la sección del medio), devuelve no acepta.

Ejemplos verificados:

"ab" → acepta (caso base).

"aabb" → acepta (n=1).

"aababb" → acepta (n=2).

"b", "aa", "abb", "aba" → no acepta.

Con este método no se depende de expresiones regulares, lo que lo hace más explícito y fácil de seguir paso a paso. Esto también es útil en C, ya que la validación se hace de manera manual controlando cada carácter de la cadena.
