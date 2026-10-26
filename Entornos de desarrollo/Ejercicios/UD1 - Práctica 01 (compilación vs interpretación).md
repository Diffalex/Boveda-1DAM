---
tags:
  - entornos-de-desarrollo
  - ud1
  - practica
  - compilacion
  - interpretacion
  - c
  - python
  - java
asignatura: Entornos de desarrollo
unidad: UD1
tema: Práctica 01 — Compilación vs interpretación
---

# UD1 — Práctica 01. Compilación frente a interpretación

Enunciado de la práctica a partir de `Anexos/ED01_Practica01_Compilacion_vs_Interpretacion.pdf`. El objetivo es comprobar las diferencias entre **compilar**, **interpretar** y **ejecutar en una máquina virtual** usando el mismo programa en C, Python y Java.

> [!info] Datos de la práctica
> - **Criterios:** CE1.c, CE1.d y CE1.f del RA1.
> - **Duración orientativa:** 2 sesiones (unos 100 minutos).
> - **Materiales:** Visual Studio Code, `gcc`, Python 3 y JDK (`javac` y `java`).
> - **Entregable:** informe con capturas, tablas completadas y conclusiones.

## Objetivo

Observar tres cosas en cada lenguaje:

1. Qué **ficheros** se generan.
2. **Cuándo** aparecen los errores.
3. **Cuánto tarda** cada programa.

## Preparación del entorno

Crea una carpeta `practica01` con tres subcarpetas: `c`, `python` y `java`. Abre la carpeta en VS Code y comprueba las herramientas en el terminal integrado:

```bash
gcc --version
python --version
javac -version
```

En Linux/macOS puede ser `python3 --version`. Si algún comando no se reconoce, avisa al profesor antes de continuar.

## Parte 1. Programa compilado: C

Crea `c/suma.c`:

```c
#include <stdio.h>

int main() {
    long long suma = 0;
    printf("Inicio del programa\n");
    for (long long i = 1; i <= 200000000; i++) {
        suma += i;
    }
    printf("La suma es: %lld\n", suma);
    return 0;
}
```

Desde `c`, compila paso a paso:

| Paso | Comando | Qué observar |
|---|---|---|
| 1 | `gcc -c suma.c` | Se genera `suma.o` (código objeto); no es legible como el fuente |
| 2 | `gcc suma.o -o suma` | El enlazador genera el ejecutable `suma` |
| 3 | `./suma` (`.\suma.exe` en Windows) | Se ejecuta sin necesidad del compilador |

> [!note] Qué debe pasar
> En la carpeta quedan `suma.c` (fuente), `suma.o` (objeto) y `suma` (ejecutable). Solo el `.c` es legible por humanos; el `.o` es binario.

## Parte 2. Programa interpretado: Python

Crea `python/suma.py`:

```python
suma = 0
print("Inicio del programa")
for i in range(1, 200000001):
    suma += i
print("La suma es:", suma)
```

Ejecútalo:

```bash
python suma.py
# En Linux/macOS:
python3 suma.py
```

> [!note] Qué debe pasar
> No se genera un ejecutable. El intérprete lee y ejecuta el `.py` directamente. Para ejecutarlo hace falta tener Python instalado.

## Parte 3. Lenguaje virtual: Java

Crea `java/Suma.java`:

```java
public class Suma {
    public static void main(String[] args) {
        long suma = 0;
        System.out.println("Inicio del programa");
        for (long i = 1; i <= 200000000L; i++) {
            suma += i;
        }
        System.out.println("La suma es: " + suma);
    }
}
```

Desde `java`:

| Paso | Comando | Qué observar |
|---|---|---|
| 1 | `javac Suma.java` | Se genera `Suma.class` (bytecode) |
| 2 | `java Suma` | La JVM ejecuta el bytecode; se escribe `Suma`, sin `.class` |
| 3 | `javap -c Suma` (opcional) | Muestra las instrucciones del bytecode |

> [!note] Qué debe pasar
> `Suma.class` no es un ejecutable nativo: necesita una **JVM**. Es código intermedio portable y se puede ejecutar en cualquier equipo con Java instalado.

## Parte 4. ¿Cuándo aparecen los errores?

Crea estos tres archivos con una variable `total` que no existe:

```c
// c/error.c
#include <stdio.h>

int main() {
    printf("Linea 1: todo bien\n");
    printf("Linea 2: todo bien\n");
    printf("Resultado: %d\n", total);
    return 0;
}
```

```python
# python/error.py
print("Linea 1: todo bien")
print("Linea 2: todo bien")
print("Resultado:", total)
```

```java
// java/Error.java
public class Error {
    public static void main(String[] args) {
        System.out.println("Linea 1: todo bien");
        System.out.println("Linea 2: todo bien");
        System.out.println("Resultado: " + total);
    }
}
```

Compila y ejecuta cada uno:

```bash
gcc error.c -o error
python error.py
javac Error.java
java Error
```

| Pregunta | C | Python | Java |
|---|---|---|---|
| ¿Se muestra «Linea 1: todo bien»? | No | Sí | No |
| ¿Se genera ejecutable o `.class`? | No | No aplica | No |
| ¿Cuándo aparece el error? | Antes de ejecutar (compilación) | Durante la ejecución | Antes de ejecutar (compilación) |
| ¿Qué dice el mensaje? | `total` no declarado | `NameError: name 'total' is not defined` | `cannot find symbol: variable total` |

> [!important] Diferencia clave
> En C y Java el error de compilación impide generar el programa, así que no se ejecuta nada. En Python el error aparece en tiempo de ejecución: las dos primeras líneas sí se muestran.

## Parte 5. ¿Cuánto tarda cada programa?

Mide tres veces cada versión y calcula la media. Cierra programas pesados durante la medición.

| Programa | Linux/macOS | Windows (PowerShell) |
|---|---|---|
| C | `time ./suma` | `Measure-Command { .\suma.exe }` |
| Python | `time python3 suma.py` | `Measure-Command { python suma.py }` |
| Java | `time java Suma` | `Measure-Command { java Suma }` |

| Programa | Intento 1 | Intento 2 | Intento 3 | Media |
|---|---|---|---|---|
| C (compilado) |  |  |  |  |
| Python (interpretado) |  |  |  |  |
| Java (JVM) |  |  |  |  |

> [!tip] Interpretación
> Los tiempos dependen del equipo. Lo habitual es que **C** sea el más rápido, **Java** quede en medio (la JVM compila con JIT las partes calientes) y **Python** sea el más lento por su ejecución interpretada.

## Parte 6. Conclusiones

Completa la tabla con lo observado:

| Aspecto | C | Python | Java |
|---|---|---|---|
| ¿Cuándo se traduce el código? | Antes de ejecutar | Durante la ejecución | Antes de ejecutar (a bytecode) |
| ¿Qué ficheros se generan? | `.o` y ejecutable | Ninguno propio | `.class` |
| ¿Qué necesita el equipo para ejecutarlo? | El ejecutable (y su runtime de C) | Intérprete de Python | JVM |
| ¿Cómo aparecen los errores? | Al compilar | Durante la ejecución | Al compilar |
| Tiempo medio observado |  |  |  |

Preguntas para razonar:

- ¿Qué diferencia hay entre el código objeto de C y el bytecode de Java?
- ¿Por qué en C el programa con error no llegó a mostrar «Linea 1» y en Python sí?
- ¿A qué se debe la diferencia de tiempos entre C, Python y Java?
- Si tuvieras que entregar un programa a un cliente sin que instale nada, ¿qué opción elegirías?
- Si quisieras que el mismo programa funcionara en Windows, Linux y macOS sin recompilar, ¿qué opción elegirías?

> [!note] Orientaciones
> - El objeto de C es código máquina para una plataforma; el bytecode de Java es intermedio y portable.
> - C detecta el error al compilar; Python lo detecta al ejecutar.
> - C es nativo; Python interpretado; Java usa JVM y JIT.
> - Para no instalar nada, un ejecutable nativo compilado; para portabilidad sin recompilar, Java (JVM) o Python (intérprete).

## Ampliación opcional

- Compila C con optimización: `gcc -O2 suma.c -o suma_o2` y vuelve a medir.
- Cambia el límite del bucle (20 000 000 y 2 000 000 000) y compara.

## Entregable

Un único informe con:

- [ ] Capturas de VS Code mostrando los ficheros generados en cada carpeta.
- [ ] Capturas de los mensajes de error de la Parte 4.
- [ ] Las tres tablas completadas.
- [ ] Las respuestas de las conclusiones.

| Criterio | Puntos |
|---|---|
| Los tres programas se compilan/ejecutan y se aportan capturas | 2 |
| Tabla de errores completa y coherente | 2 |
| Tiempos medidos tres veces y media calculada | 2 |
| Tabla comparativa completa y basada en la observación | 2 |
| Conclusiones razonadas con compilador, intérprete, bytecode y JVM | 2 |
| **Total** | **10** |

## Ver también

- [[UD1 - Desarrollo de software|UD1 — Desarrollo de software]] — teoría de compilación, interpretación y bytecode
- [[Entornos de desarrollo/Ejercicios/UD1 - Práctica 01 (IntelliJ)|Práctica 01 — IntelliJ]]
- [[Entornos de desarrollo/Ejercicios/UD1 - ED01 Actividades|ED01 — Actividades resueltas]]
- [[_Índice Entornos de desarrollo]]

---

← Volver a [[_Índice Entornos de desarrollo]]
