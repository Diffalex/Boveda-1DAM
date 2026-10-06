---
tags:
  - bases-de-datos
  - ud1
  - ficheros
  - formatos
asignatura: Bases de datos
unidad: UD1
tema: Ficheros y formatos
---

# UD1 — Ficheros y formatos

Los **ficheros** son la forma básica de almacenar información de forma duradera. Cada formato de fichero define cómo se codifican los datos internamente (estructura, cabeceras, compresión, etc.).

## Tabla resumen de formatos

| Formato | Función del fichero | Campos/características más destacados |
|---|---|---|
| **PNG** | Contenedor de datos de imagen | No pierde datos al comprimir · Formato abierto |
| **MP3** | Contenedor de audio | Compresión con pérdida · Alta compatibilidad · Alta eficiencia de almacenamiento |
| **WAV** | Contenedor de audio | Sin compresión · Tamaños mayores · Limitación de tamaño |
| **OGG** | Contenedor de audio | Soporte multicanal · Código abierto · Menor compresión que MP3 |
| **PDF** | Contenedor de información | Multiplataforma · Mantiene la integridad gráfica |

## Estructura interna de cada formato

### PNG (Portable Network Graphic)

Composición en varias capas:

- **Firma PNG** — los primeros 8 bytes (`89 50 4E 47 0D 0A 1A 0A`) que validan el formato y detectan errores de transmisión.
- **IHDR (Cabecera)** — primer fragmento crítico; metadatos básicos: ancho, altura, profundidad de bits y tipo de color.
- **IDAT (Datos de imagen)** — fragmentos con los píxeles comprimidos mediante **DEFLATE** (compresión sin pérdida); puede haber varios para facilitar el streaming.
- **PLTE (Paleta)** — opcional; lista de colores para imágenes indexadas.
- **tRNS (Transparencia)** — niveles de transparencia o color tratado como transparente.
- **IEND (Fin)** — último fragmento, marca el final del archivo.

### MP3 (MPEG-2 Audio Layer III)

- **ID3v2 (al inicio)** — etiqueta de metadatos de tamaño variable: título, artista, álbum, portada (frame `APIC`)… Cabecera de 10 bytes que empieza con `"ID3"`.
- **Tramas de audio (frames)** — el cuerpo del archivo. Cada trama representa 26 ms de audio (1152 muestras en MPEG-1 Layer III), con:
  - **Cabecera de trama (4 bytes)** — palabra de sincronización (`1111 1111 1111`), versión MPEG, capa (III), bitrate, frecuencia de muestreo, modo de canal…
  - **Información lateral** — 9, 17 o 32 bytes según versión y canal.
  - **Datos de audio** — payload comprimido (código Huffman + espectral).
- **ID3v1 (al final, opcional)** — etiqueta fija de 128 bytes con campos de longitud fija: título (30), artista (30), álbum (30), año (4), comentario (30) y género (1 byte).

### WAV (Waveform Audio File Format)

- **RIFF (cabecera raíz, 12 bytes)**:
  - `RIFF` (4 bytes) — identificador del formato.
  - Tamaño total (4 bytes) — tamaño del archivo − 8.
  - `WAVE` (4 bytes) — indica que es un archivo de audio.
- **fmt (cabecera de formato, 24 bytes)** — describe la codificación:
  - `fmt` (4 bytes) — identificador.
  - Tamaño (4 bytes) — 16 para PCM estándar.
  - Formato de audio (2 bytes) — 1 = PCM, 3 = IEEE float, 6 = A-law, 7 = μ-law, 65534 = extensible.
  - Número de canales (2 bytes) — 1 = mono, 2 = estéreo…
  - Frecuencia de muestreo (4 bytes) — 44100, 48000…
  - Tasa de bytes (4 bytes) — `SampleRate × NumChannels × BitsPerSample / 8`.
  - Alineación de bloque (2 bytes) — `NumChannels × BitsPerSample / 8`.
  - Bits por muestra (2 bytes) — 8, 16, 24, 32.
- **data (datos de audio)**:
  - `data` (4 bytes) — identificador.
  - Tamaño (4 bytes) — `NumSamples × NumChannels × BitsPerSample / 8`.
  - Muestras PCM — enteros en complemento a dos (para ≥ 9 bits) o sin signo (8 bits), intercaladas por canal (L, R, L, R…).

### OGG

Soporta varios tipos de contenido:

- **Audio** — normalmente con códec **Vorbis** u **Opus**.
- **Vídeo** — generalmente con códec **Theora**.
- **Texto** — como subtítulos.
- **Metadatos** — información de pista vía **VorbisComments**.

### PDF (Portable Document Format)

Se compone de 4 partes:

1. **Cabecera** — indica la versión del estándar PDF.
2. **Cuerpo** — describe los elementos de cada página (texto, imágenes, gráficos).
3. **Tabla de referencias cruzadas** — ubica los elementos del cuerpo para acceso aleatorio rápido.
4. **Coda (o tráiler)** — indica la posición de la tabla de referencias cruzadas al final del archivo.

## Ver también

- [[UD1 - Almacenamiento de datos y SGBD|Almacenamiento, ficheros y SGBD]] — clasificación de ficheros, accesos y SGBD
- [[UD2 - Modelo Entidad-Relación|Modelo Entidad-Relación]] — siguiente unidad
- [[_Índice Bases de datos]] — índice de la asignatura

---

← Volver a [[_Índice Bases de datos]]