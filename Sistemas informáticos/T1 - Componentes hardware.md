---
tags:
  - sistemas-informaticos
  - tema1
  - hardware
  - cpu
  - memoria
  - placa-base
asignatura: Sistemas informáticos
tema: 1
subtema: Componentes hardware
---

# T1 — Componentes hardware

La parte física (hardware) de un equipo consta de:

---

## Microprocesador (CPU)

El centro neurálgico de procesamiento. Contiene:

### Partes de la CPU

| Componente | Función |
|---|---|
| **Unidad de control (UC)** | Procesamiento, interpretación y ejecución de instrucciones. Envía señales de control y estado |
| **Unidad aritmético-lógica (UAL)** | Realiza cálculos aritméticos y lógicos |
| **Registros** | Memorias temporales de poca capacidad y alta velocidad |

### Elementos integrados en el microprocesador actual

- **Núcleos**: estructuras con unidades funcionales independientes. Un procesador multinúcleo ejecuta varias tareas simultáneamente.
- **Memorias caché**:
  - **L1** (nivel 1): dentro de cada núcleo — muy rápida
  - **L2** (nivel 2): fuera de los núcleos, compartida entre varios — intermediaria
  - **L3** (nivel 3): fuera de los núcleos, compartida por todos — conecta con la memoria RAM
- **Controlador de memoria**: gestiona la RAM
- **Controlador gráfico**: capacidad de cálculo gráfico (no todos los procesadores lo integran)

---

## Memoria principal

Se encuentra conectada a la CPU y almacena instrucciones y datos de forma **temporal** (se borra al apagar).

### Componentes de la memoria principal

| Tipo | Descripción | Velocidad | Capacidad |
|---|---|---|---|
| **Registros** | Dentro de la CPU, 32 o 64 bits | Extremadamente rápida | Muy pequeña |
| **Caché (L1/L2/L3)** | Intermedia entre registros y RAM | Muy rápida | Poca |
| **RAM** | Módulos en la placa base | Rápida | Grande |

### Características de la memoria RAM

| Característica | Descripción |
|---|---|
| **Capacidad** | En GB |
| **Velocidad (frecuencia)** | En GHz |
| **Voltaje** | Tensión de funcionamiento (V) |
| **Latencia (CL)** | Tiempo de acceso en ciclos de reloj; menor = mejor |
| **Canales** | Paralelismo con el procesador (multicanal requiere parejas/cuartetos de módulos) |
| **Tipo de módulo** | DIMM (sobremesa) o SO-DIMM (portátil) |
| **Tecnología** | SDRAM DDR4 (menor voltaje, mayor frecuencia que DDR3) |

> [!tip] Priorizar capacidad sobre frecuencia
> Es más importante cubrir un mínimo de RAM suficiente para el SO y las aplicaciones que pagar extra por mayor frecuencia.

---

## Placa base (motherboard)

Circuito impreso principal que conecta todos los componentes. Determina:
- Potencia de cálculo
- Capacidad de expansión
- Tipo de almacenamiento y alimentación

Se rige por **factores de forma** (estándares de medidas y disposición).

---

## Dispositivos de almacenamiento secundario

Almacenamiento **permanente** (no se borra al apagar):

| Tipo | Tecnología | Ventajas |
|---|---|---|
| **HDD** | Disco magnético | Alta capacidad, bajo coste |
| **SSD** | Memoria flash | Muy rápido, sin partes mecánicas |
| **NVMe** | Conexión PCIe directa al bus | Velocidad máxima |

---

## Fuente de alimentación

Transforma la corriente alterna externa en los voltajes necesarios para el equipo:
- **3.3V**: componentes electrónicos de baja potencia
- **5V**: componentes electrónicos y mecánicos de poca potencia
- **12V**: dispositivos con motores o que necesitan valores mayores

---

## Periféricos

| Tipo | Ejemplos |
|---|---|
| **Entrada** | Teclado, ratón, escáner, micrófono |
| **Salida** | Monitor, altavoces, impresora |
| **Entrada/Salida** | Pantalla táctil, pendrive, tarjetas de red |

## Ver también

- [[T1 - Memorias y velocidad de almacenamiento|Memorias y velocidad]] — escala de medidas, MT/s, comparativa HDD/SSD
- [[T1 - Procesadores y rendimiento|Procesadores y rendimiento]] — velocidad de cómputo y caché
- [[T1 - Arquitectura de un sistema informático|Arquitectura]] — Von Neumann, buses
- [[T1 - Componentes software y arranque|Software y arranque]] — qué hace el software con el hardware
- [[T1 - Máquinas virtuales y VirtualBox|VirtualBox]] — cómo se virtualiza el hardware
- [[T2 - Funciones y tipos de sistemas operativos|Sistemas operativos]] — gestión de estos recursos

---

← Volver a [[_Índice Sistemas informáticos]]
