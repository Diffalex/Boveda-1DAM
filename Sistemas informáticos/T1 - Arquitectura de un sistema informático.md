---
tags:
  - sistemas-informaticos
  - tema1
  - arquitectura
  - hardware
asignatura: Sistemas informáticos
tema: 1
subtema: Arquitectura e introducción
---

# T1 — Arquitectura de un sistema informático

## ¿Qué es un sistema informático?

Un **sistema informático** es una máquina que:
1. Acepta datos de **entrada**
2. Los **procesa**
3. Genera **resultados** (salida)

Se compone de dos partes fundamentales:
- **Hardware**: elementos físicos y tangibles
- **Software**: parte intangible (instrucciones y datos)

---

## Modelos de arquitectura

### Modelo de Von Neumann

Compuesto por tres unidades principales:

| Unidad | Función |
|---|---|
| **Unidad de procesamiento (CPU)** | Ejecuta e interpreta instrucciones. Incluye la ALU (aritmético-lógica) y la unidad de control |
| **Memoria** | Almacena instrucciones y datos |
| **Dispositivos de entrada/salida** | Interfaz con el exterior |

Las unidades se comunican mediante **buses del sistema**:

| Tipo de bus              | Función                                                   |
| ------------------------ | --------------------------------------------------------- |
| **Bus de instrucciones** | Transmite instrucciones                                   |
| **Bus de datos**         | Transmite datos                                           |
| **Bus de direcciones**   | Accede a memorias indicando dirección (lectura/escritura) |

> [!info] Ampliación
> Detalle completo (origen, programa almacenado, ciclo de instrucción y cuello de botella) en [[T1 - Modelo de Von Neumann|Modelo de Von Neumann]].

### Modelo de Harvard

Mejora de Von Neumann: accede a **instrucciones y datos simultáneamente** al encontrarlos en caminos distintos.

> [!tip] Actuales
> Los sistemas actuales combinan ideas de ambos modelos.

---

## Glosario del tema

| Término | Definición |
|---|---|
| **Motherboard / placa base** | Circuito impreso principal que conecta todos los componentes |
| **Sistema informático** | Máquina que acepta datos, los procesa y genera resultados |
| **Sistema operativo** | Software que actúa de interfaz y gestiona recursos HW y SW |
| **Software** | Parte lógica e intangible del sistema informático |
| **Virtualización** | Abstracción de los recursos hardware |

## Ver también

- [[T1 - Componentes hardware|Componentes hardware]] — detalles de CPU, memoria, etc.
- [[T1 - Componentes software y arranque|Software y arranque]] — tipos de software
- [[T1 - Máquinas virtuales y VirtualBox|VirtualBox]] — uso de máquinas virtuales

---

← Volver a [[_Índice Sistemas informáticos]]
