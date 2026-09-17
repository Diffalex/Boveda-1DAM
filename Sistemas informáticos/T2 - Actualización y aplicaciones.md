---
tags:
  - sistemas-informaticos
  - tema2
  - actualizaciones
  - windows-update
  - ubuntu
asignatura: Sistemas informáticos
tema: 2
subtema: Actualización y aplicaciones
---

# T2 — Actualización del SO y gestión de aplicaciones

---

## Actualización del sistema operativo

Mantener el SO actualizado es esencial para la **seguridad**, **rendimiento** y **estabilidad** del sistema.

### Actualizaciones en Windows

Windows descarga e instala actualizaciones de forma predeterminada. Clasificación:

| Tipo | Descripción |
|---|---|
| **Críticas e importantes** | Seguridad, privacidad y estabilidad del sistema |
| **Recomendadas** | Mejoran rendimiento o prestaciones, no son fundamentales |
| **Opcionales** | Drivers de dispositivos y software de Microsoft |

**Service Packs**: paquetes acumulativos de actualizaciones, correcciones y revisiones. Son gratuitos.

**Configuración:** Windows Update → Configuración → Actualización y seguridad

| Opción | Función |
|---|---|
| Descargar automáticamente | Las actualizaciones se descargan sin intervención |
| Pausar actualizaciones | Detiene actualizaciones por un periodo limitado |
| Ver historial | Lista de actualizaciones instaladas (se pueden desinstalar) |
| Opciones avanzadas | Configurar horarios de reinicio fuera de horas activas |

### Actualizaciones en Ubuntu

Ubuntu actualiza tanto el **software del sistema** como las **aplicaciones instaladas**.

**Configuración:** Software y actualizaciones → pestaña "Actualizaciones"

| Tipo | Descripción |
|---|---|
| **De seguridad** | Ubuntu recomienda tenerlas siempre activas |
| **Recomendadas** | Los desarrolladores de paquetes aconsejan activarlas |
| **Sin asistencia técnica** | Paquetes no soportados oficialmente |

Se puede configurar:
- Frecuencia de comprobación (diariamente recomendado)
- Acción al detectar actualizaciones de seguridad (descargar e instalar automáticamente)
- Notificaciones de nuevas versiones de Ubuntu

---

## Gestión de aplicaciones

### Windows: Aplicaciones y características

Ubicación: Configuración → Aplicaciones → Aplicaciones y características

| Función | Descripción |
|---|---|
| Listado de apps | Aparecen todas las aplicaciones instaladas (algunas son nativas y no se pueden desinstalar) |
| **Características de Windows** | Opcionales del SO que se pueden activar/desactivar (por ejemplo: Hyper-V, WSL) |

### Ubuntu: Software de Ubuntu

Ubuntu usa su propia plataforma de gestión de software (Ubuntu Software Center) para:
- Instalar aplicaciones nuevas
- Actualizar las existentes
- Desinstalar software

Se gestiona mediante **gestores de paquetes**:
- `apt` (Advanced Package Tool) — gestión por línea de comandos
- `dpkg` — gestión a nivel bajo

---

## Ver también

- [[T2 - Versiones de sistemas operativos|Versiones de SO]] — qué versiones mantienen soporte
- [[T2 - Arquitecturas de sistemas operativos|Arquitecturas de SO]] — qué kernel gestiona estas actualizaciones
- [[T1 - Componentes software y arranque|Software de sistema]] — el SO como software que se actualiza

---

← Volver a [[_Índice Sistemas informáticos]]
