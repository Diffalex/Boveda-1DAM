---
tags:
  - sistemas-informaticos
  - tema2
  - arranque
  - gestor-arranque
  - particiones
asignatura: Sistemas informáticos
tema: 2
subtema: Arranque, gestores y particiones
---

# T2 — Proceso de arranque del SO y gestores de arranque

Después del [[T1 - Componentes software y arranque|POST]], la BIOS le pasa el control al medio de arranque. A partir de ahí, el gestor de arranque del SO toma el relevo.

---

## Esquemas de particiones

Un disco duro se divide en **particiones** (volúmenes lógicos) para organizar los datos.

### Tabla de particiones

| Tipo | Descripción |
|---|---|
| **MBR** (Master Boot Record) | Estándar clásico. Máximo 4 particiones primarias, discos ≤ 2 TB |
| **GPT** (GUID Partition Table) | Estándar moderno. Soporta más de 4 particiones y discos > 2 TB |

### Tipos de partición

| Tipo | Función |
|---|---|
| **Primaria** | Puede contener un SO arrancable |
| **Extendida** | Contiene particiones lógicas (solo en MBR) |
| **Lógica** | Dentro de una partición extendida |

---

## Gestor de arranque de Windows

### Windows Boot Manager (BOOTMGR / Windows Boot Manager)

| Etapa | Descripción |
|---|---|
| **BIOS/UEFI** | Ejecuta el POST y busca el medio de arranque |
| **Windows Boot Manager** | Lee el `BCD` (Boot Configuration Data) y muestra el menú de arranque |
| **Windows Loader** | Carga el kernel de Windows (`winload.exe`) |
| **NTOSKRNL** | El kernel de Windows toma el control → se inicia el sistema |

> [!note] BCD
> El archivo `BCD` almacena la configuración de arranque. Se puede gestionar con `bcdedit` en el símbolo del sistema.

---

## Gestor de arranque de Linux

### GRUB (GRand Unified Bootloader)

| Etapa | Descripción |
|---|---|
| **BIOS/UEFI** | Ejecuta el POST |
| **GRUB Stage 1** | Busca y carga el Stage 2 |
| **GRUB Stage 2** | Muestra el menú de arranque con los kernels disponibles |
| **Carga del kernel** | El kernel de Linux (`vmlinuz`) se carga en memoria junto con el `initrd`/`initramfs` |

### Archivos clave

| Archivo | Función |
|---|---|
| `vmlinuz` | Imagen del kernel de Linux |
| `initrd` / `initramfs` | Sistema de archivos temporal necesario para el arranque |
| `/boot/grub/grub.cfg` | Configuración del menú de arranque |

> [!tip] Inicialización en Linux
> Después de cargar el kernel, se ejecuta el proceso `init` (o `systemd` en distribuciones modernas) que lanza todos los demás servicios del sistema.

---

## Comparación de gestores de arranque

| Característica | Windows Boot Manager | GRUB |
|---|---|---|
| **Configuración** | BCD (`bcdedit`) | `/boot/grub/grub.cfg` |
| **Múltiples SO** | Sí (encadenando con otros gestores) | Sí (nativo) |
| **Menú interactivo** | Limitado | Muy configurable |
| **Reparación** | `bootrec`, `bcdedit` | `grub-install`, `update-grub` |

## Ver también

- [[T1 - Componentes software y arranque|POST]] — proceso previo al gestor de arranque
- [[T2 - Instalación de sistemas operativos|Instalación]] — cómo se configuran las particiones al instalar
- [[T2 - Arquitecturas de sistemas operativos|Arquitecturas de SO]] — qué kernel se carga

---

← Volver a [[_Índice Sistemas informáticos]]
