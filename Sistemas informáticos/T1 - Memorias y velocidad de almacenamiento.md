---
tags:
  - sistemas-informaticos
  - tema1
  - hardware
  - memoria
  - almacenamiento
asignatura: Sistemas informáticos
tema: 1
subtema: Memorias y velocidad de almacenamiento
---

# T1 — Memorias y velocidad de almacenamiento

Documento de apoyo sobre memorias (fuente: `Anexos/memorias.pdf` y esquema `Anexos/Esquema_memorias.jpg`). Completa [[T1 - Componentes hardware]].

## Escala de medidas de información

Cada unidad equivale a **1.024** de la anterior (sistema binario en informática):

| Unidad | Abrev. | Equivale a | Ejemplo práctico |
|---|---|---|---|
| Byte | B | 8 bits | Un carácter de texto |
| Kilobyte | KB | 1.024 B | Una página de texto plano |
| Megabyte | MB | 1.024 KB | Una canción MP3 o una foto de baja resolución |
| Gigabyte | GB | 1.024 MB | Película en alta definición o videojuego sencillo |
| Terabyte | TB | 1.024 GB | Almacenamiento de un portátil actual |
| Petabyte | PB | 1.024 TB | Grandes bases de datos (servidores, p. ej. Netflix) |
| Exabyte | EB | 1.024 PB | Parte del tráfico de Internet mundial |
| Zettabyte | ZB | 1.024 EB | Datos que genera la humanidad en un año |
| Yottabyte | YB | 1.024 ZB | Cantidad casi inimaginable hoy en día |

## Escala de velocidad de la memoria RAM

La velocidad de la RAM se mide de dos formas: **frecuencia de reloj efectiva** (MT/s o MHz) y **ancho de banda** (GB/s).

### Frecuencia y transferencias (velocidad de reloj)

Las memorias actuales son tipo **DDR** (*Double Data Rate*): envían el doble de datos por cada ciclo de reloj. Por eso se usa **MT/s** (megatransferencias por segundo), aunque comercialmente se etiquete como MHz.

| Generación | Frecuencia |
|---|---|
| DDR3 (antigua) | ≈ 1.333 MT/s |
| DDR4 (común) | 2.666 – 3.200 MT/s |
| DDR5 (última) | > 5.200 hasta 8.000 MT/s |

### Ancho de banda

Gigabytes de información que entran/salen por segundo:

- DDR4 normal: ~ **25,6 GB/s**
- DDR5 moderna: > **60 GB/s**

## Comparativa de almacenamiento y velocidad

| Medio | Interfaz / conector (tecnología) | Velocidad práctica |
|---|---|---|
| HDD mecánico antiguo | IDE (PATA) · cinta 40/80 pines | 80–100 MB/s (5400 rpm) · 120–160 MB/s (7200 rpm) |
| HDD*/SSD formato 2,5" | SATA I · cable de datos 7 pines | ~150 MB/s |
| | SATA II · cable de datos 7 pines | ~300 MB/s |
| | SATA III · cable de datos 7 pines | ~600 MB/s |
| SSD alto rendimiento | M.2 NVMe (PCIe 3.0) · ranura M.2 (muesca M) | ~3.500 MB/s |
| | M.2 NVMe (PCIe 4.0) | ~7.500 MB/s |
| | M.2 NVMe (PCIe 5.0) | ~14.500 MB/s |

> [!tip] Idea clave
> Los discos mecánicos (HDD) usan las interfaces SATA/IDE en MB/s; los SSD de alto rendimiento usan **M.2 NVMe** sobre PCIe y superan con mucho esas velocidades.

## Ver también

- [[T1 - Componentes hardware]] — teoría de la unidad (CPU, caché, RAM, placa)
- [[T1 - Procesadores y rendimiento|Procesadores y rendimiento]] — velocidad de cómputo y caché
- [[Sistemas informáticos/Ejercicios/UD1 - Conectores y dispositivos|Conectores de la placa base]] — SATA, M.2, RAM en la tabla resuelta
- [[Sistemas informáticos/Ejercicios/UD1 - Arranque y configuración de dispositivos|Arranque y configuración de dispositivos]] — práctica con BIOS/Aida64
- [[_Índice Sistemas informáticos|Índice de Sistemas informáticos]]

---

← Volver a [[_Índice Sistemas informáticos]]