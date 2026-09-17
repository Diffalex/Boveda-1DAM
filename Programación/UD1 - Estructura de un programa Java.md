---
tags:
  - programacion
  - java
  - ud1
  - plantilla
asignatura: Programación
unidad: UD1
tema: Estructura de un programa
---

# Estructura de un programa Java

Toda aplicación Java sigue una estructura base. La siguiente plantilla es la organización estándar que se debe seguir:

```java
import java.util.Scanner;

public class NombreClase {
    public static void main(String[] args) {

        // ─── Declaración de variables ───
        // Constantes
        // Variables de entrada
        // Variables de salida
        // Variables auxiliares
        Scanner teclado = new Scanner(System.in);

        // ─── Entrada de datos ───
        System.out.println("PLANTILLA DE PROGRAMA ");
        System.out.println("----------------------");

        // ─── Procesamiento ───
        // Aquí va la lógica del programa

        // ─── Salida de resultados ───
        System.out.println("RESULTADO");
        System.out.println("---------");

        System.out.println();
        System.out.println("Fin del programa.");
    }
}
```

## Secciones de la plantilla

| Sección | Descripción |
|---|---|
| **Imports** | Librerías necesarias (`java.util.Scanner`) |
| **Declaración de variables** | Constantes, entrada, salida y auxiliares — agrupadas para claridad |
| **Entrada de datos** | Petición de datos al usuario (lectura de `teclado`) |
| **Procesamiento** | Lógica y operaciones del programa |
| **Salida de resultados** | Mostrar la información al usuario |

## Convenciones aplicadas

- Los nombres de las variables siguen las reglas de la nota [[UD1 - Nomenclatura de identificadores|Nomenclatura de identificadores]]
- El nombre de la **clase** coincide con el nombre del fichero (obligatorio)
- Las secciones se separan con bloques de guiones para legibilidad

## Flujo de ejecución

```
main() se ejecuta
   ↓
Declaración de variables
   ↓
Entrada de datos (lectura de Scanner)
   ↓
Procesamiento
   ↓
Salida por consola (System.out)
   ↓
Fin del programa
```

## Ver también

- [[UD1 - Comentarios y salida por consola|Comentarios]] — cómo documentar el código
- [[UD1 - Entrada de datos con Scanner|Entrada con Scanner]] — cómo leer datos del teclado
- [[UD1 - Nomenclatura de identificadores|Reglas de identificadores]] — reglas de nombrado

---

← Volver a [[_Índice Programación]]
