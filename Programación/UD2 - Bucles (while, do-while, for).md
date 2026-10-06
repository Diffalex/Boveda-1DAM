---
tags:
  - programacion
  - java
  - ud2
  - estructuras-control
  - bucles
asignatura: Programación
unidad: UD2
tema: Bucles
---

# Bucles — `while`, `do-while` y `for`

Un **bucle** (estructura repetitiva o iterativa) repite un bloque de sentencias mientras se cumpla una condición. Evita repetir código y es la base para recorrer rangos o validar entradas.

## `while` — comprueba antes de entrar

Evalúa la condición; solo si es `true` ejecuta el bloque (puede que **no se ejecute nunca**):

```java
while (condición) {
    // sentencias repetidas
}
```

Ejemplo: secuencia de números desde `inicio` hasta `fin`:

```java
while (num1 <= num2) {
    System.out.print(num1 + " ");
    num1++;
}
```

> [!tip] Contador
> La variable que controla el bucle debe **modificarse dentro** del bloque (p. ej. `num1++`), o el bucle sería infinito.

## `do-while` — entra y comprueba después

Ejecuta el bloque **al menos una vez** y luego comprueba la condición:

```java
do {
    // sentencias (se ejecutan sí o sí una vez)
} while (condición);
```

> [!note] "Modo cabezón"
> La entrada validada (pedir un número hasta que cumpla una condición) se resuelve de forma natural con `do-while`: se pide, se comprueba y se vuelve a pedir mientras sea inválido. Es el patrón del ejercicio `EjercicioBucles1` (pedir un número **par** hasta que lo sea).

## `for` — bucle con contador

Pensado para repetir *un número conocido de veces*. Tiene tres partes: inicialización, condición y actualización:

```java
for (inicialización; condición; actualización) {
    // sentencias repetidas
}
```

Tabla de multiplicar del 7:

```java
for (contador = 1; contador <= 10; contador++) {
    resultado = contador * 7;
    System.out.println(7 + " x " + contador + " = " + resultado);
}
```

> [!note] Variables del `for`
> La variable se puede declarar dentro de la inicialización (`for (int i = 1; …)`) o fuera (`int i; for (i = 1; …)`). En el código de clase se usa habitualmente declarada fuera junto al resto de variables.

## Bucles anidados

Un bucle dentro de otro. El **interno** se completa entero por cada "vuelta" del externo. Ejemplo: dibujar varias líneas de asteriscos.

> [!warning] Cuidado con las variables
> En `Asteriscos.java`, la variable `contador` se declara dos veces (fuera del `for` y como variable del `for`), y el `for` interno usa la externa mientras que el externo también la usa. Ambos `for` deben usar variables distintas para funcionar de forma predecible.

## `break` — salir del bucle

Interrumpe el bucle inmediatamente y continúa tras él.

## Cuándo usar cada uno

| Bucle | Cuándo |
|---|---|
| `while` | Nº de repeticiones **desconocido** y se decide al entrar |
| `do-while` | Nº de repeticiones desconocido pero **al menos una** (entrada validada) |
| `for` | Nº de repeticiones **conocido** (contador) |

## Ver también

- [[Programación/Ejercicios/UD2 - Ejemplos bucles y switch|Ejemplos bucles y switch]] — programas de clase (`EjercicioWhile`, `EjercicioResueltoFor`, `Multiplicaciones`, `Asteriscos`, `EjercicioBucles1`)
- [[UD2 - Selección múltiple (switch)|Selección múltiple `switch`]] — la otra estructura de control nueva de la unidad
- [[UD2 - Estructura condicional (if-else)|Condicionales]] — estructura de control lineal
- [[UD1 - Entrada de datos con Scanner|Entrada con Scanner]] — los bucles de validación leen datos por teclado

---

← Volver a [[_Índice Programación]]