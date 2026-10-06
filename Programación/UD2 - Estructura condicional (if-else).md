---
tags:
  - programacion
  - java
  - ud2
  - estructuras-control
  - condicionales
asignatura: Programación
unidad: UD2
tema: Estructura condicional
---

# Estructura condicional — `if/else`

Hasta ahora los programas ejecutan las sentencias **en orden** (estructura secuencial). La estructura **condicional** permite que el programa **tome decisiones**: unas sentencias se ejecutan, otras no, según una condición.

## `if`

Las sentencias dentro de las llaves solo se ejecutan si la condición es `true`:

```java
if (edad >= 18) {
    System.out.println("Eres mayor de edad");
}
```

## `if / else`

Si la condición es `false` se ejecuta el bloque del `else`:

```java
if (edad >= 18) {
    System.out.println("Eres mayor de edad");
} else {
    System.out.println("Menor de edad");
}
```

## `else if`

Para encadenar varias comprobaciones. Se evalúan en orden; en cuanto una es `true`, se ejecuta su bloque y se salta al final:

```java
if (nota < 5) {
    System.out.println("INSUFICIENTE");
} else if (nota < 6) {
    System.out.println("SUFICIENTE");
} else if (nota < 7) {
    System.out.println("BIEN");
} else if (nota < 9) {
    System.out.println("NOTABLE");
} else {
    System.out.println("SOBRESALIENTE");
}
```

> [!tip] Sin llaves
> Si hay una única sentencia, las llaves son opcionales. En clase se escriben muchas veces sin ellas:
>
> ```java
> if (num1 > num2)
>     System.out.println("num1 es mayor");
> else
>     System.out.println("num2 es mayor");
> ```

## Operadores de comparación y lógicos

| Operador | Significado | | Operador | Significado |
|---|---|---|---|---|
| `==` | igual a | | `&&` | Y (and) |
| `!=` | distinto de | | `\|\|` | O (or) |
| `<` `>` | menor / mayor | | `!` | No (not) |
| `<=` `>=` | menor o igual / mayor o igual | | | |

Los operadores `&&` y `||` son de **cortocircuito**: `&&` no evalúa el segundo operando si el primero es `false`; `||` no lo evalúa si el primero es `true`.

## Módulo `%` y números pares/impares

El operador `%` da el **resto** de la división entera:

```java
int resto = num1 % 2;
if (resto == 0)
    System.out.println("Es par");
else
    System.out.println("Es impar");
```

## Bloques de sentencias y ámbito

Las llaves `{ }` agrupan sentencias en un **bloque**. Las variables declaradas dentro de un bloque solo existen dentro de él (su *ámbito* o *scope*):

```java
public class BloqueSentencias {
    public static void main(String[] args) {
        int num1 = 10;   // existe en todo el método
        double num2 = 1.3;

        System.out.println(num1);
    }
}
```

## Ver también

- [[Programación/Ejercicios/UD2 - Ejemplos if-else|Ejemplos if/else]] — programas de clase con la estructura condicional
- [[UD1 - Tipos de datos primitivos|Tipos primitivos]] — tipos usados en las condiciones (`int`, `double`)
- [[UD1 - Entrada de datos con Scanner|Entrada con Scanner]] — los programas condicionales leen datos por teclado

---

← Volver a [[_Índice Programación]]