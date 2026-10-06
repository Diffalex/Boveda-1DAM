---
tags:
  - programacion
  - java
  - ud1
  - jdk
  - jre
  - jvm
asignatura: Programación
unidad: UD1
tema: JDK, JRE y JVM
---

# UD1 — JDK, JRE y JVM

Son tres piezas relacionadas pero distintas del ecosistema Java. La relación es de contención: **JDK ⊃ JRE ⊃ JVM**.

## JDK (Java Development Kit)

Herramientas de **desarrollo**. Es lo que necesitas **instalar para programar** en Java:

- `javac` — compilador de Java (de `.java` a `.class`/bytecode).
- `javadoc` — genera documentación a partir de los comentarios del código.
- `jar` — crea y gestiona ficheros `.jar` (paquetes de la aplicación).
- `debugger` — depurador.

## JRE (Java Runtime Environment)

Herramientas para **ejecutar** programas (no para desarrollarlos):

- **JVM** (Java Virtual Machine) — la que **realmente interpreta el bytecode**.
- **Bibliotecas estándar** — `java.lang`, `java.util`, etc.
- **Ficheros de soporte**.

## JVM (Java Virtual Machine)

Intérprete del bytecode (`.class`) producido por `javac`. Es la que hace que el mismo programa corra en cualquier sistema (Windows, Linux, macOS…) sin recompilar — el principio **"Escribe una vez, ejecuta en cualquier parte"**.

> [!note] Diferencia clave
> - Para **ejecutar** un programa basta con la **JRE**.
> - Para **programar** necesitas el **JDK** (incluye el `javac`, el debugger, etc., además de todo lo de la JRE).
> La **JVM** es el corazón de la JRE.

## Ver también

- [[UD1 - Estructura de un programa Java|Estructura de un programa]] — de `.java` a `.class` con `javac`
- [[UD1 - Tipos de datos primitivos|Tipos primitivos]] — tipos con los que trabaja el programa
- [[Programación/Ejercicios/UD1 - Ejemplos java|Ejemplos de programas]] — código de clase

---

← Volver a [[_Índice Programación]]