---
tags:
  - programacion
  - java
  - ud3
  - poo
  - objetos
  - clases
  - metodos
asignatura: Programación
unidad: UD3
tema: Utilización de objetos (POO)
---

# UD3 — Utilización de objetos (POO)

Fuente: `Utilización_de_objetos_OCR.pdf` (en `Anexos/`). La unidad pasa de la programación estructurada a la **Programación Orientada a Objetos (POO)**: qué son clases y objetos, cómo se crean y manipulan, y cómo se usan las clases de la API de Java (métodos, `String`, paquetes, consola, fechas y excepciones).

> [!info] Contenido
> 1. De la programación estructurada a la POO
> 2. Fundamentos y características de la POO
> 3. Clases y objetos
> 4. Ciclo de vida: declarar, instanciar, manipular y destruir
> 5. Métodos: parámetros, retorno, `static`, inmutabilidad, `equals`
> 6. Paquetes y bibliotecas de Java
> 7. Entrada y salida por consola
> 8. Fechas y horas (`java.time`)
> 9. Excepciones (`try`/`catch`)

## 1. De la programación estructurada a la POO

| Paradigma | En qué se centra |
|---|---|
| **Programación estructurada** | En las **acciones** (verbos): funciones y procedimientos que descomponen el problema en pasos |
| **Programación Orientada a Objetos** | En los **objetos** (sustantivos): entidades que reúnen datos y las operaciones sobre esos datos |

En la programación estructurada los datos y las funciones están **separados** y suelen ser globales: cualquier cambio en los datos puede obligar a tocar muchas funciones. En POO, datos y funciones forman una sola entidad (el objeto) y el estado queda **protegido** dentro de él.

La POO busca una correspondencia directa entre el **espacio del problema** (mundo real) y el **espacio de la solución** (programa). Así el código es más legible y fácil de desarrollar, modificar y mantener.

> [!note] Beneficios
> - **Comprensión** — el código refleja los conceptos del problema real.
> - **Modularidad** — cada clase vive en su archivo y se puede cambiar sin afectar al resto.
> - **Mantenimiento** — los cambios quedan localizados; el mantenimiento es la mayor parte del coste del software.
> - **Seguridad** — no se modifican los datos directamente, solo mediante las operaciones previstas.
> - **Reusabilidad** — una clase (p. ej. `Persona`) se reaprovecha en otras aplicaciones.

## 2. Características de la POO

- **Abstracción** — definir lo importante de un objeto sin entrar en el detalle de implementación. La herramienta principal es la **clase**.
- **Modularidad** — dividir la aplicación en clases independientes (una por archivo).
- **Encapsulación** (ocultamiento de la información) — el objeto oculta sus datos y solo expone una interfaz de uso; se evita manipulaciones inadecuadas.
- **Jerarquía** — relaciones entre clases:
  - **Generalización/especialización (herencia, "es un")**: `CocheDeCarreras` **es un** `Coche`.
  - **Agregación ("es parte de")**: `Coche` **tiene** motor, ruedas, frenos, ventanas.
- **Polimorfismo** — varias clases pueden realizar la misma acción de forma distinta (un perro, un gato y una persona se "expresan" de forma diferente).

> [!tip] Lenguajes históricos
> **Simula** (1962) introdujo el concepto de clase; **Smalltalk** (1972) popularizó la POO y el MVC; **C++** (1985) consolidó la clase con atributos y métodos; **Eiffel** (1986), **Java** (1995, bytecode + JVM) y **C#** (2000) completan la evolución.

## 3. Clases y objetos

Un **objeto** es una entidad con tres características:

- **Identidad** — lo distingue de cualquier otro objeto, aunque tenga los mismos valores (p. ej. el número de bastidor de un coche).
- **Estado** — lo definen sus **atributos** (propiedades, campos o variables miembro) y sus valores.
- **Comportamiento** — lo definen sus **métodos** (funciones miembro): las acciones que puede realizar.

Los objetos se comunican enviándose **mensajes**: llamar a un método de otro objeto. El conjunto de mensajes a los que un objeto responde es su **protocolo**.

Una **clase** es el **molde o plantilla** a partir de la cual se crean objetos. Define:

- los **atributos comunes** a todos los objetos de la clase,
- los **métodos** que pueden usarse para manejarlos.

Cada objeto creado a partir de una clase es una **instancia** de esa clase. "Objeto" e "instancia" son sinónimos en la práctica.

```java
public class Vehiculo {
    // atributos (estado)
    String marca;
    String modelo;
    int cilindrada;

    // métodos (comportamiento)
    public void arrancar() { /* ... */ }
    public void acelerar() { /* ... */ }
    public void frenar() { /* ... */ }
}
```

> [!important] En esta unidad no implementamos clases
> El objetivo es **utilizar** clases ya hechas (API de Java y ejemplos proporcionados): instanciar objetos con `new` y llamar a sus métodos. La implementación de nuestras propias clases se verá más adelante.

## 4. Utilización de objetos

### 4.1 Ciclo de vida

1. **Creación** — se reserva memoria y se inicializan los atributos.
2. **Manipulación** — se usan los atributos y métodos del objeto.
3. **Destrucción** — se elimina el objeto y se liberan sus recursos.

### 4.2 Declaración

Se declara una **variable de tipo referencia**: el tipo es la clase y el nombre empieza por minúscula.

```java
Rectangle rectangulo;      // una referencia
Rectangle r1, r2, r3;      // varias referencias
```

Una referencia recién declarada **no contiene ningún objeto**. En Java el compilador no deja usarla hasta que se le asigne explícitamente un valor (no se puede asumir que valga `null`).

> [!note] Referencia nula
> `null` indica que la variable no apunta a ningún objeto. No es lo mismo que una cadena vacía `""`, que sí es un objeto `String` de longitud cero.

### 4.3 Instanciación y constructor

Se crea el objeto con el operador **`new`** y una llamada al **constructor**:

```java
Rectangle rectangulo = new Rectangle(0, 0, 10, 5);
```

Pasos que ocurren:

1. `new` reserva memoria para los atributos del objeto.
2. Se ejecuta el **constructor**, que inicializa esos atributos.
3. `new` devuelve la **referencia** al objeto y se asigna a la variable.

**Características de un constructor:**

- Tiene el **mismo nombre que la clase** y no devuelve ningún valor de forma explícita.
- Se invoca **automáticamente** con `new`; no se puede volver a llamar sobre un objeto ya creado (una nueva llamada crea otro objeto).
- Puede haber **varios constructores** (sobrecarga): mismo nombre, distinta lista de parámetros.
- Puede recibir parámetros para fijar los valores iniciales.
- Si la clase no define ninguno, el compilador genera un **constructor por defecto** vacío que inicializa los atributos a `0`, `false` o `null` según el tipo.

La clase `Rectangle` (paquete `java.awt`) tiene, entre otros:

```java
Rectangle r1 = new Rectangle(0, 0, 10, 5); // x, y, base, altura
Rectangle r2 = new Rectangle(8, 4);        // base y altura; posición (0,0)
```

### 4.4 Referencias, asignación y objetos huérfanos

Una variable de tipo referencia guarda una **dirección de memoria** (la "llave" del objeto), no el objeto en sí. Al asignar una referencia a otra **no se copia el objeto**:

```java
Rectangle r1 = new Rectangle(0, 0, 10, 5);
Rectangle r2 = r1;          // r1 y r2 apuntan al MISMO objeto

r2.setSize(20, 20);
System.out.println(r1.getWidth()); // 20.0
```

Si una variable deja de apuntar a su objeto y no queda ninguna otra referencia, el objeto queda **huérfano** y el recolector de basura lo eliminará.

### 4.5 Manipulación: el operador punto

Para acceder a un atributo o llamar a un método se usa `objeto.miembro`:

```java
rectangulo.width = 100;          // atributo público
rectangulo.setSize(200, 200);    // método
double base = rectangulo.getWidth();
```

Solo se puede acceder a los miembros **accesibles** (públicos). El resto forma parte de la implementación interna y es invisible desde fuera: la clase se comporta como una **caja negra** y su interfaz pública es lo que podemos usar.

> [!tip] Atributos públicos vs métodos
> Lo habitual es que los atributos sean privados y se manipulen mediante métodos (`setSize`, etc.). Así los cambios quedan controlados y validados.

### 4.6 Destrucción y recolector de basura

Java destruye automáticamente los objetos que ya no están referenciados mediante el **garbage collector**. Se ejecuta en segundo plano, marca los objetos inalcanzables y libera su memoria cuando resulta oportuno. El programador no tiene que liberar memoria manualmente.

### 4.7 La clase `String`

`String` es una **clase** (tipo referenciado), no un tipo primitivo, aunque Java permite usarla de forma especial:

```java
String mensaje;                              // declaración
mensaje = new String("El primer programa");  // instanciación con constructor
String texto = "El primer programa";         // forma habitual (sin new)
```

Ambas formas son equivalentes: Java traduce el literal a una llamada al constructor. `String` es **inmutable**: sus métodos (`concat`, `replace`, `trim`, etc.) no cambian el objeto original, sino que devuelven uno nuevo.

## 5. Métodos

Un método tiene **cabecera** (interfaz pública) y **cuerpo** (implementación):

```java
public boolean contains(int x, int y) {
    // cuerpo: código que se ejecuta al invocar el método
}
```

- **Tipo de retorno** — tipo del valor devuelto; `void` si no devuelve nada.
- **Parámetros** — datos de entrada, con su tipo, separados por comas.
- La llamada debe coincidir en **número, tipo y orden** con la declaración.

> [!important] Java pasa todos los parámetros por valor
> En el caso de referencias a objetos se copia **la referencia**: el método no puede hacer que la variable original apunte a otro objeto, pero **sí puede modificar el estado** del objeto al que apunta (salvo que sea inmutable).

### 5.1 Ejemplo: métodos de `Rectangle`

```java
Rectangle r1 = new Rectangle(1, 5, 4, 10);
Rectangle r2 = new Rectangle(5, 3, 4, 6);

boolean dentro = r1.contains(3, 3);        // ¿contiene el punto (3,3)?
boolean comun  = r1.intersects(r2);        // ¿tienen zona en común?
Rectangle interseccion = r1.intersection(r2); // nuevo Rectangle
Rectangle union        = r1.union(r2);        // nuevo Rectangle
```

> [!note] Objetos creados sin `new`
> Un método también puede devolver un objeto nuevo (p. ej. `intersection`, `union`, `concat`). No hace falta llamar al constructor directamente para obtener una instancia.

### 5.2 Documentación: javadoc

La documentación de una clase (Javadoc) describe su **interfaz pública**: atributos públicos, constructores y métodos, con sus parámetros y valores de retorno. Es lo único que necesitamos conocer para usar una clase de la API sin ver su implementación interna.

### 5.3 Objetos inmutables

Una clase es **inmutable** cuando sus instancias no pueden cambiar de estado tras crearse. Son inmutables en Java:

- `String`,
- las clases envoltorio (`Integer`, `Double`, `Character`, `Boolean`, etc.),
- las clases de fecha y hora (`LocalDate`, `LocalTime`, `LocalDateTime`).

Cualquier método que "modificaría" el objeto devuelve en realidad una **nueva instancia**:

```java
String original = "Hola";
original.concat(" caracola");        // el resultado se pierde
System.out.println(original);        // Hola

String transformada = original.concat(" caracola");
System.out.println(transformada);    // Hola caracola
```

### 5.4 Comparar objetos: `equals` frente a `==`

- **`equals`** compara el **contenido/estado**: dos objetos distintos con los mismos valores son iguales.
- **`==`** compara las **referencias**: solo es `true` si ambas variables apuntan al mismo objeto.

```java
Rectangle r1 = new Rectangle(1, 2, 5, 4);
Rectangle r2 = new Rectangle(1, 2, 5, 4);
Rectangle r3 = r1;

r1.equals(r2); // true  (mismos valores)
r1 == r2;      // false (objetos distintos)
r1 == r3;      // true  (misma referencia)
```

> [!important] Regla práctica
> Para comparar objetos usa siempre **`equals`**. El operador `==` solo sirve para saber si dos referencias apuntan al mismo objeto.

### 5.5 Métodos estáticos

Un método **estático** (método de clase) se invoca desde la clase, sin crear ningún objeto:

```java
NombreClase.nombreMetodoEstatico();
```

No puede acceder al estado de una instancia y se usa para operaciones genéricas. La clase `Math` (`java.lang`) es el ejemplo típico: no se puede instanciar y todos sus métodos y constantes son estáticos.

```java
double angulo = 45.0 * Math.PI / 180.0;
System.out.println(Math.cos(angulo));
System.out.println(Math.sqrt(3));
System.out.println(Math.pow(10.0, 2.5));
System.out.println(Math.max(4, 9));
System.out.println(Math.abs(-7));
```

> [!tip] Invoca siempre con el nombre de la clase
> Aunque Java permite llamar a un método estático a través de un objeto, no es correcto: induce a pensar que depende de ese objeto. Escribe siempre `Math.round(...)`, `Integer.parseInt(...)`, etc.

#### Números aleatorios

**`Math.random()`** devuelve un `double` en `[0.0, 1.0)`. Para otros rangos se escala y se convierte:

```java
double real = Math.random();                 // [0.0, 1.0)
int hasta25 = (int) (Math.random() * 25);    // [0, 24]
int hasta25Incluido = (int) (Math.random() * 26); // [0, 25]
int redondeado = (int) Math.round(Math.random() * 25); // [0, 25]
int entre1y10 = (int) (Math.random() * 10) + 1;        // [1, 10]
```

En general, para un entero en `[0, N]` ambos incluidos: `(int) (Math.random() * (N + 1))`.

La clase **`Random`** (`java.util`) ofrece más posibilidades y permite fijar la semilla:

```java
import java.util.Random;

Random rnd = new Random();          // semilla distinta en cada ejecución
Random fijo = new Random(42);       // semilla fija (resultados reproducibles)

int cualquiera = rnd.nextInt();     // cualquier int
int entre0y24 = rnd.nextInt(25);    // [0, 25)
boolean cara = rnd.nextBoolean();
double real = rnd.nextDouble();     // [0.0, 1.0)
```

#### Métodos fábrica o pseudoconstructores

Son métodos estáticos que **fabrican** objetos de la propia clase, como si fueran constructores. Es el caso de `LocalDate.of(...)`, `LocalTime.now()`, `LocalDate.parse(...)`, etc.

### 5.6 Clases envoltorio y autoboxing

Cada tipo primitivo tiene una **clase envoltorio** que lo encapsula como objeto:

| Primitivo | Envoltorio |
|---|---|
| `boolean` | `Boolean` |
| `byte` | `Byte` |
| `char` | `Character` |
| `short` | `Short` |
| `int` | `Integer` |
| `long` | `Long` |
| `float` | `Float` |
| `double` | `Double` |

Se usan cuando una estructura de datos necesita objetos en lugar de primitivos. Desde Java 5 la conversión es automática:

```java
Integer oEntero = 20;        // autoboxing (primitivo → objeto)
int entero = oEntero;        // unboxing (objeto → primitivo)
```

> [!note] También son inmutables
> `oNumero += 3` no modifica el `Integer` original: crea una **nueva instancia** con el nuevo valor.

### 5.7 Representación textual: `toString`

Toda clase Java dispone de `toString()`, que devuelve una representación textual del objeto. Si no se ha reescrito, devuelve algo como `NombreClase@hash`, poco útil.

```java
Rectangle r1 = new Rectangle(1, 2, 5, 4);
System.out.println(r1.toString());
// java.awt.Rectangle[x=1,y=2,width=5,height=4]

System.out.println("r1 = " + r1); // llamada implícita a toString()
```

Cuando concatenamos un objeto con una cadena, Java llama a `toString()` automáticamente.

## 6. Paquetes y bibliotecas

Un **paquete** agrupa clases relacionadas. Las clases de un mismo paquete tienen acceso privilegiado entre sí (cierta "relación de confianza"). La declaración va al principio del archivo:

```java
package ejemplos;
```

Para usar una clase de otro paquete se importa:

```java
import java.util.Scanner;      // una clase concreta
import java.awt.*;             // todas las clases del paquete (no subpaquetes)
import java.util.regex.Pattern;
```

También se puede usar el nombre completamente cualificado sin importar:

```java
java.util.Scanner teclado = new java.util.Scanner(System.in);
```

Y existe el **import estático** para usar métodos o constantes sin el nombre de la clase:

```java
import static java.lang.Math.round;

System.out.println(round(20.2)); // 20
```

> [!tip] ¿Y `java.lang`?
> `java.lang` se importa automáticamente: por eso `System`, `String`, `Math` o `Integer` funcionan sin `import`.

Paquetes habituales de la API de Java:

| Paquete | Contenido |
|---|---|
| `java.lang` | Clases básicas (`Object`, `System`, `String`, envoltorios). Importado por defecto |
| `java.io` | Entrada/salida (ficheros, teclado) |
| `java.util` | Utilidades: `Scanner`, `Random`, colecciones |
| `java.math` | Precisión arbitraria: `BigInteger`, `BigDecimal` |
| `java.time` | Fechas y horas: `LocalDate`, `LocalTime`, `LocalDateTime` |
| `java.awt` / `javax.swing` | Interfaces gráficas (AWT y Swing) |
| `java.net` | Programación en red |
| `java.sql` | Acceso a bases de datos |
| `java.security` | Seguridad |

## 7. Entrada y salida por consola

La clase **`System`** (`java.lang`) proporciona tres objetos estáticos:

- `System.in` — entrada estándar (teclado).
- `System.out` — salida estándar (pantalla).
- `System.err` — salida de error estándar.

`System` no se instancia: se usa directamente.

### 7.1 Entrada con `BufferedReader`

`System.in` lee **bytes**. Para leer texto se encadenan `InputStreamReader` (bytes → caracteres) y `BufferedReader` (lectura por líneas):

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;

BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String linea = br.readLine();                  // lee una línea completa
int numero = Integer.parseInt(linea);          // String → int
```

Si el texto no representa un número válido, `parseInt` lanza `NumberFormatException`.

### 7.2 Entrada con `Scanner`

`Scanner` (`java.util`) permite leer directamente distintos tipos:

```java
import java.util.Scanner;

Scanner teclado = new Scanner(System.in);

int numero = teclado.nextInt();
double real = teclado.nextDouble();
String palabra = teclado.next();      // una palabra
String linea = teclado.nextLine();    // una línea completa
```

### 7.3 Salida con `System.out`

```java
System.out.print("Sin salto de línea");
System.out.println("Con salto de línea");
System.out.printf("Total: %.2f%n", 12345.1684); // formato
```

Códigos de formato habituales de `printf`: `%d` entero, `%f` real, `%e` notación científica, `%s` cadena, `%c` carácter, `%n` salto de línea. No modifican el valor de la variable, solo cómo se muestra.

### 7.4 Salida de error con `System.err`

`System.err` es también un `PrintStream`, pero asociado a la salida de error. Sirve para separar los mensajes de error de la salida normal (en IDE como NetBeans o Eclipse se muestran en otro color):

```java
System.out.println("Salida estándar");
System.err.println("Salida de error");
```

## 8. Fechas y horas: `java.time`

La API moderna (desde JDK 8) usa clases **inmutables** del paquete `java.time`. Se crean con métodos estáticos (`now`, `of`, `parse`) y cualquier operación devuelve una **nueva instancia**.

### 8.1 `LocalDate` — solo fecha

```java
import java.time.LocalDate;
import java.time.Month;

LocalDate hoy = LocalDate.now();
LocalDate fecha = LocalDate.of(1945, 11, 30);
LocalDate fecha2 = LocalDate.of(1945, Month.NOVEMBER, 30);
LocalDate parseada = LocalDate.parse("2019-12-26");

System.out.println(hoy); // 2026-10-20 (ISO 8601: año-mes-día)
```

### 8.2 `LocalTime` — solo hora

```java
import java.time.LocalTime;

LocalTime hora = LocalTime.of(20, 30, 45, 35); // h, m, s, ns
LocalTime ahora = LocalTime.now();
LocalTime parseada = LocalTime.parse("10:25:45");
```

### 8.3 `LocalDateTime` — fecha y hora

```java
import java.time.LocalDateTime;

LocalDateTime fechaHora = LocalDateTime.of(fecha, hora);
LocalDateTime ahora = LocalDateTime.now();

LocalDateTime mas20h   = ahora.plusHours(20);
LocalDateTime menos6m  = ahora.minusMonths(6);
LocalDateTime menos2d  = ahora.minusDays(2);
LocalDateTime parseada = LocalDateTime.parse("2020-11-28T19:34:50.63");
```

### 8.4 Formateo con `DateTimeFormatter`

```java
import java.time.format.DateTimeFormatter;

DateTimeFormatter isoFecha = DateTimeFormatter.ISO_LOCAL_DATE;
DateTimeFormatter isoHora  = DateTimeFormatter.ISO_LOCAL_TIME;

System.out.println(fechaHora.format(isoFecha));
System.out.println(fechaHora.format(isoHora));

DateTimeFormatter personalizado =
        DateTimeFormatter.ofPattern("'Hoy es' d 'del mes' M 'del año' yyyy 'y son las' HH 'horas'");
System.out.println(fechaHora.format(personalizado));
// Hoy es 21 del mes 10 del año 1989 y son las 17 horas
```

Letras de patrón: `d` día, `M` mes, `y` año, `H` hora (0-23), `h` hora (1-12), `m` minuto, `s` segundo. El texto entre comillas simples se imprime literal.

Constantes ISO: `ISO_LOCAL_DATE` (fecha), `ISO_LOCAL_TIME` (hora), `ISO_LOCAL_DATE_TIME` (fecha y hora).

### 8.5 `ChronoUnit` y `Period`

```java
import java.time.temporal.ChronoUnit;
import java.time.Period;

LocalDate semanaSig = hoy.plus(1, ChronoUnit.WEEKS);
LocalDate mesSig    = hoy.plus(1, ChronoUnit.MONTHS);
LocalDate anyoSig   = hoy.plus(1, ChronoUnit.YEARS);
LocalDate decadaSig = hoy.plus(1, ChronoUnit.DECADES);

long dias = ChronoUnit.DAYS.between(hoy, proximoCumple);
Period periodo = Period.between(hoy, proximoCumple);
```

`ChronoUnit` mide cantidades en una unidad simple; `Period` expresa la diferencia en años, meses y días.

## 9. Excepciones

Un programa puede compilar correctamente y fallar **en tiempo de ejecución** (división por cero, entrada no numérica, índice fuera de rango, etc.). Estos errores son **excepciones**.

Jerarquía: `Throwable` → `Error` (fallos de la JVM, no corregibles por el programa) y `Exception` (errores de nuestros programas).

### 9.1 Capturar con `try`/`catch`

```java
try {
    int numero = Integer.parseInt(teclado.nextLine());
    System.out.println("Número: " + numero);
} catch (NumberFormatException e) {
    System.out.println("No es un número válido: " + e.getMessage());
} finally {
    // se ejecuta siempre (opcional)
}
```

- Puede haber **varios `catch`**, uno por tipo de excepción.
- Los `catch` más **específicos** deben ir primero; el genérico `Exception` va al final.
- `finally` es opcional y se ejecuta siempre.

> [!warning] `throw` no es `throws`
> `throw` lanza una excepción de forma explícita; `throws` declara en la cabecera de un método qué excepciones puede lanzar. La delegación con `throws` se verá en unidades posteriores.

### 9.2 Interrupción y reanudación

Java usa el modelo de **interrupción**: la operación que falla se anula y se transfiere el control al `catch`. Para simular una **reanudación** (volver a intentarlo) se coloca el `try`/`catch` dentro de un bucle:

```java
boolean valido = false;
while (!valido) {
    try {
        int n = Integer.parseInt(teclado.nextLine());
        valido = true;
        System.out.println("Leído: " + n);
    } catch (NumberFormatException e) {
        System.out.println("Introduce un número válido, por favor.");
    }
}
```

Si no se captura una excepción, la JVM la trata por nosotros, muestra la traza y **detiene el programa**.

## Ver también

- [[UD1 - Entrada de datos con Scanner|Entrada de datos con Scanner]] — lectura por teclado y `close()`
- [[UD1 - Tipos de datos primitivos|Tipos de datos primitivos]] — base para entender referencias y envoltorios
- [[UD2 - Estructura condicional (if-else)|Condicionales]] y [[UD2 - Bucles (while, do-while, for)|Bucles]] — control de flujo usado en los ejemplos
- [[_Índice Programación]]

---

← Volver a [[_Índice Programación]]
