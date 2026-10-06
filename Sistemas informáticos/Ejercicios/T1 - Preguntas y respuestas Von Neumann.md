---
tags:
  - sistemas-informaticos
  - tema1
  - arquitectura
  - von-neumann
  - preguntas
  - trabajo
asignatura: Sistemas informáticos
tema: 1
subtema: Preguntas y respuestas sobre Von Neumann
---

# T1 — Preguntas y respuestas: Modelo de Von Neumann

## 1) Descripción general de la arquitectura

La arquitectura Von Neumann —también llamada **modelo de programa almacenado** o **arquitectura Princeton**— es el esquema conceptual de computador propuesto por **John von Neumann** (y colaboradores) en 1945, en el *First Draft of a Report on the EDVAC*. Define cómo debe organizarse un computador digital para que sea **reprogramable** sin cambiar físicamente la máquina.

Sus bases son:

- **Programa almacenado**: las instrucciones del programa **y** los datos residen en la **misma memoria** (RAM), indistinguibles por su ubicación; solo se diferencian por el modo en que se usan. Esto permite que un programa pueda tratarse como datos (base de compiladores y ensambladores).
- **Memoria direccionable**: cada celda se identifica con una **dirección única**, a la que se accede para leer o escribir.
- **Unidad central de proceso (CPU)**: ejecuta e interpreta instrucciones; incluye la **unidad de control (UC)**, la **unidad aritmético-lógica (UAL)** y los **registros** (entre ellos el **contador de programa, PC**).
- **Ejecución secuencial**: las instrucciones se ejecutan una tras otra en orden; el **contador de programa (PC)** indica cuál toca a continuación, y solo se altera con **instrucciones de salto** (transferencia de control).
- **Comunicación por un único bus**: CPU, memoria y E/S comparten un **mismo canal** de transmisión (datos, direcciones y control), lo que posteriormente generará el *cuello de botella de Von Neumann*.
- **Entrada/Salida**: periféricos que reciben datos (entrada) y entregan resultados (salida).

Contexto histórico: las máquinas anteriores (como la **ENIAC**, de la década de 1940) eran de **programa fijo**: se programaban cableando conmutadores y conexiones físicas, y cambiarlas podía llevar semanas. El modelo de Von Neumann revolucionó esto al **almacenar el programa en memoria** junto a los datos, permitiendo reprogramar la máquina con solo cargar software.

> [!note] Idea clave
> Todo el procesamiento gira en torno a una **memoria común** para datos e instrucciones y a una **ejecución paso a paso** controlada por el contador de programa.

## 2) Diagrama explicativo

```text
┌─────────────┐     ┌───────────────────────┐
│   ENTRADA   │────▶│         CPU           │
│  (teclado,  │     │ ┌────┐   ┌──────────┐ │
│   ratón...) │     │ │ UC │──▶│   UAL    │ │
└─────────────┘     │ └────┘   └──────────┘ │
                    │  ┌──────────────┐     │
┌─────────────┐     │  │  Registros   │     │
│   SALIDA    │◀────│  │  (incl. PC)  │     │
│ (monitor...)│     │  └──────────────┘     │
└─────────────┘     └───────▲───▲───────────┘
                            │   │   Bus único
                    ┌───────┴───┴────────┐
                    │   MEMORIA (datos   │
                    │  e instrucciones)  │
                    └────────────────────┘
```

### Explicación del diagrama

El diagrama representa el flujo de información de la arquitectura:

1. **Entrada** — los datos del exterior (teclado, ratón) entran a la **CPU**.
2. **CPU** — compuesta por la **UC** (interpreta órdenes), la **UAL** (hace los cálculos) y los **registros** (trabajo interno, incluye el PC).
3. **Bus único** — CPU ↔ **Memoria** por un solo camino compartido por el que viajan *datos*, *direcciones* y *control*; por eso instrucciones y datos compiten por el mismo canal (→ cuello de botella).
4. **Memoria** — contiene **datos e instrucciones juntos** (idea del programa almacenado).
5. **Salida** — la CPU manda los resultados al exterior (monitor, impresora).

La conexión vertical doble marca la comunicación **bidireccional** CPU↔memoria; las flechas laterales, la entrada y salida de datos por periféricos.

## 3) Descripción de sus componentes y comunicación

La arquitectura tiene **5 componentes funcionales**:

- **Unidad de control (UC)** — interpreta cada instrucción, genera las señales de control y gobierna el ciclo.
- **Unidad aritmético-lógica (UAL)** — ejecuta las operaciones aritméticas (+, −, ×) y lógicas (AND, OR, comparaciones).
- **Registros** — celdas ultrarrápidas dentro de la CPU; guardan operandos, resultados y el **PC** (dirección de la siguiente instrucción).
- **Memoria principal** — almacena **instrucciones y datos**; se accede por dirección y es volátil (se pierde al apagar).
- **Dispositivos E/S** — comunican la máquina con el exterior (teclado, monitor, disco).

### Comunicación por buses

Los buses son los **caminos físicos** que conectan todo. Hay **tres**:

- **Bus de datos** — los valores que se mueven: operandos de la memoria a la CPU y resultados a la memoria.
- **Bus de direcciones** — la **localización** (dirección de memoria) a la que se accede; la emite la CPU.
- **Bus de control** — las **señales de gobierno** de la UC: cuándo leer, cuándo escribir, sincronización con el reloj.

### Flujo de la comunicación en un ciclo

1. La **UC** pone en el **bus de direcciones** la celda a leer.
2. La **memoria** devuelve la instrucción por el **bus de datos**.
3. La **UC** la decodifica y, si hay cálculo, envía operandos a la **UAL**.
4. El resultado viaja de vuelta por el **bus de datos** a memoria o a un registro, todo coordinado por las señales del **bus de control**.

> [!tip] Punto clave
> En Von Neumann los **tres buses se comparten** entre instrucciones y datos (frente a Harvard, que los separa).

## 4) Comparativa vs. ordenadores modernos

La estructura de fondo es la misma —CPU, memoria y buses—, pero los modernos han evolucionado para **eliminar el cuello de botella** que limita a Von Neumann puro:

- **Memorias caché (L1/L2/L3)**: capas rápidas entre CPU y RAM; la CPU lee de la caché en vez de esperar a la memoria principal.
- **Pipelining**: solapan las fases del ciclo de instrucción (mientras una se ejecuta, la siguiente se decodifica).
- **Múltiples núcleos (multicore)**: varias UC/UAL en un mismo chip trabajando en paralelo; Von Neumann clásico era mononúcleo.
- **Harvard en caché**: cachés de instrucciones y de datos separadas, con acceso simultáneo.
- **Controlador de memoria integrado**: la CPU gestiona la RAM directamente, sin un bus externo lento.
- **Gráficos integrados y vectores (SIMD)**: una instrucción opera sobre muchos datos a la vez.
- **Ejecución fuera de orden (OoO)**: la CPU reordena instrucciones para no quedarse bloqueada esperando memoria.

Comparado con el modelo original (1945):

- **Unidad de proceso**: de un único núcleo (UC + UAL) → **multicore** con varios por chip.
- **Memoria**: de una sola RAM → **jerarquía** registros → L1/L2/L3 → RAM.
- **Acoplamiento CPU-memoria**: de un **solo bus compartido** → **múltiples buses** y controlador integrado.
- **Ejecución**: de secuencial estricta → **pipeline + fuera de orden**.
- **Datos e instrucciones**: por el **mismo canal** → **separados en caché** (Harvard híbrido).

### Veredicto

Los ordenadores actuales **no son Von Neumann puro ni Harvard puro**: usan un **modelo híbrido** que conserva la idea del programa almacenado (una sola memoria principal) pero adopta trucos de Harvard y técnicas modernas para acelerar. El esquema mental de Von Neumann sigue siendo la base para entender cómo funciona un PC.

## 5) Importancia en la informática

- **Hizo los ordenadores programables**: al guardar el programa en memoria, la misma máquina puede hacer de calculadora, editor o juego solo cargando software. Antes (ENIAC), reprogramar era recablear y podía llevar semanas.
- **Base de la industria del software**: compiladores, sistemas operativos y lenguajes existen porque las instrucciones se tratan como datos.
- **Modelo universal**: casi todos los procesadores actuales (x86, ARM, RISC-V) siguen su esquema CPU + memoria + buses. Entenderlo es entender cómo funciona un PC.
- **Punto de referencia**: el cuello de botella y arquitecturas alternativas (Harvard, neuromórfica, cuántica) se comparan siempre **contra** Von Neumann.

### En resumen

Es el esquema fundacional que hizo las máquinas **reprogramables con software** y sigue siendo la base para entender cualquier ordenador.

## 6) Cuello de botella de Von Neumann

En que la CPU y la memoria **comparten un único canal/bus**. Como por ahí circulan a la vez instrucciones y datos, no pueden moverse ambos simultáneamente y la CPU pasa **esperando a la memoria**, que además es más lenta que ella. Eso limita el rendimiento, y empeora con cada generación porque CPU y RAM crecen más rápido que el bus que las une. El término lo acuñó **John Backus** (Premio Turing, 1977).

## 7) Primeros computadores de arquitectura Von Neumann

- **SSEM "Baby"** (Universidad de Mánchester, **1948**) — primer ordenador del mundo en ejecutar un programa almacenado de verdad (un programa de factorización el 21 de junio de 1948).
- **EDSAC** (Universidad de Cambridge, **1949**) — primer computador electrónico *práctico* y completo de programa almacenado (6 de mayo de 1949).
- **EDVAC** (EE. UU., **1951**) — la máquina que dio nombre al informe de von Neumann; presentada en 1949 pero operativa de forma regular desde 1951.
- **IAS machine** (Princeton, **1952**) — construida siguiendo directamente el diseño de von Neumann; inspiró decenas de clones.
- **MANIAC I**, **ILLIAC**, **CSIRAC** — descendientes directos del diseño IAS; el CSIRAC (Australia, 1949) fue además de los primeros en reproducir música por computador.

**En una línea**: la gran mayoría fueron **clones del diseño IAS** (Princeton) y derivados de EDVAC/EDSAC, y "Baby" fue la pionera que demostró que el programa almacenado funcionaba.

## 8) Diferencias entre Von Neumann y Harvard

La principal diferencia es que Von Neumann **comparte** recursos mientras Harvard los **separa**:

- **Memoria**: Von Neumann usa una sola memoria para datos e instrucciones; Harvard usa dos memorias independientes (una para instrucciones y otra para datos).
- **Buses**: Von Neumann tiene un único bus compartido; Harvard tiene buses propios para cada memoria.
- **Acceso**: en Von Neumann la CPU solo hace un acceso por ciclo (o lee instrucción o mueve datos), lo que genera el *cuello de botella*; Harvard permite acceder a instrucciones y datos a la vez, resultando más rápida.
- **Complejidad y coste**: Harvard es más compleja y cara; Von Neumann es más sencilla y barata de implementar.
- **Uso actual**: los ordenadores modernos combinan ambas, usando Harvard en las cachés (instrucciones y datos separados) y Von Neumann en la memoria principal.

**En resumen**: Harvard sacrifica simplicidad por velocidad al separar instrucciones y datos; los sistemas actuales usan una mezcla de los dos modelos.

## 9) ¿En qué casos es más óptima cada arquitectura?

Von Neumann es más óptima cuando:

- Se necesita una máquina de **propósito general** (PC, portátil, servidor, smartphone): programas variados que cambian constantemente.
- El **coste y la simplicidad** pesan más que la velocidad máxima.
- Se quiere **reprogramar o actualizar el software** sin tocar hardware (programa en RAM).
- Se valoran la **flexibilidad** y aprovechar mejor la memoria (una sola RAM).

Harvard es más óptima cuando:

- Hay **tiempo real o determinismo**: aplicaciones embebidas (controles de coche, aviónica, robots) donde cada ciclo cuenta.
- El **programa es fijo** y cabe en memoria no volátil (ROM/flash), permitiendo acceder a datos e instrucciones a la vez.
- Se prioriza la **velocidad** sobre la complejidad: **DSP** (procesado de audio/señal), **tarjetas gráficas (GPU)**, microcontroladores (**Arduino/AVR, PIC**).
- No importa que sea más cara porque se fabrica en masa a bajo coste unitario.

**Regla mnemotécnica**: software cambiante + bajo coste → Von Neumann; programa fijo + velocidad/determinismo → Harvard. Y en la práctica, todo lo moderno es **híbrido**.

## 10) Clasificación de tipos de dispositivos

Cada arquitectura se usa en tipos de dispositivos distintos:

- **Von Neumann** (propósito general, software cambiante):
  - Ordenadores personales: PCs y portátiles.
  - Servidores y centros de datos.
  - Smartphones y tablets (a nivel de memoria principal).
  - Mainframes.

- **Híbrida** (Von Neumann + Harvard):
  - Prácticamente todo lo moderno: procesadores **Intel, AMD, ARM**.
  - Consolas de videojuegos.
  - GPUs y teléfonos actuales, porque las cachés separan instrucciones de datos (Harvard) sobre una memoria principal única (Von Neumann).

- **Harvard** (programa fijo, tiempos deterministas):
  - Microcontroladores embebidos: **Arduino/AVR, PIC, 8051**.
  - Procesadores **DSP** (audio, señales, radio).
  - **Tarjetas gráficas (GPU)**.
  - Firmwares embebidos: routers, impresoras, electrodomésticos, sistemas del coche, satélites.

**En una línea**: **general** → Von Neumann; **masivo/híbrido moderno** → mezcla; **embebido/tiempo real** → Harvard pura.

## Bibliografía

- **Wikipedia (es)** — *Arquitectura de Von Neumann*: origen del *First Draft* (EDVAC, 1945), definición formal, cuello de botella (John Backus, 1977), primeras máquinas y paliativos.
  <https://es.wikipedia.org/wiki/Arquitectura_de_von_Neumann>

- **LibreTexts Español** — *1.3: Arquitecturas de Von Neumann y Harvard*: comparativa de memorias y buses, diferencia de ciclos de acceso.
  <https://espanol.libretexts.org/Bookshelves/Ingenieria/Implementacion_de_una_CPU_de_una_direccion_en_Logisim_(Kann)/01:_Introducci%C3%B3n/1.03:_Arquitecturas_de_Von_Neumann_y_Harvard>

- **Kansas State University — Intro CS Textbook** — *Von Neumann Architecture*: componentes (control unit, ALU, memoria, E/S) y relevancia actual.
  <https://textbooks.cs.ksu.edu/cc110/i-concepts/05-universal-computers/10-von-neumann/index.html>

- **University of Illinois — CS102 (Spring 2026)** — *Computer components and architecture*: elementos del modelo y breve biografía de John von Neumann.
  <https://courses.grainger.illinois.edu/cs102/sp2026/text/architecture.html>

- **Beas Arco, J.** — *Sistemas informáticos* (Editorial Síntesis). Libro de clase.

> [!note] Nota
> El contenido se redactó resumiendo estas fuentes; los esquemas y diagramas ASCII son propios.

## Ver también

- [[T1 - Modelo de Von Neumann|Modelo de Von Neumann]] — teoría completa
- [[T1 - Arquitectura de un sistema informático|Arquitectura de un sistema informático]] — visión general y buses
- [[T1 - Componentes hardware|Componentes hardware]] — CPU, caché y RAM

---

← Volver a [[_Índice Sistemas informáticos]]