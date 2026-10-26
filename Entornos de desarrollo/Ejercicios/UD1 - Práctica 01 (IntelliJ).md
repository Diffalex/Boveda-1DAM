---
tags:
  - entornos-de-desarrollo
  - ud1
  - practica
  - intellij
  - java
  - bytecode
asignatura: Entornos de desarrollo
unidad: UD1
tema: Práctica 01 — IntelliJ
---

# UD1 — Práctica 01. IntelliJ: código fuente, objeto y ejecutable

Enunciado de la práctica a partir de `Anexos/UD1_Practica01_IntelliJ_Codigo_fuente_objeto_ejecutable v1.1.pdf`. El objetivo es recorrer el ciclo completo de un programa Java con IntelliJ IDEA: **fuente** (`.java`) → **objeto** (`.class`) → **ejecutable** (`.jar`).

> [!info] Datos de la práctica
> - **Criterios:** RA1.c y RA1.d.
> - **Materiales:** IntelliJ IDEA y JDK 17 o superior.
> - **Entregable:** un único PDF con las **9 capturas** y sus explicaciones.

## Conceptos

| Concepto | En Java | Qué es |
|---|---|---|
| **Código fuente** | `TallerJava.java` | Código escrito por el programador |
| **Código objeto** | `TallerJava.class` | Bytecode generado por `javac`; lo entiende la JVM |
| **Código ejecutable** | `ED01_P01_Apellidos_Nombre.jar` | Empaquetado final que se ejecuta con `java -jar` |

> [!note] No es lo mismo que en C
> El `.class` no es código máquina nativo: es **bytecode** portable. La JVM lo interpreta o lo compila con JIT. El `.jar` es un paquete que contiene clases y metadatos.

## Parte 1. Crear el código fuente

1. Abre IntelliJ IDEA y crea un **New Project**.
2. Rellena:
   - **Name:** `ED01_P01_Apellidos_Nombre`.
   - **Location:** una carpeta localizable.
   - **Build system:** `IntelliJ` (no Maven ni Gradle).
   - **JDK:** 17 o superior; si no aparece, `Add JDK > Download JDK`.
   - Desmarca **Add sample code**.
3. Pulsa **Create**.
4. En el panel Project, clic derecho sobre `src` → **New > Package** → `PracticaUd01`.
5. Clic derecho sobre el paquete → **New > Java Class** → `TallerJava`.

> [!tip] Capturas
> La captura 1 debe mostrar la ventana **New Project** rellena justo antes de pulsar **Create**. La captura 2 debe mostrar el panel Project con el paquete y el código completo.

### Enunciado

Un alumno quiere saber su calificación final del módulo de Entornos de Desarrollo:

- **55 %** del promedio de sus tres calificaciones parciales.
- **30 %** de la calificación del examen final.
- **15 %** de la calificación de un trabajo final.

El programa debe pedir los tres parciales (enteros), el examen (entero) y el trabajo (entero), y mostrar la nota final con decimales.

### Código

```java
package PracticaUd01;

import java.util.Scanner;

public class TallerJava {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Nota parcial 1: ");
        int parcial1 = sc.nextInt();
        System.out.print("Nota parcial 2: ");
        int parcial2 = sc.nextInt();
        System.out.print("Nota parcial 3: ");
        int parcial3 = sc.nextInt();
        System.out.print("Nota examen final: ");
        int examen = sc.nextInt();
        System.out.print("Nota trabajo final: ");
        int trabajo = sc.nextInt();

        double promedioParciales = (parcial1 + parcial2 + parcial3) / 3.0;
        double notaFinal = promedioParciales * 0.55
                         + examen * 0.30
                         + trabajo * 0.15;

        System.out.printf("Nota final: %.2f%n", notaFinal);
        sc.close();
    }
}
```

> [!warning] Medias
> Divide entre `3.0`, no entre `3`. Si divides entre `3` haces una división entera y pierdes los decimales del promedio. También puedes usar `double` para las notas.

## Parte 2. Crear el código objeto

1. Menú **Build > Rebuild Project** (o `Ctrl + F9` para compilar solo lo cambiado).
2. Revisa la ventana **Build**: debe aparecer `Build completed successfully`.
3. Comprueba que se ha generado:

```text
out/production/ED01_P01_Apellidos_Nombre/PracticaUd01/TallerJava.class
```

> [!note] Qué hace IntelliJ
> IntelliJ invoca a `javac` para convertir `TallerJava.java` en `TallerJava.class`. Si hay errores, los muestra en la ventana Build y **no genera** el `.class`.

## Parte 3. Ejecutar el código ejecutable

1. Pulsa **Run** (triángulo verde) o usa **Run > Run 'TallerJava'**.
2. Introduce los datos en la ventana **Run**, pulsando Intro después de cada uno.
3. Comprueba que la nota final coincide con el cálculo.

IntelliJ **no genera el `.jar` automáticamente**; hay que crear un artefacto.

## Parte 4. Generar el JAR

1. **File > Project Structure…** (`Ctrl + Alt + Mayús + S`).
2. En la lista izquierda, elige **Artifacts**.
3. Pulsa **+** → **JAR > From modules with dependencies…**.
4. En **Main Class**, elige `PracticaUd01.TallerJava`.
5. Deja el resto por defecto y pulsa **OK**, luego **Apply** y **OK**.
6. Menú **Build > Build Artifacts…**, elige el artefacto y pulsa **Build**.
7. Verifica que existe:

```text
out/artifacts/ED01_P01_Apellidos_Nombre_jar/ED01_P01_Apellidos_Nombre.jar
```

## Parte 5. Ejecutar el JAR desde el terminal

En el panel Project, clic derecho sobre la carpeta `ED01_P01_Apellidos_Nombre_jar` → **Open in > Terminal**. Se abre un terminal ya situado en esa carpeta. Ejecuta:

```bash
java -jar "ED01_P01_Apellidos_Nombre.jar"
```

Si `java` no se reconoce, el JDK descargado por IntelliJ no está en el `PATH`: avisa al profesor o instala un JDK del sistema.

> [!tip] Capturas 3-9
> - **3:** archivo `TallerJava.java` en `src`.
> - **4:** Build completado correctamente.
> - **5:** `TallerJava.class` en `out/production/...`.
> - **6:** ventana Run con datos y nota final.
> - **7:** Project Structure con el artefacto y la Main Class.
> - **8:** `.jar` visible en `out/artifacts/...`.
> - **9:** terminal con `java -jar`, datos y resultado.

## Entrega

- [ ] PDF con portada, índice y las **9 capturas** en orden.
- [ ] Cada captura numerada y con una frase que explique qué se ve.
- [ ] Nombre del archivo: `ED01_P01_Apellidos_Nombre.pdf`.
- [ ] Proyecto nombrado `ED01_P01_Apellidos_Nombre`.
- [ ] Paquete `PracticaUd01` y clase `TallerJava`.
- [ ] El programa calcula correctamente la nota final.
- [ ] Se muestran `.class` y `.jar` generados.

| Criterio | Valoración |
|---|---|
| PDF único, bien nombrado y con nombre en la portada | Obligatorio |
| Capturas 1-9 completas, ordenadas y legibles | Obligatorio |
| Se demuestra la generación de `.class` y `.jar` | Obligatorio |
| El programa calcula bien la nota final | Obligatorio |
| Ejercicio al 100 % y correcto | Hasta 10 |

## Ver también

- [[UD1 - Desarrollo de software|UD1 — Desarrollo de software]] — teoría de fuente, objeto, ejecutable y bytecode
- [[Entornos de desarrollo/Ejercicios/UD1 - Práctica 01 (compilación vs interpretación)|Práctica 01 — Compilación vs interpretación]]
- [[Entornos de desarrollo/Ejercicios/UD1 - ED01 Actividades|ED01 — Actividades resueltas]]
- [[_Índice Entornos de desarrollo]]

---

← Volver a [[_Índice Entornos de desarrollo]]
