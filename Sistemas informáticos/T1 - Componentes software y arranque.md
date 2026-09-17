---
tags:
  - sistemas-informaticos
  - tema1
  - software
  - sistema-operativo
  - post
  - bios
asignatura: Sistemas informáticos
tema: 1
subtema: Componentes software y arranque
---

# T1 — Componentes software y proceso de arranque

## ¿Qué es el software?

Conjunto de instrucciones que, al ejecutarse, realizan tareas con un fin común. La relación con el hardware es bidireccional: uno depende del otro.

### Flujo de ejecución de un programa

1. El almacén secundario guarda instrucciones y datos
2. Se trasladan a la memoria principal hasta llegar a los **registros de la CPU**
3. La UC ejecuta las instrucciones y genera señales de control al resto del hardware

---

## Tipos de software

| Tipo | Descripción | Ejemplos |
|---|---|---|
| **Software de sistema** | Interfaz entre usuario y hardware; gestiona el equipo | SO, BIOS/UEFI, drivers, firmware, software de virtualización |
| **Software de desarrollo** | Herramientas para crear software | Editores, compiladores, IDE (IntelliJ, Eclipse) |
| **Software de aplicación** | Tareas concretas para el usuario final | Procesadores de texto, navegadores, juegos |

---

## El sistema operativo

El SO es el software más importante de un equipo:

- Actúa de **interfaz** entre el usuario y el hardware
- Gestiona eficazmente los recursos HW y SW
- Facilita la interacción del usuario con la máquina

Ejemplos: Windows, macOS, Android, distribuciones Linux (Ubuntu, Fedora).

---

## Proceso de arranque (POST)

Al pulsar el botón de encendido:

### 1. La fuente de alimentación distribuye voltajes
- 3.3V → componentes electrónicos de baja potencia
- 5V → componentes mecánicos de poca potencia
- 12V → dispositivos con motores

### 2. La BIOS ejecuta el POST (Power On Self Test)

El procesador ejecuta las instrucciones de la **ROM BIOS** para testear:
- Procesador
- Memoria RAM
- Fuente de alimentación
- Placa base

### 3. Señales de error del POST

| Tipo | Descripción |
|---|---|
| **Sonoras** | Pitidos de diferente frecuencia a través del altavoz de la placa base |
| **Visuales** | Displays en la placa base o tarjetas POST que muestran códigos de error |

> [!note] Cada fabricante de BIOS tiene su propio código de pitidos. Consultar siempre la guía del fabricante.

### 4. Inicialización y configuración

1. Se inicia el adaptador gráfico
2. Se testea e inicializa procesador, RAM, almacenamiento secundario...
3. Se muestran mensajes para acceder al **BIOS Setup Utility** o al menú de arranque
4. Se activan buses (SATA, USB) y dispositivos Plug and Play
5. Se resumen los dispositivos detectados y recursos asignados

### 5. Paso del testigo al medio de arranque

Una vez completado el POST, la BIOS le pasa el control al **primer medio de almacenamiento** (configurado en BIOS Setup Utility), que comienza la carga del sistema operativo.

> [!tip] BIOS vs UEFI
> UEFI es la evolución de la BIOS clásica: interfaz gráfica, soporte de discos > 2TB, arranque más rápido.

## Ver también

- [[T1 - Componentes hardware|Componentes hardware]] — BIOS/UEFI y dispositivos testeados
- [[T2 - Arranque, gestores y particiones|Gestores de arranque del SO]] — continúa después del POST
- [[T1 - Máquinas virtuales y VirtualBox|VirtualBox]] — cómo se simula el POST en entorno virtual

---

← Volver a [[_Índice Sistemas informáticos]]
