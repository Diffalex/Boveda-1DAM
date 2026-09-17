---
tags:
  - sistemas-informaticos
  - tema2
  - instalacion
  - ubuntu
  - windows
  - virtualbox
asignatura: Sistemas informáticos
tema: 2
subtema: Instalación de sistemas operativos
---

# T2 — Instalación de sistemas operativos

---

## Requisitos mínimos

Antes de instalar un SO hay que comprobar los requisitos del sistema (procesador, RAM, almacenamiento, resolución de pantalla).

| Componente | Ubuntu Desktop | Windows 10 Pro |
|---|---|---|
| **Procesador** | 2 GHz dual-core | 1 GHz o superior |
| **RAM** | 4 GB | 2 GB (64-bit) |
| **Almacenamiento** | 25 GB | 32 GB |
| **Resolución** | 1024×768 | 800×600 |

---

## Planificación de la instalación

1. **Elegir el SO** a instalar
2. **Decidir el tipo de instalación:**
   - **Nativa**: directamente sobre el hardware real
   - **Virtual**: en una [[T1 - Máquinas virtuales y VirtualBox|máquina virtual]] (usando VirtualBox)
3. **Preparar medios de instalación:**
   - Imagen ISO → grabar en USB (con herramientas como Rufus o Etcher)
   - O montar como unidad virtual en MV
4. **Configurar la BIOS/UEFI** para arrancar desde el medio de instalación

---

## Instalación de Ubuntu Desktop en VirtualBox

### Proceso resumido

1. Crear nueva MV en VirtualBox → nombre, tipo Linux/Ubuntu (64-bit)
2. Asignar memoria RAM (mínimo 2 GB, recomendado 4 GB)
3. Crear disco virtual (VDI, reservado dinámicamente, mínimo 25 GB)
4. Montar la imagen ISO de Ubuntu en la unidad óptica virtual
5. Iniciar la MV → se lanza el instalador de Ubuntu
6. Seleccionar idioma, teclado, tipo de instalación
7. Crear usuario y contraseña
8. Esperar a que finalize → el sistema se reinicia

---

## Instalación de Windows 10 Pro en VirtualBox

### Proceso resumido

1. Crear nueva MV → nombre, tipo Windows/Windows 10 (64-bit)
2. Asignar memoria RAM (mínimo 2 GB, recomendado 4 GB)
3. Crear disco virtual (VDI, reservado dinámicamente, mínimo 32 GB)
4. Montar la imagen ISO de Windows 10
5. Iniciar → se lanza el instalador de Windows
6. Seleccionar idioma, versión (Pro), tipo de instalación (personalizada)
7. Particionar el disco virtual (un solo volumen)
8. Esperar a que finalize → se reinicia y configura el sistema

---

## Instalaciones desatendidas

Permiten instalar un SO sin intervención del usuario, mediante archivos de configuración:

| SO | Herramienta de instalación desatendida |
|---|---|
| **Windows 10** | Archivo `Autounattend.xml` (respuesta a preguntas del instalador) |
| **Ubuntu** | Archivo `preseed.cfg` ( Respuestas automáticas al instalador) |

Útil para desplegar varios equipos con la misma configuración sin repetir pasos manualmente.

## Ver también

- [[T1 - Máquinas virtuales y VirtualBox|VirtualBox]] — cómo crear y configurar la MV antes de instalar
- [[T2 - Versiones de sistemas operativos|Versiones de SO]] — qué versiones elegir
- [[T1 - Componentes software y arranque|Arranque]] — qué ocurre después de la instalación
- [[T2 - Arranque, gestores y particiones|Gestores de arranque]] — cómo arranca el SO instalado

---

← Volver a [[_Índice Sistemas informáticos]]
