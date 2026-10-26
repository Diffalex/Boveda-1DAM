---
tags:
  - entornos-de-desarrollo
  - ud1
  - desarrollo-software
  - hardware
  - von-neumann
  - ide
  - case
  - rad
  - ciclo-vida
  - metodologias-agiles
  - scrum
  - kanban
  - xp
  - lenguajes
  - compilacion
  - bytecode
  - pruebas
  - mantenimiento
asignatura: Entornos de desarrollo
unidad: UD1
tema: Desarrollo de software
---

# UD1 — Desarrollo de software

Resumen de los apuntes oficiales `Anexos/ED01_Apuntes_Desarrollo_de_software.pdf` (25 páginas, RA1 y criterios CE1.a–CE1.g), completado con los enunciados `ED01 - Actividades Ud01..docx` y `ED01 - Actividades01 - Introducción y lenguajes.docx`.

> [!info] Cómo usar esta nota
> Las **definiciones** están en tablas o en párrafos breves; las **ideas clave** se destacan en callouts. Al final hay preguntas de autoevaluación y la correspondencia con los criterios de evaluación.
>
> Material original adaptado de la presentación «UA1. Desarrollo de software» de Luis del Moral Martínez y de los apuntes de Javier Gutiérrez (CC BY-NC-SA 4.0).

> [!info] Contenido
> 1. El ordenador y el software
> 2. Programas y aplicaciones informáticas
> 3. Lenguajes de programación
> 4. Traducción y compilación de código
> 5. Fases del desarrollo de una aplicación
> 6. Metodologías ágiles
> 7. Documentación, pruebas, mantenimiento y roles
> 8. Criterios de evaluación y autoevaluación

## 1. El ordenador y el software

### 1.1. Ordenador, hardware y software

| Concepto | Definición |
|---|---|
| **Ordenador** | Máquina que acepta datos de entrada, los procesa siguiendo instrucciones y produce resultados |
| **Hardware** | Parte física y tangible del sistema informático |
| **Software** | Parte lógica e intangible: programas e instrucciones que indican al hardware qué hacer |
| **Sistema operativo** | Software que gestiona los recursos del hardware y hace de intermediario entre aplicaciones y equipo |

El software **se desarrolla**, no se fabrica; normalmente no se estropea, aunque puede contener errores. Se crea con un lenguaje de programación y una metodología de trabajo.

### 1.2. Componentes principales

| Componente | Función |
|---|---|
| **CPU (procesador)** | Ejecuta las instrucciones. Contiene la **Unidad de Control (UC)**, que dirige la ejecución, y la **ALU**, que hace operaciones aritméticas y lógicas |
| **Memoria principal (RAM)** | Almacena temporalmente programas y datos mientras se ejecutan |
| **Periféricos de entrada/salida** | Comunican el ordenador con el usuario: teclado, ratón, pantalla, impresora... |

Hardware y software son inseparables: el hardware solo entiende **código binario**; el software escrito en un lenguaje de programación debe traducirse antes de ejecutarse.

### 1.3. Arquitectura de Von Neumann

Modelo de 1946 basado en el **programa almacenado**: las instrucciones y los datos comparten la misma memoria. Sus tres bloques son la **memoria principal**, la **CPU** (UC + ALU) y los **periféricos de E/S**.

| Fase del ciclo de instrucción | Qué ocurre |
|---|---|
| **Captación** | La UC busca en memoria la siguiente instrucción |
| **Decodificación** | La UC interpreta qué operación hay que realizar |
| **Ejecución** | La ALU realiza el cálculo o la comparación |
| **Almacenamiento** | El resultado vuelve a memoria o sale por un periférico; el ciclo se repite |

> [!important] Idea clave
> El **programa almacenado** permite que las instrucciones se guarden en memoria junto a los datos. Es la base de la arquitectura Von Neumann y del funcionamiento de los ordenadores actuales.

## 2. Programas y aplicaciones informáticas

### 2.1. Programa y aplicación

Un **programa** o **aplicación** es un conjunto de instrucciones que indican al ordenador cómo realizar un proceso. Se desarrolla con un lenguaje de programación; si el ordenador no entiende una instrucción, muestra un error. Ejemplos: sistemas operativos, ofimática, bases de datos, correo, mensajería y videojuegos.

| Tipo de software | Función | Ejemplos |
|---|---|---|
| **De sistema** | Gestiona el hardware y da soporte al resto | Sistema operativo, controladores, utilidades |
| **De programación** | Permite crear y depurar programas | Editores, compiladores, IDE, depuradores |
| **De aplicación** | Resuelve tareas concretas para el usuario | Ofimática, navegadores, juegos, gestión |
| **Malicioso** | Busca dañar o acceder sin permiso | Virus, troyanos, ransomware |

### 2.2. Software a medida frente a software estándar

| Aspecto | A medida | Estándar |
|---|---|---|
| **Desarrollo** | Según los requisitos de una empresa concreta | Genérico, válido para cualquier cliente |
| **Adquisición** | Requiere tiempo de desarrollo y mantenimiento propio | Se compra ya desarrollado y solo se configura |
| **Coste** | Suele ser más caro | Normalmente más barato |
| **Fiabilidad** | Menos probado (menos usuarios) | Más probado, suele tener menos errores |
| **Ajuste** | Hace justo lo necesario | Puede incluir funciones que no se usan o faltar alguna |

### 2.3. Librerías, IDE, CASE y RAD

| Concepto | Definición |
|---|---|
| **Librería (biblioteca)** | Conjunto de funciones o clases ya programadas que se pueden reutilizar (`java.util`, `java.io`) |
| **IDE** | Entorno Integrado de Desarrollo: reúne editor, compilador/intérprete y depurador en una sola interfaz |
| **CASE** | *Computer-Aided Software Engineering*: herramientas que automatizan tareas del desarrollo |
| **RAD** | *Rapid Application Development*: desarrollo rápido con prototipos funcionales y revisiones frecuentes del cliente |

#### Funciones de un IDE

| Función | Qué aporta |
|---|---|
| **Editor inteligente** | Coloreado de sintaxis, autocompletado y detección de errores en tiempo real |
| **Depurador** | Sigue variables y detiene la ejecución en puntos concretos |
| **Control de versiones** | Histórico de cambios y recuperación de versiones |
| **Refactorización** | Cambia el código sin alterar su funcionamiento |
| **Documentación** | Genera documentación a partir de comentarios |
| **Gestión de proyectos** | Organiza fuentes, compilados y recursos |

IDE habituales: **NetBeans**, **Eclipse**, **Visual Studio**, **C++ Builder** y **JBuilder**. La elección depende del lenguaje, la licencia y el tipo de proyecto.

#### Tipos de CASE

| Tipo | Fase en la que ayuda |
|---|---|
| **U-CASE** | Planificación y análisis |
| **M-CASE** | Diseño |
| **L-CASE** | Programación, pruebas y documentación |
| **I-CASE** | Integra varias fases en una misma herramienta |

Ventajas de CASE: menos errores humanos, documentación más completa y mayor coherencia. Ejemplos: StarUML y Visual Paradigm (diseño), SonarQube (calidad).

## 3. Lenguajes de programación

### 3.1. Definición y niveles

Un **lenguaje de programación** es un lenguaje artificial que permite expresar instrucciones comprensibles por el ordenador. Tiene **sintaxis** (símbolos y reglas de escritura) y **semántica** (significado de las instrucciones).

| Nivel | Descripción | Ejemplos |
|---|---|---|
| **Bajo nivel** | Código máquina (0/1), único que entiende directamente la CPU | Instrucciones binarias |
| **Medio nivel** | Mnemotécnicos cercanos al hardware | Ensamblador (`ADD`, `MOV`) |
| **Alto nivel** | Cercano al lenguaje humano | C, Java, Python, JavaScript |

> [!note] Clasificación según el curso
> En estos apuntes, el **lenguaje máquina** es bajo nivel, el **ensamblador** es medio y **C/Java/Python** son alto nivel. Otros materiales llaman “bajo” al ensamblador y “medio” a C; aquí seguimos la tabla anterior.

### 3.2. Paradigmas

| Paradigma | Idea principal | Ejemplos |
|---|---|---|
| **Estructurada (imperativa)** | Secuencia, selección e iteración organizadas en funciones o procedimientos | C, Pascal |
| **Orientada a objetos (imperativa)** | Clases y objetos que combinan datos y comportamiento | Java, Python |
| **Funcional (declarativa)** | Funciones matemáticas sin efectos secundarios | Haskell, Lisp |
| **Lógica (declarativa)** | Hechos y reglas; el sistema infiere la solución | Prolog |

Los lenguajes **imperativos** indican **cómo** hacerlo, paso a paso; los **declarativos** indican **qué** se quiere conseguir.

### 3.3. Ejemplos mínimos

**C — programación estructurada:**

```c
#include <stdio.h>

int main() {
    for (int i = 1; i <= 5; i++)
        printf("%d\n", i);
}
```

Secuencia, iteración (`for`) y función (`main`); imprime del 1 al 5.

**Java — orientación a objetos:**

```java
class Perro {
    String nombre;

    void ladrar() {
        System.out.println(nombre + ": ¡Guau!");
    }
}
```

Una **clase** es la plantilla; un **objeto** es una instancia concreta creada con `new Perro()`. `nombre` es un atributo y `ladrar()` un método.

**Prolog — programación lógica:**

```prolog
padre(juan, maria).
padre(juan, pedro).
padre(pedro, ana).

abuelo(X, Z) :- padre(X, Y), padre(Y, Z).
```

Los **hechos** afirman algo; las **reglas** definen relaciones; las consultas permiten inferir respuestas.

**Lisp — programación funcional:**

```lisp
(defun factorial (n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))
```

La **recursión** sustituye al bucle: caso base y caso recursivo. Las funciones de orden superior, como `mapcar`, reciben funciones como argumento.

### 3.4. Código fuente, objeto y ejecutable

| Tipo | Definición |
|---|---|
| **Código fuente** | El que escribe el programador en un lenguaje de programación |
| **Código objeto** | Código máquina o intermedio generado tras compilar; aún puede necesitar enlazado |
| **Ejecutable** | Programa final listo para ejecutarse, con las librerías enlazadas |

### 3.5. Características deseables del código

| Característica | Significado |
|---|---|
| **Modularidad** | Dividido en partes pequeñas y manejables |
| **Corrección** | Hace exactamente lo que se pide |
| **Legibilidad** | Es fácil de leer y mantener |
| **Eficiencia** | Aprovecha bien los recursos |
| **Portabilidad** | Puede ejecutarse en distintos equipos |

El código fuente puede ser **abierto** (se puede estudiar y modificar) o **cerrado** (uso restringido).

### 3.6. Criterios para elegir un lenguaje

| Criterio | Pregunta que responde |
|---|---|
| **Tipo de aplicación** | ¿Web, escritorio, móvil, videojuego, ciencia de datos? |
| **Rendimiento** | ¿Se necesita máxima velocidad o basta con un buen tiempo de respuesta? |
| **Portabilidad** | ¿Debe funcionar en varios sistemas sin cambios? |
| **Ecosistema** | ¿Hay librerías, documentación y comunidad suficientes? |
| **Curva de aprendizaje** | ¿El equipo ya lo conoce o hay que formarse? |
| **Seguridad y mantenimiento** | ¿Es crítico y debe mantenerse durante años? |

No existe un lenguaje mejor en absoluto: depende del problema, del equipo y del entorno.

## 4. Traducción y compilación de código

### 4.1. Traductores

Un **traductor** convierte un lenguaje de alto nivel en ensamblador o lenguaje máquina. Hay dos tipos principales:

- **Compilador:** traduce todo el programa antes de ejecutarlo.
- **Intérprete:** traduce y ejecuta el código línea a línea, “al vuelo”.

### 4.2. Fases de la compilación

| Paso | Fase | Qué ocurre |
|---|---|---|
| 1 | **Código fuente** | Archivo escrito por el programador (`hola.c`) |
| 2 | **Preprocesado** | Se procesan directivas (`#include`, `#define`) y se eliminan comentarios |
| 3 | **Compilación** | Se comprueba la sintaxis y se traduce a código máquina; aquí aparecen los errores de compilación |
| 4 | **Código objeto** | Archivo con código máquina (`hola.o`), aún sin librerías |
| 5 | **Enlazado** | El enlazador une el objeto con las librerías y genera el ejecutable |

Con `gcc`:

```bash
gcc -c hola.c          # genera hola.o (objeto)
gcc hola.o -o hola     # enlaza y genera hola (ejecutable)
./hola                 # ejecuta
gcc hola.c -o hola     # todo de una vez
```

> [!important] Idea clave
> El ejecutable resultante es **independiente**: se puede ejecutar sin el compilador.

### 4.3. Interpretación

| Paso | Fase | Qué ocurre |
|---|---|---|
| 1 | **Leer** | El intérprete lee la siguiente línea |
| 2 | **Analizar y traducir** | Comprueba la sintaxis y traduce solo esa instrucción |
| 3 | **Ejecutar** | La instrucción se ejecuta de inmediato |
| 4 | **¿Más líneas?** | Si quedan, vuelve al paso 1; si no, termina |

Si hay un error, la ejecución se detiene **en esa línea**: el error aparece al llegar a ella, no antes. Ejemplos: Python, JavaScript, PHP, Bash.

### 4.4. Compilado frente a interpretado

| Aspecto | Compilador | Intérprete |
|---|---|---|
| **Cuándo traduce** | Todo el programa, antes de ejecutar | Línea a línea, durante la ejecución |
| **Resultado** | Ejecutable independiente | No genera ejecutable propio |
| **Velocidad** | Más rápido al ejecutar | Más lento: traduce cada vez |
| **Errores** | Se detectan antes de ejecutar | Aparecen al llegar a la línea |
| **Equipo destino** | Basta con el ejecutable | Hace falta el intérprete |
| **Ejemplos** | C, C++ | PHP, JavaScript, Python, Bash |

### 4.5. Lenguajes virtuales, bytecode y máquinas virtuales

| Tipo | Funcionamiento | Ejemplo |
|---|---|---|
| **Compilado** | Traducción completa y ejecutable independiente; más rápido | C/C++ |
| **Interpretado** | Traducción y ejecución línea a línea; necesita intérprete | PHP, JavaScript |
| **Virtual** | Se compila a **bytecode** y lo ejecuta una máquina virtual | Java |

El **bytecode** es un código intermedio independiente del sistema. La **máquina virtual** lo ejecuta en cada equipo.

Funciones de una máquina virtual:

- Hace de **puente** entre el bytecode y el hardware.
- Garantiza **portabilidad** sin recompilar.
- Gestiona la **memoria** automáticamente (recolector de basura).
- Verifica el bytecode y protege la memoria (seguridad y estabilidad).
- **Interpreta** el bytecode o lo **compila con JIT** para mejorar el rendimiento.

> [!note] Ventaja e inconveniente
> El bytecode es portable, pero su ejecución puede ser algo más lenta que la de un lenguaje compilado directamente.

### 4.6. Java: del código a la ejecución

| Paso | Elemento | Qué ocurre |
|---|---|---|
| 1 | **Código fuente** | `Hola.java`, escrito por el programador |
| 2 | **Compilador `javac`** | Traduce el fuente a bytecode |
| 3 | **Bytecode** | `Hola.class`, igual en todos los sistemas |
| 4 | **JVM** | Ejecuta el bytecode: lo interpreta o lo compila con JIT |

| Sigla | Significado |
|---|---|
| **JDK** | Java Development Kit: para desarrollar; incluye `javac`, herramientas y el JRE |
| **JRE** | Java Runtime Environment: para ejecutar; incluye la JVM y las bibliotecas estándar |
| **JVM** | Java Virtual Machine: ejecuta el bytecode y gestiona la memoria |

> [!important] “Escribe una vez, ejecuta en cualquier sitio”
> El mismo `.class` funciona con la JVM de cualquier sistema compatible.

### 4.7. Framework y entorno de ejecución

| Concepto | Definición |
|---|---|
| **Framework** | Plataforma con bibliotecas y estructuras ya construidas; acelera el desarrollo, pero crea dependencia. Ejemplos: .NET, Spring |
| **Runtime (entorno de ejecución)** | Utilidades para ejecutar programas compilados: máquina virtual + bibliotecas estándar. Ejemplo: JRE |

## 5. Fases del desarrollo de una aplicación

### 5.1. Las ocho fases

| Nº | Fase | Qué se hace |
|---|---|---|
| 1 | **Fase inicial** | Estudio de viabilidad: idea, costes, plazos y recursos |
| 2 | **Análisis** | Se recogen y documentan los requisitos del cliente |
| 3 | **Diseño** | Arquitectura, base de datos, interfaces y módulos |
| 4 | **Implementación** | Se escribe el código y se integran los módulos |
| 5 | **Pruebas** | Se comprueba que cumple los requisitos y no tiene errores |
| 6 | **Explotación** | Instalación, puesta en marcha y formación de usuarios |
| 7 | **Mantenimiento** | Corrección de errores y mejoras con el software en producción |
| 8 | **Retirada** | Fin del soporte y migración de datos a otro sistema |

Un **requisito** es una necesidad o condición que el software debe cumplir según el cliente.

### 5.2. Modelos de ciclo de vida

Un **modelo de ciclo de vida** organiza y encadena las fases. Hay dos familias:

- **Clásicos o predictivos:** se planifica todo al principio. Cascada, cascada con realimentación, en V, iterativo incremental, prototipado y espiral.
- **Ágiles o adaptativos:** entregas cortas y frecuentes; el cambio es bienvenido. Scrum, Kanban, XP, Lean, Scrumban y DevOps.

La elección depende de la **estabilidad de los requisitos**, el **tamaño**, el **riesgo** y la **implicación del cliente**.

| Modelo | Cuándo usarlo | Ventaja | Inconveniente |
|---|---|---|---|
| **Cascada** | Requisitos claros y estables; proyectos pequeños | Sencillo y bien documentado | Rígido: no admite cambios |
| **En V** | Software crítico; pruebas clave | Pruebas planificadas desde el inicio | Poco flexible |
| **Iterativo incremental** | Proyectos medianos con entregas parciales | Resultados pronto y errores tempranos | Exige buena arquitectura |
| **Espiral** | Proyectos grandes, caros y de alto riesgo | Gestiona riesgos desde el inicio | Complejo y costoso |
| **Scrum** | Requisitos cambiantes; equipos pequeños | Entregas cortas y cliente implicado | Exige mucha implicación |
| **Kanban** | Soporte, mantenimiento y flujo continuo | Flexible y fácil de implantar | Sin plazos fijos: menos previsible |

#### Cascada y cascada con realimentación

Las fases se suceden **en orden estricto**, sin vuelta atrás. La **cascada con realimentación** permite volver a la fase anterior para corregir errores. El cliente ve el producto al final y los errores se detectan tarde.

#### Modelo en V

Variante de la cascada en la que **cada fase de diseño tiene asociada una fase de pruebas**. En el vértice está la codificación. Es muy usado en software crítico, pero poco flexible.

#### Iterativo incremental y prototipado

- **Iterativo:** se repite el ciclo mejorando el producto en cada vuelta.
- **Incremental:** cada ciclo añade una parte funcional nueva.
- **Prototipado:** se construye una versión preliminar para validar requisitos. Puede ser **desechable** (se tira) o **evolutivo** (se mejora hasta el producto final).

#### Espiral

Modelo iterativo centrado en el **análisis de riesgos**; combina prototipado y cascada. Cada vuelta recorre: objetivos, análisis de riesgos, desarrollo y pruebas, y planificación de la siguiente vuelta.

## 6. Metodologías ágiles

### 6.1. Manifiesto Ágil

Documento de 2001 con **cuatro valores**:

| Se valora más... | ...que |
|---|---|
| **Individuos e interacciones** | Procesos y herramientas |
| **Software funcionando** | Documentación exhaustiva |
| **Colaboración con el cliente** | Negociación contractual |
| **Respuesta ante el cambio** | Seguir un plan rígido |

Se concreta en **12 principios**: entregas frecuentes, cambios bienvenidos, equipos autoorganizados, simplicidad y mejora continua, entre otros.

### 6.2. Scrum

Marco ágil que organiza el trabajo en **sprints** (iteraciones de 1 a 4 semanas) y entrega un incremento al final de cada uno.

| Elemento | Contenido |
|---|---|
| **Roles** | **Product Owner** (define y prioriza qué se construye), **Scrum Master** (facilita el proceso y elimina obstáculos) y **equipo de desarrollo** (construye, autoorganizado) |
| **Eventos** | Sprint, planificación del Sprint, Scrum diario (15 min), revisión del Sprint y retrospectiva |
| **Artefactos** | **Product Backlog** (lista priorizada), **Sprint Backlog** (tareas del sprint) e **Incremento** (producto funcional) |

Sinónimos habituales: *jefe de proyecto* ≈ Product Owner; *cliente* ≈ stakeholders/Product Owner; *equipo de desarrollo* = Development Team.

#### Historias de usuario

Una **historia de usuario** describe una necesidad desde el punto de vista del usuario, no como una especificación técnica:

> Como **[rol]**, quiero **[acción]** para **[beneficio]**.

Ejemplo: «Como cliente, quiero recuperar mi contraseña para volver a entrar en mi cuenta». Se completa con **criterios de aceptación** verificables y se prioriza dentro del Product Backlog.

### 6.3. Kanban

Método ágil que organiza el trabajo **visualmente** en un tablero de columnas (Por hacer, En curso, Hecho) y limita el trabajo simultáneo.

- Origen: Toyota; “kanban” significa tarjeta.
- Visualizar el trabajo con tarjetas.
- Limitar el **WIP** (*Work In Progress*): máximo de tareas en curso.
- **Flujo continuo**, sin sprints ni fechas fijas.
- Medir el **lead time** y detectar cuellos de botella.
- Muy usado en mantenimiento y soporte.

| Aspecto | Kanban | Scrum |
|---|---|---|
| **Iteraciones** | Flujo continuo, sin sprints | Sprints de 1-4 semanas |
| **Roles** | No define roles obligatorios | Product Owner, Scrum Master y equipo |
| **Cambios** | Se pueden añadir tareas en cualquier momento | Se fijan al inicio del sprint |
| **Métrica principal** | Lead time y WIP | Velocidad del equipo |
| **Ideal para** | Soporte y mantenimiento | Desarrollo con requisitos cambiantes |

### 6.4. Otras metodologías

| Metodología | Idea principal |
|---|---|
| **XP** | Programación en parejas, pruebas antes del código (TDD) e integración continua |
| **Lean** | Eliminar desperdicio, entregar rápido y mejorar de forma continua |
| **Scrumban** | Mezcla Scrum (roles, sprints) con Kanban (tablero y límites WIP) |
| **DevOps** | Une desarrollo y operaciones: automatiza integración, pruebas y despliegue (CI/CD) |

**XP** se apoya en cinco valores: **comunicación, simplicidad, feedback, coraje y respeto**. Prácticas habituales: programación en parejas, TDD, integración continua, entregas pequeñas y refactorización.

**Lean** busca eliminar todo lo que no aporta valor: trabajo en curso excesivo, esperas, defectos, tareas innecesarias y burocracia. Sus siete principios son: eliminar desperdicios, entregar rápido, generar conocimiento, aplazar decisiones, empoderar al equipo, construir calidad desde el inicio y optimizar el conjunto.

## 7. Documentación, pruebas, mantenimiento y roles

### 7.1. Documentación

| Manual | A quién va dirigido |
|---|---|
| **Manual de usuario** | Explica cómo usar la aplicación |
| **Manual técnico** | Dirigido a programadores y administradores |
| **Manual de instalación** | Detalla el proceso de instalación |

### 7.2. Pruebas

| Tipo | Qué comprueba |
|---|---|
| **Unitarias** | Cada parte del software por separado |
| **De integración** | Que todas las partes funcionan juntas |
| **Beta test** | Prueba final en el entorno real, con el cliente |

> [!important] Verificación y validación
> **Verificación:** ¿estamos construyendo el producto **correctamente**? Comprueba que cumple las especificaciones y está bien hecho.
>
> **Validación:** ¿estamos construyendo el **producto correcto**? Comprueba que satisface las necesidades reales del cliente.
>
> La verificación mira las especificaciones; la validación, el uso real.

### 7.3. Mantenimiento

| Tipo | Qué hace |
|---|---|
| **Correctivo** | Soluciona errores detectados |
| **Perfectivo** | Mejora la funcionalidad existente |
| **Evolutivo** | Añade nuevas funciones que pide el cliente |
| **Adaptativo** | Adapta el software a nuevos entornos o tecnologías |

### 7.4. Roles

| Rol | Responsabilidad |
|---|---|
| **Arquitecto de software** | Decide la estructura del proyecto y las tecnologías |
| **Jefe de proyecto** | Dirige el equipo, gestiona tiempos y trata con el cliente |
| **Analista** | Estudia el problema y diseña el sistema |
| **Programador** | Codifica y prueba los módulos |

## 8. Criterios de evaluación y autoevaluación

### 8.1. Correspondencia con los criterios

| Criterio | Contenido | Apartados |
|---|---|---|
| **CE1.a** | Relación de los programas con los componentes del sistema: memoria, procesador, periféricos | 1 |
| **CE1.b** | Clasificación de los lenguajes de programación | 3.1–3.3 |
| **CE1.c** | Diferenciación entre código fuente, objeto y ejecutable | 3.4–3.5 |
| **CE1.d** | Generación de código intermedio para máquinas virtuales | 4.5–4.7 |
| **CE1.e** | Funcionalidad de las herramientas de programación | 2.2–2.3 |
| **CE1.f** | Funcionamiento de los traductores de lenguajes | 4.1–4.4 |
| **CE1.g** | Fases del desarrollo de una aplicación | 5–7 |

### 8.2. Preguntas de autoevaluación

1. ¿Qué diferencia hay entre hardware y software? Pon un ejemplo de cada uno.
2. ¿Qué dos unidades componen la CPU y qué hace cada una?
3. Explica el concepto de “programa almacenado” y las cuatro fases del ciclo de instrucción.
4. Compara software a medida y software estándar.
5. ¿Qué componentes forman un IDE y qué funciones añade frente a un editor simple?
6. ¿Qué significan las siglas CASE y qué tipos hay?
7. Ordena de menor a mayor cercanía al lenguaje humano: alto nivel, lenguaje máquina y ensamblador.
8. Diferencia paradigma imperativo y declarativo y cita un lenguaje de cada uno.
9. ¿Qué diferencia hay entre código fuente, código objeto y ejecutable?
10. Ordena las fases de la compilación y explica qué hace el enlazador.
11. ¿Por qué los errores de un programa interpretado aparecen más tarde que los de uno compilado?
12. Describe el recorrido de un programa Java desde `Hola.java` hasta su ejecución y diferencia JDK, JRE y JVM.
13. Enumera las ocho fases del desarrollo de una aplicación.
14. ¿Qué diferencia un modelo predictivo de uno ágil?
15. ¿Qué roles, eventos y artefactos tiene Scrum?
16. Explica qué es un tablero Kanban y qué significa limitar el WIP.
17. Distingue mantenimiento correctivo, perfectivo, evolutivo y adaptativo.

## Ver también

- [[Entornos de desarrollo/Ejercicios/UD1 - ED01 Actividades|ED01 — Actividades resueltas]] — respuestas del cuestionario
- [[Entornos de desarrollo/Ejercicios/UD1 - Práctica 01 (compilación vs interpretación)|Práctica 01 — Compilación vs interpretación]]
- [[Entornos de desarrollo/Ejercicios/UD1 - Práctica 01 (IntelliJ)|Práctica 01 — IntelliJ: fuente, objeto y ejecutable]]
- [[UD1 - Cuestiones previas|Cuestiones previas]]
- [[_Índice Entornos de desarrollo]]

---

← Volver a [[_Índice Entornos de desarrollo]]
