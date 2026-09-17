---
tags:
  - sistemas-informaticos
  - tema2
  - arquitecturas
  - kernel
  - monolitico
  - microkernel
asignatura: Sistemas informáticos
tema: 2
subtema: Arquitecturas de sistemas operativos
---

# T2 — Arquitecturas de los sistemas operativos

La arquitectura del SO ha evolucionado junto con el hardware. Existen varias tipologías, cada una con ventajas e inconvenientes.

---

## Estructura genérica de un SO

```
┌──────────────────────────────────┐
│           Usuario                │
├──────────────────────────────────┤
│  Interfaz  │  Programas usuario  │
├──────────────────────────────────┤
│         Servicios del SO         │
│  (gestión de procesos, E/S, etc) │
├──────────────────────────────────┤
│          Núcleo (kernel)         │
│  HAL - Hardware Abstraction Layer │
├──────────────────────────────────┤
│           Hardware               │
└──────────────────────────────────┘
```

---

## Tipos de arquitecturas

### 1. Sistemas con capas o anillos

Estructura **jerárquica** en niveles. Cada capa solo puede acceder a la inferior.

| Componente | Función |
|---|---|
| **Núcleo (kernel)** | Interactúa directamente con el hardware (HAL) |
| **Servicios** | Gestión de procesos, E/S y memoria — da soporte a la capa superior |
| **Interfaz** | Shell o interfaz gráfica + programas de usuario |

**Ejemplos:** THE, MULTICS (ambos de los años 60-70)

### 2. Sistemas monolíticos

Toda la funcionalidad del SO se ejecuta en un **único espacio de direcciones** en modo supervisor.

| Ventajas | Inconvenientes |
|---|---|
| Rendimiento (todas las rutinas en modo supervisor) | Difícil evolución y resolución de errores |
| | Baja estabilidad |

**Ejemplo:** Ubuntu Linux

### 3. Microkernel

El núcleo se reduce al mínimo indispensable:

| En modo núcleo (kernel) | En modo usuario |
|---|---|
| Gestión de memoria | Gestión de archivos |
| Gestión prioritaria de procesos e hilos | Protocolos de comunicación |
| Comunicación básica entre procesos | Drivers de dispositivos |

El micronúcleo gestiona la comunicación entre **clientes** (apps de usuario) y **servidores** (módulos del SO), ambos ejecutándose en modo usuario.

| Ventajas | Inconvenientes |
|---|---|
| Mayor seguridad (la mayoría en modo usuario) | Sobrecarga de comunicación → menor rendimiento |
| Mayor estabilidad | |
| Fácil actualización | |

**Ejemplo:** MINIX

### 4. Kernel híbrido

Combina diseño **microkernel** con implementación **monolítica**:

- Mantiene parte de los servicios como módulos en modo supervisor (a diferencia del microkernel puro)
- Combina estabilidad del microkernel con el rendimiento del monolítico

| Ventajas | Inconvenientes |
|---|---|
| Gran estabilidad y alto rendimiento | Complejidad en diseño |

---

## SO actuales y sus arquitecturas

| SO | Arquitectura |
|---|---|
| **Ubuntu Linux** | Monolítico |
| **Windows (familia NT)** | Híbrido |
| **macOS** | Híbrido |

## Ver también

- [[T2 - Funciones y tipos de sistemas operativos|Tipos de SO]] — clasificación por funciones
- [[T1 - Componentes software y arranque|POST]] — proceso de arranque previo a la carga del kernel
- [[T2 - Versiones de sistemas operativos|Versiones de SO]] — ejemplos concretos de cada arquitectura

---

← Volver a [[_Índice Sistemas informáticos]]
