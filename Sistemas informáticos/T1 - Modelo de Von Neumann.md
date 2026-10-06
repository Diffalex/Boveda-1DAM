---
tags:
  - sistemas-informaticos
  - tema1
  - arquitectura
  - von-neumann
  - cpu
asignatura: Sistemas informáticos
tema: 1
subtema: Modelo de Von Neumann
---

# T1 — Modelo de Von Neumann

Arquitectura de computador de **programa almacenado**, base de prácticamente todos los ordenadores modernos.

## Descripción general

La arquitectura Von Neumann —también llamada **modelo de programa almacenado** o **arquitectura Princeton**— es el esquema conceptual de computador propuesto en 1945 por **John von Neumann** y colaboradores en el *First Draft of a Report on the EDVAC*. Define cómo organizar un computador digital para que sea **reprogramable** sin cambiar físicamente la máquina.

Sus bases son:

- **Programa almacenado**: instrucciones **y** datos residen en la **misma memoria** (RAM), indistinguibles por su ubicación; solo se diferencian por el modo en que se usan. Permite que un programa se trate como datos (base de compiladores y ensambladores).
- **Memoria direccionable**: cada celda se identifica con una **dirección única**, a la que se accede para leer o escribir.
- **Unidad central de proceso (CPU)**: ejecuta e interpreta instrucciones; incluye la **unidad de control (UC)**, la **unidad aritmético-lógica (UAL)** y los **registros** (entre ellos el **contador de programa, PC**).
- **Ejecución secuencial**: las instrucciones se ejecutan una tras otra en orden; el **contador de programa (PC)** indica cuál toca a continuación y solo se altera con **instrucciones de salto** (transferencia de control).
- **Comunicación por un único bus**: CPU, memoria y E/S comparten un **mismo canal** de transmisión (datos, direcciones y control), origen del *cuello de botella de Von Neumann*.
- **Entrada/Salida**: periféricos que aportan datos (entrada) y entregan resultados (salida).

> [!note] Idea clave
> Todo el procesamiento gira en torno a una **memoria común** para datos e instrucciones y a una **ejecución paso a paso** controlada por el contador de programa.

## Origen

Descrita en 1945 por el matemático y físico **John von Neumann** y otros colaboradores en el *First Draft of a Report on the EDVAC* (primer borrador de un informe sobre el EDVAC), un diseño para un computador digital electrónico. Por ello también recibe el nombre de **arquitectura Princeton**.

Su novedad frente a las máquinas anteriores (p. ej. la ENIAC, programada con conmutadores y cables) es que el **programa se guarda en memoria** junto con los datos, en lugar de venir "cableado" físicamente.

## Componentes

| Unidad | Función |
|---|---|
| **CPU** | Ejecuta e interpreta instrucciones |
| — **Unidad de control (UC)** | Decide qué operación hacer, cuándo y sobre qué operandos |
| — **Unidad aritmético-lógica (UAL/ALU)** | Realiza los cálculos aritméticos y lógicos |
| — **Registros** | Memorias temporales de poca capacidad y alta velocidad (incluyen PC, registros de instrucción y de propósito general) |
| **Memoria** | Almacena tanto instrucciones como datos |
| **Dispositivos de E/S** | Interfaz con el exterior (entrada y salida) |

Todas las unidades se comunican mediante **buses del sistema**:

| Tipo de bus            | Función                                              |
| ---------------------- | ---------------------------------------------------- |
| **Bus de datos**       | Circulan los datos de las operaciones                |
| **Bus de direcciones** | Circula la dirección de memoria a la que se accede   |
| **Bus de control**     | Circulan las señales de control generadas por la UC   |

## Programa almacenado

La característica clave: **datos e instrucciones comparten la misma memoria** (RAM) y el mismo camino de acceso.

Consecuencias:
- Permite escribir programas que tratan instrucciones como datos: **ensambladores, compiladores, enlazadores y cargadores** ("programas que escriben programas").
- Posibilita el **código automodificable** (históricamente útil; hoy en desuso por difícil de depurar).
- Riesgo: un programa erróneo o malicioso puede sobrescribir otros programas o el SO; se mitiga con **protección de memoria** y control de acceso.

## Definición formal

Un computador es de arquitectura Von Neumann cuando:

1. Programas y datos se almacenan en una **memoria común**.
2. Cada **celda de memoria** se identifica con una **dirección única**.
3. Instrucciones y datos tienen distintos modos de uso, pero no se distinguen por su codificación en memoria.
4. El programa se **ejecuta de forma secuencial**, comenzando por la primera instrucción; se altera con instrucciones de **salto** (transferencia de control).

## Ciclo de instrucción

La UC va extrayendo y ejecutando instrucciones de memoria una tras otra:

| Fase                     | Qué ocurre                                                                     |
| ------------------------ | ------------------------------------------------------------------------------ |
| **Buscar (fetch)**       | Se lee de memoria la instrucción apuntada por el **contador de programa (PC)** |
| **Decodificar (decode)** | Se interpreta la instrucción y se calculan las direcciones de los operandos    |
| **Ejecutar (execute)**   | Se extraen los operandos y se realiza la operación (p. ej. en la UAL)          |
| **Almacenar (store)**    | Se guarda el resultado y se actualiza el PC (posible salto)                    |

## Cuello de botella de Von Neumann

Al compartir datos e instrucciones un **único canal/bus** entre CPU y memoria, no pueden realizarse a la vez la búsqueda de una instrucción y una operación de datos. Ese canal compartido limita la **tasa de transferencia** y la CPU queda esperando a la memoria, reduciendo el rendimiento.

> [!tip] Origen del término
> El término *von Neumann bottleneck* lo acuñó **John Backus** en su discurso del **Premio Turing (1977)**.

El problema crece con cada generación: la velocidad del procesador y la capacidad de memoria aumentan más rápido que la capacidad de transferencia entre ambos.

### Paliativos

- **Memorias caché** (L1/L2/L3) y **pipelining** (solapamiento de fases del ciclo).
- **Arquitectura Harvard**: memorias separadas para instrucciones y datos, permitiendo acceso simultáneo.
- Arquitecturas **híbridas** actuales: los computadores modernos combinan ideas de ambos modelos.

## Comparativa Harvard

| Característica | Von Neumann | Harvard |
|---|---|---|
| Memoria | Única para datos e instrucciones | Separada (una para datos, otra para instrucciones) |
| Acceso | Un bus compartido | Buses dedicados por tipo |
| Rendimiento | Cuello de botella | Puede acceder a ambos a la vez |

## Ver también

- [[T1 - Preguntas y respuestas Von Neumann|Preguntas y respuestas Von Neumann]] — resumen con diagrama y comparativas
- [[T1 - Arquitectura de un sistema informático|Arquitectura de un sistema informático]] — visión general y el modelo de Harvard
- [[T1 - Componentes hardware|Componentes hardware]] — CPU, memorias caché y RAM
- [[T1 - Componentes software y arranque|Software y arranque]] — qué hace el software sobre este hardware

---

← Volver a [[_Índice Sistemas informáticos]]