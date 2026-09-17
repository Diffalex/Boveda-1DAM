---
tags:
  - sistemas-informaticos
  - tema1
  - virtualizacion
  - virtualbox
  - maquinas-virtuales
asignatura: Sistemas informáticos
tema: 1
subtema: Máquinas virtuales y VirtualBox
---

# T1 — Máquinas virtuales y VirtualBox

## ¿Qué es una máquina virtual?

Una **máquina virtual (MV)** es una computadora no real, instalada mediante software que simula su funcionamiento autónomo sobre un sistema físico real.

| Término | Significado |
|---|---|
| **Host / anfitrión** | Sistema informático real donde se instalan las MV |
| **SO host / anfitrión** | Sistema operativo del equipo real |
| **Guest / invitado** | Máquina virtual o SO instalado en ella |

---

## Usos principales de las máquinas virtuales

| Uso | Descripción |
|---|---|
| **Pruebas** | Probar SW y configuraciones sin afectar al equipo real |
| **Portabilidad** | Las MV se pueden trasladar fácilmente entre hosts |
| **Ahorro de costes** | Infinitas MV en un mismo equipo sin coste adicional |
| **Copias de seguridad** | Al ser archivos, se pueden clonar y restaurar fácilmente |
| **Centralización de servicios** | Un equipo alberga varias MV con diferentes servicios |

---

## Software de virtualización: el hipervisor

El software que abstrae los recursos HW del host se llama **hipervisor** o **VMM** (Virtual Machine Monitor).

> [!important] Los recursos HW reales del host determinan el rendimiento de las MV que se ejecuten sobre él.

### Tipos de hipervisores

| Tipo | Descripción |
|---|---|
| **Nativo** | Se ejecuta directamente sobre el hardware |
| **Alojado (hosted)** | Se ejecuta sobre el sistema operativo del host |

### Software de virtualización más conocido

| Software | Características |
|---|---|
| **VMware** | Líder en entornos empresariales |
| **Microsoft Hyper-V** | Integrado en Windows Server, Pro y Enterprise |
| **Oracle VM VirtualBox** | Open source (GPLv2), multiplataforma, ideal para formación |
| **Citrix XenServer** | Versiones gratuita y comercial |
| **QEMU** | Muy usado en entornos Linux |
| **Parallels** | Solución para Macintosh |

---

## Oracle VM VirtualBox

VirtualBox es el software de virtualización que se usa en el módulo.

### Características importantes a evaluar

- **Plataforma**: SO anfitriones y arquitecturas (32/64 bits)
- **SO guest**: qué sistemas se pueden instalar
- **Licencia**: tipo de licencia del software
- **Portabilidad**: exportación e importación de MV
- **Instantáneas**: puntos de restauración (estados de configuración en un momento dado)

### Entorno de VirtualBox

1. **Barra principal**: Archivo | Máquina | Ayuda
2. **Cinta de botones**: Nueva MV, configurar, descartar, iniciar
3. **Panel izquierdo**: listado de máquinas virtuales
4. **Botones de vista**: Herramientas de máquina / Herramientas globales

### Creación de una máquina virtual

Al pulsar **Nueva** se configuran:

| Parámetro | Opciones clave |
|---|---|
| **Nombre y SO** | Nombre representativo, tipo y versión del SO invitado |
| **Tamaño de memoria** | Cantidad de RAM (se resta del host durante la ejecución) |
| **Disco duro virtual** | No agregar / Crear nuevo / Usar existente |

#### Tipos de archivo de disco duro virtual

| Formato | Origen |
|---|---|
| **VDI** | VirtualBox (por defecto) |
| **VHD** | Microsoft |
| **VMDK** | VMware (abierto) |
| **QCOW** | QEMU |

#### Almacenamiento del disco virtual

| Tipo | Descripción |
|---|---|
| **Reservado dinámicamente** | Va ocupando espacio incrementalmente — más flexible |
| **Tamaño fijo** | Reserva todo el espacio desde el inicio — más rápido una vez creado |

### Instantáneas

Las **instantáneas** guardan el estado de una MV en un momento dado, permitiendo restaurarla si algo sale mal. Son especialmente útiles antes de realizar cambios arriesgados en el sistema.

## Ver también

- [[T1 - Arquitectura de un sistema informático|Arquitectura]] — cómo se abstrae el hardware real
- [[T1 - Componentes software y arranque|POST]] — el arranque real vs. el simulado en MV
- [[T2 - Instalación de sistemas operativos|Instalación de SO]] — cómo instalar Ubuntu y Windows en VirtualBox
- [[T2 - Arquitecturas de sistemas operativos|Arquitecturas de SO]] — qué tipo de kernel ejecutan los SO invitados

---

← Volver a [[_Índice Sistemas informáticos]]
