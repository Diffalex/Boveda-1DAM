---
tags:
  - programacion
  - java
  - ud1
  - identificadores
asignatura: Programación
unidad: UD1
tema: Nomenclatura de identificadores
---

# Nomenclatura de identificadores Java

Las reglas de nombrado se dividen en **obligatorias** (dan error de compilación si se incumplen) y **convenios** (el código compila, pero es menos legible).

## Reglas obligatorias

| Regla | Ejemplo correcto | Ejemplo incorrecto |
|---|---|---|
| Distingue mayúsculas de minúsculas | `Alumno` ≠ `alumno` | — |
| No puede empezar por dígito | `datos2` | `2datos` ❌ |
| Solo puede contener letras, dígitos, `_` y `$` | `nombre_alumno` | `nombre-alumno` ❌ |
| No puede ser palabra clave del lenguaje | `miClase` | `class` ❌ |
| No puede ser `true`, `false` ni `null` | `esValido` | `true` ❌ |

## Convenios de estilo

| Elemento | Convención | Ejemplo |
|---|---|---|
| Variables y métodos | `camelCase` | `ficheroClientes`, `calcularTotal()` |
| Clases | `PascalCase` | `FicheroClientes`, `ManejadorCliente` |
| Constantes | `MAYÚSCULAS_CON_GUION_BAJO` | `MAX_ALUMNOS` |
| Nombres descriptivos | Sin abreviaturas crípticas | `ficheroClientes` vs `fc` |

> [!warning] No empezar por `$` ni `_`
> Aunque legal, el compilador reserva internamente `$` y `_` por convención.

## Ver también

- [[UD1 - Estructura de un programa Java|Estructura de un programa]] — cómo se aplican estos nombres en la plantilla
- [[UD1 - Comentarios y salida por consola|Comentarios]] — buenas prácticas de documentación

---

← Volver a [[_Índice Programación]]
