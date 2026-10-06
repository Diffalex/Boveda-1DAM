---
tags:
  - programacion
  - java
  - ud1
  - tipos-datos
asignatura: Programación
unidad: UD1
tema: Tipos de datos primitivos
---

# Tipos de datos primitivos en Java

Java tiene **8 tipos primitivos** que guardan valores simples (no objetos). Los demás tipos (arrays, `String`, etc.) son tipos de referencia.

## Tabla de tipos primitivos

| Tipo | Información representada | Rango | Descripción | Valor por defecto |
|---|---|---|---|---|
| `byte` | Números enteros | -128 .. +127 | 8 bits de longitud | `0` |
| `short` | Números enteros | -32768 .. +32767 | 16 bits de longitud | `0` |
| `int` | Números enteros | -2147483648 .. +2147483647 | 32 bits de longitud. Es el tipo entero que se usa por defecto¹ | `0` |
| `long` | Números enteros | -9223372036854775808 .. +9223372036854775807 | 64 bits de longitud. Para enteros muy grandes | `0l` / `0L` |
| `char` | Un carácter (letra, dígito, símbolo…) | Cualquier carácter Unicode | Guarda un solo carácter, entre comillas simples: `'A'` | `'\u0000'` |
| `float` | Números decimales | Precisión → unas 7 cifras exactas | Coma flotante de 32 bits. Se escribe con `f`/`F` al final. Ejemplo: `float f = 3.14f;` | `0.0f` / `0.0F` |
| `double` | Números decimales | Precisión → unas 15-16 cifras exactas | Coma flotante de 64 bits. Es el tipo decimal que se usa por defecto¹. Ejemplo: `double d = 3.14;` | `0.0d` / `0.0D` |
| `boolean` | Verdadero o falso | `true` / `false` | Se usa para condiciones y comprobaciones | `false` |

> ¹ Cuando escribes un número sin indicar explícitamente su tipo, Java decide por ti:
> - Si es entero (sin coma), como `100`, Java lo trata automáticamente como `int`.
> - Si tiene decimales, como `3.14`, Java lo trata automáticamente como `double`.
>
> Por eso `int` es el tipo entero "por defecto" y `double` el decimal "por defecto": son los que Java asume si no le dices lo contrario.

## Literales y sufijos

Si quieres usar otro tipo, tienes que avisar a Java con un sufijo:

```java
float pi = 3.14;   // ERROR: 3.14 ya "ha nacido" como double
float pi = 3.14f;  // OK: la f le dice a Java "quiero float, no double"
```

La `f` final (o `F`) indica que el número es `float`. Java no permite guardar un `double` en un `float` sin más.

## ⚠️ Sobre `float` y `double`

Los ordenadores guardan los números decimales en **binario**. Igual que 1/3 no puede escribirse de forma exacta en decimal (0,3333…, interminable), algunos números decimales normales tampoco pueden escribirse de forma exacta en binario. Esto provoca, a veces, **errores de redondeo diminutos e invisibles**.

> [!warning] Nunca compares `float`/`double` con `==`
> No compares dos números `float` o `double` con `==` para ver si son iguales. En vez de preguntar si son exactamente iguales, pregunta si están **muy, muy cerca**.

## Ver también

- [[UD1 - Nomenclatura de identificadores|Reglas de identificadores]] — cómo nombrar las variables que guardan estos tipos
- [[UD1 - Estructura de un programa Java|Estructura de un programa]] — dónde se declaran las variables en la plantilla
- [[UD1 - Entrada de datos con Scanner|Entrada de datos]] — `nextInt()`, `nextDouble()` leen estos tipos
- [[UD1 - Comentarios y salida por consola|Comentarios y salida]] — cómo mostrar e imprimir estos valores

---

← Volver a [[_Índice Programación]]