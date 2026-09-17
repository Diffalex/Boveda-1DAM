---
tags:
  - programacion
  - java
  - ud1
  - comentarios
  - consola
asignatura: Programación
unidad: UD1
tema: Comentarios y salida por consola
---

# Comentarios y salida por consola

## Tipos de comentarios

### Comentario de una línea
Se usa `//` y afecta solo hasta el final de la línea:

```java
// Esto es un comentario de una línea
String nombre = "Ana"; // También válido al final de una línea
```

### Comentario multilínea
Se encierra entre `/*` y `*/`, abarcando varias líneas sin necesidad de repetir `//`:

```java
/*
 * Comentario multilínea.
 * Puede ocupar varias líneas.
 * Es útil para explicar bloques de código.
 */
```

> [!tip] No uses comentarios para explicar código obvio
> Comenta el **por qué**, no el **qué** si ya es evidente.

## Salida por consola

### `System.out.println()`
Imprime el texto seguido de un salto de línea:

```java
System.out.println("Hola Mundo");
// Salida: Hola Mundo\n
```

### `System.out.print()`
Imprime el texto **sin** añadir salto de línea:

```java
System.out.print("Hola ");
System.out.print("Mundo");
// Salida: Hola Mundo
```

## Ejemplo: HolaMundo

```java
public class HolaMundo {
    public static void main() {
        // Imprime un saludo por pantalla
        System.out.println("Hola Mundo");
    }
}
```

> [!important] El nombre de la clase debe coincidir con el nombre del fichero
> Si el fichero se llama `HolaMundo.java`, la clase principal se llama `HolaMundo`.

## Ver también

- [[UD1 - Estructura de un programa Java|Estructura de un programa]] — estructura completa
- [[UD1 - Entrada de datos con Scanner|Entrada de datos]] — cómo leer datos
- [[UD1 - Nomenclatura de identificadores|Reglas de identificadores]] — convenciones de nombrado

---

← Volver a [[_Índice Programación]]
