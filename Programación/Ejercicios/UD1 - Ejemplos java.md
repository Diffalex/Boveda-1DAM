---
tags:
  - programacion
  - java
  - ud1
  - ejercicios
  - trabajo
asignatura: Programación
unidad: UD1
tema: Ejemplos de programas en Java
subtema: Código de clase (prog-ud1)
---

# UD1 — Ejemplos de programas en Java

Programas de práctica (proyecto IntelliJ `prog-ud1`). Muestran la [[UD1 - Estructura de un programa Java|plantilla estándar]], la lectura con [[UD1 - Entrada de datos con Scanner|Scanner]] y comportamientos relacionados con [[UD1 - Tipos de datos primitivos|tipos primitivos]].

## Ejemplo 1: HolaMundo

Ejemplo mínimo con comentarios multilínea ([[UD1 - Comentarios y salida por consola|comentarios]]).

```java
/* Ejemplo de comentario multilinea, "//" otro tipo de comentario para linea unica
   el multilinea no salta al darle al enter
 */
// Ejemplo

// Siempre nombre de clase debe coincidir con nombre fichero

public class HolaMundo {
    public static void main() {
        // Linea de abajo se refiere a imprimir en pantalla de comandos,
        // mayuscula System si no error de sintaxis
        System.out.println("Hola Mundo");
    }
}
```

## Ejemplo 2: EstructuraPrograma

La plantilla completa de programa con secciones (declaración, entrada, procesamiento, salida). Ver [[UD1 - Estructura de un programa Java|Estructura de un programa]].

```java
import java.util.Scanner;

public class EstructuraPrograma {
    public static void main(String[] args) {

        // Declaración de variables
        // Constantes, variables de entrada, salida y auxiliares
        Scanner teclado = new Scanner(System.in);

        // Entrada de datos
        System.out.println("PLANTILLA DE PROGRAMA ");
        System.out.println("----------------------");

        // Procesamiento
        // Aquí vendrá nuestro código de procesamiento

        // Salida de resultados
        System.out.println("RESULTADO");
        System.out.println("---------");
        System.out.println("Fin del programa.");
    }
}
```

## Ejemplo 3: Calculoiva

Cálculo del IVA: lee el precio con [[UD1 - Entrada de datos con Scanner|`nextDouble()`]] y usa `double`.

```java
import java.util.Scanner;

public class Calculoiva {
    public static void main() {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Introduce precio del producto");
        double precioProducto = teclado.nextDouble();
        double iva = 0.21 * precioProducto;
        double precioconIVA = precioProducto + iva;
        System.out.println("Precio producto: " + precioProducto);
        System.out.println("Importe del iva: " + iva);
        System.out.println("Precio con IVA: " + precioconIVA);
    }
}
```

## Ejemplo 4: Operadores

Demuestra los **errores de redondeo** de `double` y por qué no hay que comparar con `==` (ver [[UD1 - Tipos de datos primitivos|tipos primitivos]]).

```java
public class Operadores {
    public static void main() {
        double num1 = 0.1 + 0.2;
        double num2 = 0.3;
        float num3 = 3.2F;
        double num4 = 3.8;
        int num5 = 3;
        double num6 = 2 / 3.0;
        double num7 = 2 % 3;

        System.out.println("num1 = " + num1);
        System.out.println("num2 = " + num2);
        // un = es asignación, == es comparación
        System.out.println("¿num1 == num2? " + (num1 == num2));
        System.out.println("num6 = " + num6);
        System.out.println("num7 = " + num7);
    }
}
```

> [!important] Resultado del ejemplo Operadores
> `0.1 + 0.2 == 0.3` da **`false`** por la representación binaria inexacta de los decimales. Nunca compares `float`/`double` con `==`.

## Ejemplo 5: DatosPrimitivos

Complementa al ejemplo anterior: demuestra que ni `0.1`, ni `0.2`, ni `0.3` tienen representación binaria exacta.

```java
public class DatosPrimitivos {
    public static void main() {
        double a = 0.1 + 0.2;
        double b = 0.3;

        // Los decimales se guardan en binario, y no todos los numeros decimales
        // tienen una representacion exacta en binario (aunque parezcan "sencillos").
        // Por eso "a" no es exactamente 0.3, aunque lo parezca a simple vista.
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("¿a == b? " + (a == b));

        /* ¿Por qué falla justo este ejemplo?
        Porque ni 0.1, ni 0.2, ni 0.3 se pueden guardar exactos en binario:
        los tres llevan ya un pequeño error de fabrica, y al sumar dos
        errores pequeños, el resultado deja de coincidir con el tercero. */
    }
}
```

> [!note] Explicación de `DatosPrimitivos`
> La suma `0.1 + 0.2` da `0.30000000000000004`, por eso `a == b` es `false`.

## Ejemplo 6: OperadoresLogicos

Tablas de verdad de los operadores lógicos: negación `!`, AND `&`/`&&`, OR `|`/`||` y XOR `^`.

```java
public class OperadoresLogicos {
    public static void main() {
        System.out.println("EJEMPLOS DE USO DE OPERADORES LÓGICOS");
        System.out.println("-------------------------------------");

        System.out.println("Negacion:\n !false es : " + (!false));
        System.out.println(" !true es : " + (!true));

        System.out.println("Operador AND (&):");
        System.out.println(" false & false es : " + (false & false));
        System.out.println(" false & true  es : " + (false & true));
        System.out.println(" true  & false es : " + (true & false));
        System.out.println(" true  & true  es : " + (true & true));

        System.out.println("Operador OR (|):");
        System.out.println(" false | false es : " + (false | false));
        System.out.println(" false | true  es : " + (false | true));
        System.out.println(" true  | false es : " + (true | false));
        System.out.println(" true  | true  es : " + (true | true));

        System.out.println("Operador OR Exclusivo o XOR (^):");
        System.out.println(" false ^ false es : " + (false ^ false));
        System.out.println(" false ^ true  es : " + (false ^ true));
        System.out.println(" true  ^ false es : " + (true ^ false));
        System.out.println(" true  ^ true  es : " + (true ^ true));

        System.out.println("Operador AND (&&):");
        System.out.println(" false && false es : " + (false && false));
        System.out.println(" false && true  es : " + (false && true));
        System.out.println(" true  && false es : " + (true && false));
        System.out.println(" true  && true  es : " + (true && true));

        System.out.println("Operador OR (||):");
        System.out.println(" false || false es : " + (false || false));
        System.out.println(" false || true  es : " + (false || true));
        System.out.println(" true  || false es : " + (true || false));
        System.out.println(" true  || true  es : " + (true || true));
    }
}
```

> [!tip] Resumen de operadores booleanos
> - `!` invierte el valor (`!true = false`).
> - `&` / `&&` (AND): solo `true & true` da `true`. La diferencia es que `&` evalúa ambos operandos siempre y `&&` evalúa el segundo solo si es necesario (*cortocircuito*).
> - `|` / `||` (OR): da `true` desde que un operando es `true` (`||` también en cortocircuito).
> - `^` (XOR): `true` solo si los operandos **difieren** (`true ^ false = true`, `true ^ true = false`).

## Ejemplo 7: Conversiones

Conversiones entre tipos primitivos: **implícitas** (automáticas, sin pérdida) y **explícitas (casting)** forzadas con paréntesis.

```java
public class Conversiones {
    public static void main(String[] args) {
        // Declaración de variables
        int ent1;      // int 32bits
        long ent2;     // long 64bits
        float real1;   // float 32bits - 7 cifras aproximación
        double real2;  // double 64bits - 15-16 cifras aproximación

        // Inicialización
        ent1 = 0;
        ent2 = 0;
        real1 = 0.0F;   // los literales reales son double; la F indica float
        real2 = 0.0F;   // conversión automática o implícita

        ent1 = (int) ent2;   // casting: fuerza la conversión
        ent2 = ent1;         // conversión implícita (int -> long, sin pérdida)
        ent2 = (long) ent1;  // conversión explícita (innecesaria)
        ent2 = 5L;
        ent2 = 55;           // conversión implícita
        real2 = 2.0F;        // conversión implícita
        ent1 = (int) (2 / 3.0);   // precedencia: el cast se aplica tras la división
        real1 = (float) (2 / 3.0); // cast double -> float
        real1 = 3_000_000_000L;    // separador _ en los literales
    }
}
```

> [!important] Sobre las conversiones
> - **Implícitas** (automáticas): de tipo "más pequeño" a "más grande" (p. ej. `int` → `long` → `double`).
> - **Explícitas (casting)**: se fuerzan con el tipo entre paréntesis, p. ej. `(int)`, `(float)`. Pueden perder precisión (`double` → `float`, `long` → `int`).
> - El separador `_` en literales (`3_000_000_000L`) se puede usar para mejorar la legibilidad.

## Ejemplo 8: Ejercicio1 — leer un nombre

Utiliza [[UD1 - Entrada de datos con Scanner|`nextLine()`]] para leer una línea completa.

```java
import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        // Declaración de variables
        String nombre;
        Scanner teclado = new Scanner(System.in);

        // Entrada de datos
        System.out.println("Introduce tu nombre: ");
        nombre = teclado.nextLine();
        System.out.println("Hola, " + nombre + " ¿que tal el curso?");
    }
}
```

## Ejemplo 9: Ejercicio2 — calcular la edad

Lee un número entero con [[UD1 - Entrada de datos con Scanner|`nextInt()`]] y hace un cálculo.

```java
import java.util.Scanner;

public class Ejercicio2 {
    static public void main(String[] args) {
        // Declaración de variables
        int anio;
        int anioActual = 2026;
        Scanner teclado = new Scanner(System.in);

        // Entrada de datos
        System.out.println("Introduce tu año de nacimiento");
        anio = teclado.nextInt();
        System.out.println("Tu edad actual es: " + (anioActual - anio));
    }
}
```

> [!tip] Práctica pendiente
> Los demás enunciados de práctica están en [[Programación/Ejercicios/UD1 - Enunciados de práctica|Enunciados de práctica (pendientes)]].

## Ver también

- [[UD1 - Tipos de datos primitivos|Tipos de datos primitivos]] — por qué `3.14f` lleva sufijo
- [[UD1 - Entrada de datos con Scanner|Entrada con Scanner]] — lectura de datos
- [[UD1 - Estructura de un programa Java|Plantilla de programa]] — estructura de los ejemplos

---

← Volver a [[_Índice Programación]]