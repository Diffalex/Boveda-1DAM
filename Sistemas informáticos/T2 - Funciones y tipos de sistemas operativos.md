---
tags:
  - sistemas-informaticos
  - tema2
  - sistemas-operativos
  - funciones
  - tipos
asignatura: Sistemas informáticos
tema: 2
subtema: Funciones y tipos de sistemas operativos
---

# T2 — Funciones y tipos de sistemas operativos

## Funciones del sistema operativo

El SO gestiona el hardware y software del equipo de forma transparente al usuario. Sus funciones principales son:

| Función | Descripción |
|---|---|
| **Gestión de procesos** | Reparte el tiempo del procesador entre los procesos. Planifica la ejecución de tareas, sincronización y asignación a múltiples núcleos |
| **Gestión de memoria** | Planifica la memoria principal, incluyendo la **memoria virtual** (uso del disco como extensión de la RAM) |
| **Gestión de entradas y salidas** | Administra dispositivos E/S (teclado, pantalla, red, discos) |
| **Gestión de almacenamiento secundario** | Controla el acceso a discos duros, SSD, etc. |
| **Gestión de archivos** | Organiza y controla la estructura de archivos en el sistema |
| **Seguridad** | Protege el sistema frente a accesos no autorizados |

> [!note] El SO también consume recursos
> El propio sistema operativo es software y consume recursos (RAM, CPU). Especialmente relevante en sistemas con pocos recursos.

---

## Tipos de sistemas operativos

Se pueden clasificar según distintos criterios:

### a) Por número de procesos concurrentes

| Tipo | Descripción |
|---|---|
| **Monotarea / monoprogramado** | Un usuario solo ejecuta un proceso a la vez (además del SO) |
| **Multitarea / multiprogramado** | Un usuario ejecuta varios procesos simultáneamente |

### b) Por número de usuarios

| Tipo | Descripción |
|---|---|
| **Monousuario** | Un solo usuario accede a todos los recursos |
| **Multiusuario** | Varios usuarios concurrentemente |

> [!tip] Relación multiusuario-multitarea
> Un sistema multiusuario **siempre** es multitarea, ya que trata con procesos de varios usuarios. Pero puede existir un sistema multiusuario y monotarea (varios usuarios, un proceso cada uno).

### c) Por tipo de proceso

| Tipo | Descripción |
|---|---|
| **Tiempo real** | Requiere plazos de ejecución estrictos. Ej: aviónica, instrumentación médica |
| **Interactivo / tiempo compartido** | Orientado a la participación continua del usuario (procesadores de texto, navegadores). Ej: Windows, Ubuntu, macOS |
| **Por lotes (batch)** | Tareas ejecutadas en serie sin intervención del usuario. Ej: facturas agrupadas, producción |

> [!warning] Penalización cruzada
> Si un SO interactivo ejecuta tareas batch, estas sufren penalización en sus tiempos de ejecución (y viceversa).

### d) Por tipo de interfaz

| Tipo | Descripción |
|---|---|
| **Textual** | Comandos escritos en un terminal — mayor potencia, mayor conocimiento requerido |
| **Gráfico (GUI)** | Ventanas, botones e íconos — más intuitivo, pero consume más recursos |

### e) Por modelo de servicio

| Tipo | Descripción |
|---|---|
| **Escritorio / cliente** | Gestiona procesamiento, memoria y E/S de una sola computadora |
| **En red** | Gestiona la red, usuarios y recursos de forma centralizada en un servidor |
| **Distribuido** | Actúan varios computadores de forma transparente al usuario |

> [!note] Arquitectura de red
> Los SO de escritorio pueden estar conectados a una red, pero el usuario es consciente de los accesos externos.

## Ver también

- [[T2 - Arquitecturas de sistemas operativos|Arquitecturas de SO]] — cómo se organizan internamente
- [[T1 - Componentes software y arranque|Componentes software]] — el SO como software de sistema
- [[T2 - Versiones de sistemas operativos|Versiones de SO]] — ejemplos concretos de cada tipo

---

← Volver a [[_Índice Sistemas informáticos]]
