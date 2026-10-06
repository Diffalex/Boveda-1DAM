---
tags:
  - programacion
  - java
  - ud2
  - estructuras-control
  - switch
asignatura: Programación
unidad: UD2
tema: Selección múltiple
---

# Selección múltiple — `switch`

El `switch` permite elegir entre **varios valores concretos** de una variable (menú, códigos, categorías), evitando cadenas largas de `else if`.

## Sintaxis general

```java
switch (expresión) {
    case valor1:
        // sentencias
        break;
    case valor2:
        // sentencias
        break;
    ...
    default:
        // si no coincide ningún case
        break;
}
```

> [!note] `break` y `default`
> Cada `case` suele terminar en `break` para **salir** del `switch` (si no, continúa al siguiente caso: *fallthrough*). `default` se ejecuta cuando ningún `case` coincide.

## `switch` anidado

Un `switch` dentro de otro. En `EstacionMes.java`, el primer `switch` selecciona la estación según un número (1-4) y, dentro, un segundo `switch` asigna el mes según otro número (1-3):

```java
switch (estacion) {
    case 1: // Invierno
        nombreEstacion = "Invierno";
        switch (mesEstacion) {
            case 1: nombreMes = "Diciembre"; break;
            case 2: nombreMes = "Enero";     break;
            case 3: nombreMes = "Febrero";   break;
        }
        break;
    case 2: // Primavera
        // ...
        break;
    // ...
}
```

## Validación de rangos antes del `switch`

Antes de entrar en el `switch` conviene comprobar que la entrada es válida; así evitamos que un valor fuera de rango "caiga" a un `default` o deje la variable vacía:

```java
if (estacion < 1 || estacion > 4 || mesEstacion < 1 || mesEstacion > 3) {
    System.out.println("Valor inválido.");
} else {
    // switch (estacion) { ... }
}
```

## `switch` frente a `else if`

| | `switch` | `else if` |
|---|---|---|
| Compara | valores discretos (`==`) | condiciones arbitrarias |
| Legibilidad | alta con muchos casos | baja con muchas condiciones encadenadas |
| Uso típico | menús, códigos, unidades (1, 2, 3…) | notas, rangos, combinaciones lógicas |

## Ver también

- [[Programación/Ejercicios/UD2 - Ejemplos bucles y switch|Ejemplos bucles y switch]] — `EstacionMes.java` (switch anidado)
- [[UD2 - Bucles (while, do-while, for)|Bucles]] — el `switch` suele combinarse con bucles y validación
- [[UD2 - Estructura condicional (if-else)|Condicionales]] — alternativa con `else if`
- [[UD1 - Entrada de datos con Scanner|Entrada con Scanner]] — los valores del `switch` se leen por teclado

---

← Volver a [[_Índice Programación]]