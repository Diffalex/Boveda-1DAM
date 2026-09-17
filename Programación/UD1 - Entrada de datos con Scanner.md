---
tags:
  - programacion
  - java
  - ud1
  - scanner
  - entrada-datos
asignatura: Programación
unidad: UD1
tema: Entrada de datos con Scanner
---

# Entrada de datos con Scanner

Para leer datos introducidos por el usuario se usa la clase `Scanner` del paquete `java.util`.

## Crear el objeto Scanner

```java
import java.util.Scanner;

Scanner teclado = new Scanner(System.in);
```

- `System.in` representa la entrada estándar (teclado)

## Métodos principales

| Método | Lee | Ejemplo |
|---|---|---|
| `nextInt()` | Un número entero | `int edad = teclado.nextInt();` |
| `nextDouble()` | Un número con decimales | `double precio = teclado.nextDouble();` |
| `next()` | Una palabra (hasta espacio) | `String nombre = teclado.next();` |
| `nextLine()` | Una línea completa | `String frase = teclado.nextLine();` |

## Ejemplo completo

```java
import java.util.Scanner;

public class EjemploScanner {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.println("Introduce tu nombre:");
        String nombre = teclado.nextLine();

        System.out.println("Introduce tu edad:");
        int edad = teclado.nextInt();

        System.out.println("Hola " + nombre + ", tienes " + edad + " años.");
    }
}
```

## Errores comunes

- **Mezclar `nextInt()` con `nextLine()`**: después de leer un número, el salto de línea queda en el buffer. Se puede solucionar con un `teclado.nextLine()` adicional para descartarlo:

```java
int edad = teclado.nextInt();
teclado.nextLine(); // descarta el \n pendiente
String ciudad = teclado.nextLine();
```

## Ver también

- [[UD1 - Comentarios y salida por consola|Salida por consola]] — `System.out.println()` y `print()`
- [[UD1 - Estructura de un programa Java|Plantilla]] — dónde se ubica la entrada en la estructura
- [[UD1 - Nomenclatura de identificadores|Reglas de identificadores]] — cómo nombrar las variables leídas

---

← Volver a [[_Índice Programación]]
