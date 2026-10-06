# Bóveda 1DAM — README de contexto

> **Ruta:** `/home/alex/Escritorio/Boveda Dam`
> **Tipo:** Bóveda de **Obsidian** con apuntes de 1º de DAM (Desarrollo de Aplicaciones Multiplataforma)
> **Última actualización del contexto:** 2026-10-06
>
> Este archivo resume **toda la estructura y convenciones de la bóveda** para poder responder consultas leyendo solo este README. Mantenlo actualizado cuando cambie la estructura.

---

## 1. Propósito

Colección de apuntes de clase de **1º DAM**, escritos en **Markdown** y enlazados entre sí con wikilinks de Obsidian (`[[...]]`). Se comparte con la clase vía **GitHub** y se edita desde Obsidian (plugin *Obsidian Git*).

## 2. Repositorio y git

- **Remote:** `https://github.com/Diffalex/Boveda-1DAM.git` (origin)
- **Rama:** `main`
- **Historial reciente:**
  - `890c620 Añadir notas sobre el modelo de Von Neumann`
  - `9b221b3 Guía de clase + instalación de Obsidian para compañeros`
  - `23511b1 Apuntes 1 DAM - primera version`
- **`.gitignore`:** `.obsidian/workspace.json`, `.obsidian/workspace-mobile.json`, `.obsidian/cache`, `.trash/`, `.DS_Store`
- **Convenio de trabajo:** no se hace `git add`/`commit`/`push` salvo que el usuario lo pida explícitamente.

## 3. Estructura general

La bóveda es una carpeta por **asignatura**. Dentro, un archivo `.md` por tema/unidad, un índice `_Índice <Nombre>.md`, y subcarpetas auxiliares `Ejercicios/` (prácticas y trabajos resueltos) y `Anexos/` (PDFs/docx fuente) cuando existen.

```
Boveda Dam/                      ← raíz de la bóveda
├── README.md                    ← este archivo (contexto)
├── 00 - General/                ← hub y guías transversales
│   ├── Asignaturas 1 DAM.md     ← hub central: enlaza los índices de todas las asignaturas
│   └── GUIA_CLASE.md            ← guía de colaboración (clonar, Obsidian Git, atajos)
├── Bases de datos/              ← UD1 y UD2 (ficheros, SGBD, E-R)
├── Digitalización/              ← ⚠️ PENDIENTE de contenido
├── Entornos de desarrollo/      ← UD1 (cuestiones previas + actividades)
├── Lenguajes de marcas/         ← UD1 (atributos XML + actividad presencial + supuesto tienda)
├── Prevención de riesgos laborales/ ← PRL: conceptos básicos (nuevo)
├── Programación/                ← UD1 completa + ejercicios + UD2 (condicionales, switch y bucles)
├── Sistemas informáticos/       ← T1 y T2 completos + ejercicios + evaluación
└── Sostenibilidad/              ← UD1: desarrollo sostenible y Agenda 2030 (nuevo)
```

### Punto de entrada recomendado

`00 - General/Asignaturas 1 DAM.md` → enlaza cada `_Índice <Asignatura>.md`. Cada índice lista las notas de la asignatura, sus unidades/temas y los ejercicios.

---

## 4. Detalle por asignatura

### 4.1 Programación
Prefijo: `UD` (unidades). UD1 — "Introducción a la programación" (Java).

| Nota | Contenido |
|---|---|
| `_Índice Programación.md` | Índice de la asignatura: UD1 completa + UD2 (condicional, switch y bucles) + unidades pendientes (UD3 expresiones/operadores, UD4 métodos y clases, UD5 arrays) |
| `UD1 - Nomenclatura de identificadores.md` | Reglas obligatorias y convenios de nombres en Java (`camelCase`, `PascalCase`, constantes). Fuente complementaria en `Anexos/` (*Java_Reglas_vs_Convenios_Identificadores.pdf*) |
| `UD1 - Estructura de un programa Java.md` | Plantilla estándar de un programa Java (imports, variables, entrada, procesamiento, salida) |
| `UD1 - Comentarios y salida por consola.md` | Comentarios `//` · `/* */`, `System.out.println()` y `print()` |
| `UD1 - Entrada de datos con Scanner.md` | Clase `Scanner`: `nextInt()`, `nextDouble()`, `next()`, `nextLine()`; errores comunes y cierre con `close()` (Anexo V) |
| `UD1 - Tipos de datos primitivos.md` | Los 8 primitivos, sufijos (`3.14f`), tipos por defecto, no comparar `float`/`double` con `==`. Fuente: `Anexos/Anexo III.Java_Tipos_Primitivos.pdf` |
| `UD1 - JDK, JRE y JVM.md` | Esquema JDK (javac, javadoc, jar, debugger) ⊃ JRE (JVM + bibliotecas estándar) ⊃ JVM. Fuente: `Anexos/Esquema JDK.pdf` |
| `UD2 - Estructura condicional (if-else).md` | Teoría `if/else if/else`, operadores de comparación y lógicos, módulo `%`, bloques y ámbito. (nueva) |
| `UD2 - Bucles (while, do-while, for).md` | Teoría de bucles: `while`, `do-while` (entrada "modo cabezón"), `for`, bucles anidados, `break` y cuándo usar cada uno. (nueva) |
| `UD2 - Selección múltiple (switch).md` | Teoría de `switch`/`case`/`default`, `switch` anidado, validación de rangos y comparativa con `else if`. (nueva) |
| `Ejercicios/UD1 - Ejemplos java.md` | Código de clase (`prog-ud1`): HolaMundo, EstructuraPrograma, Calculoiva, Operadores y DatosPrimitivos, OperadoresLogicos, Conversiones (casting) y Ejercicio1/Ejercicio2 (Scanner) — 9 ejemplos |
| `Ejercicios/UD1 - Soluciones de práctica.md` | Los **19 ejercicios de práctica resueltos** (proyecto `prog-ud1`), con el código completo de cada uno (nueva) |
| `Ejercicios/UD1 - Enunciados de práctica.md` | Checklist de los **19 enunciados, todos resueltos** y enlazados a sus soluciones |
| `Ejercicios/UD2 - Ejemplos if-else.md` | Programas de clase de `prog-ud2` (ParImpar, MayorEdad, nota→calificación, día laborable/festivo, positivo/negativo, mayor de dos); `EjercicioClase8` incompleto (pendiente) (nueva) |
| `Ejercicios/UD2 - Ejemplos bucles y switch.md` | Programas de `prog-ud2` con bucles y `switch`: `EjercicioWhile`, `EjercicioResueltoFor` (tabla del 7), `Multiplicaciones`, `Asteriscos` (for anidado), `EstacionMes` (switch anidado); `EjercicioBucles1` incompleto (pendiente). (nueva) |

**Fuentes en el equipo:** `/home/alex/Escritorio/1 DAM/Programacion/Unidad 1/` (PDFs de la Unidad 1, proyectos IntelliJ `prog-ud1/src/*.java`, `prog-ud2/src/*.java`).

### 4.2 Sistemas informáticos
Prefijo: `T` (temas). T1 — Fundamentos de los sistemas informáticos y máquinas virtuales. T2 — Sistemas operativos: introducción.

| Nota | Contenido |
|---|---|
| `_Índice Sistemas informáticos.md` | Índice: T1 y T2 completos + ejercicios + evaluación + pendientes (T3 archivos/almacenamiento, T4 usuarios y procesos, T5 redes, T6 seguridad, T7 ofimática) |
| `T1 - Arquitectura de un sistema informático.md` | Arquitectura e introducción a un sistema informático |
| `T1 - Modelo de Von Neumann.md` | Modelo de Von Neumann (teoría completa) |
| `T1 - Componentes hardware.md` | CPU, caché (L1/L2/L3), RAM, placa base |
| `T1 - Memorias y velocidad de almacenamiento.md` | Escala de medidas (B→YB), velocidad RAM (MT/s, DDR3/4/5), ancho de banda y comparativa HDD/SATA/M.2 NVMe. Fuentes: `Anexos/memorias.pdf`, `Anexos/Esquema_memorias.jpg` (nueva) |
| `T1 - Procesadores y rendimiento.md` | Núcleos e IPC, rendimiento teórico y real, caché (hit/miss), frecuencia, tiempo de ejecución y escala MHz/GHz. Fuente: `Anexos/problemas_procesadores.pdf` (nueva) |
| `T1 - Componentes software y arranque.md` | Software, sistema operativo, proceso de arranque (POST, BIOS) |
| `T1 - Máquinas virtuales y VirtualBox.md` | Virtualización y VirtualBox |
| `T2 - Funciones y tipos de sistemas operativos.md` | Funciones y tipos de SO |
| `T2 - Arquitecturas de sistemas operativos.md` | Arquitecturas de SO (kernel monolítico, microkernel) |
| `T2 - Versiones de sistemas operativos.md` | Windows, Linux (Ubuntu, Mint, Debian, Fedora, CentOS/RHEL), macOS |
| `T2 - Instalación de sistemas operativos.md` | Instalación de SO (Ubuntu/Windows en VirtualBox) |
| `T2 - Arranque, gestores y particiones.md` | Proceso de arranque, gestores de arranque, particiones |
| `T2 - Actualización y aplicaciones.md` | Actualización (Windows Update) y gestión de aplicaciones |
| `Ejercicios/T1 - Preguntas y respuestas Von Neumann.md` | **Ejercicio/trabajo del tema 1** (Von Neumann): 10 preguntas desarrolladas, diagrama ASCII, comparativa con Harvard, bibliografía. Fuentes resueltas en `Anexos/` (*SI_VonNeumann*, *Escobar…VonNeumann.pdf*) |
| `Ejercicios/Cuestionario de conocimientos previos.md` | **Test resuelto** de 20 preguntas (SO, particiones, DNS, IP, RAID, sistemas de archivos, MV, LAN, firewall…). Fuente resuelta en `Anexos/` |
| `Ejercicios/UD1 - Conectores y dispositivos.md` | **Tabla resuelta** de conectores de la placa base (IDE, SATA, M.2, socket LGA1366, PCIe, RAM DDR5, PS/2, VGA, HDMI, USB… → elemento a conectar → cable → utilidad). Fuente en `Anexos/` (nueva) |
| `Ejercicios/T1 - Problemas de procesadores.md` | **3 problemas de rendimiento pendientes** (M1: 6 núcleos/3 GHz/IPC 1,5; M2: 12 núcleos/2 GHz; ejecución de un programa de 3·10⁹ instrucciones). Fuente: `Anexos/problemas_procesadores.pdf` (nueva) |
| `Ejercicios/UD1 - Arranque y configuración de dispositivos.md` | **Práctica pendiente** en 4 bloques: interior del PC y placa (pila/chipset), arranque/BiOS (temperatura, RAM, orden de arranque) + Aida64, configuración USB/controladores, impresora Microsoft Print to PDF. Fuente: `Anexos/UD1_Arranque_Configuracion_Dispositivos.docx` (nueva) |
| `_Programación didáctica SI.md` | Datos de evaluación del módulo: RA1 en UD1-2, fase dual 12/04→04/06/2027, media ponderada de RA, pérdida de continua a los 33 días |

**Nota sobre duplicados:** en el curso hay versiones resueltas y sin rellenar. Los anexos (`.docx`/`.pdf`) copiados son siempre las **versiones rellenas**; los enunciados sin resolver no se copian.

### 4.3 Bases de datos
Prefijo: `UD`. UD1 (ficheros, almacenamiento y SGBD) y UD2 (modelo E-R) iniciadas.

| Nota | Contenido |
|---|---|
| `_Índice Bases de datos.md` | Índice: UD1 y UD2 completadas + unidades previstas (UD3 E/R→tablas y normalización, UD4 SQL, UD5 administración) |
| `UD1 - Ficheros y formatos.md` | Formatos de fichero (PNG, MP3, WAV, OGG, PDF): función, campos característicos y estructura interna. Fuente resuelta en `Anexos/` (*trabajo Ficheros*) |
| `UD1 - Almacenamiento de datos y SGBD.md` | Datos/información, memoria y almacenamiento, ficheros (tipos, accesos, índices), bases de datos, SGBD, Big Data/BI y normativa de protección de datos. Fuente: `Anexos/tema1-main.zip` (nueva) |
| `UD2 - Modelo Entidad-Relación.md` | Modelado (conceptual/lógico/físico), diagramas E/R y notaciones, entidades fuertes/débiles, atributos y claves, cardinalidad, participación, E/R extendido y ejercicios. Fuente: `Anexos/tema2-main.zip` (nueva) |

### 4.4 Entornos de desarrollo — UD1 iniciada

| Nota | Contenido |
|---|---|
| `_Índice Entornos de desarrollo.md` | Índice de la asignatura |
| `UD1 - Cuestiones previas.md` | Cuestionario inicial: perfil del alumno (CFGM Sistemas, motivación, áreas de interés). Fuente en `Anexos/` (*CuestionesPrevias.pdf*) |
| `Ejercicios/UD1 - ED01 Actividades.md` | **Cuestionario ED01 pendiente** (software, ciclo de vida, modelos ágiles/SCRUM/Kanban/XP, lenguajes de programación), en 3 bloques con checklist (nueva) |

### 4.5 Lenguajes de marcas — UD1 iniciada

| Nota | Contenido |
|---|---|
| `_Índice Lenguajes de marcas.md` | Índice: UD1 (XML) iniciada + unidades previstas (UD2 HTML/CSS, UD3…) |
| `UD1 - Atributos en XML.md` | Teoría: cuándo usar atributos vs elementos, comparativa, ejemplos correctos/incorrectos. Fuente: `Anexos/Analisis_Uso_de_Atributos_en_XML.pdf` |
| `Ejercicios/UD1 - Ejemplos XML.md` | Ejemplos **resueltos** (Biblioteca.xml con atributo `ISBN` y Clínica.xml solo con elementos); los ficheros XML están en la carpeta. `Alquileres.xml` y `relaciones.xml` son supuestos **sin rellenar** (práctica pendiente) |
| `Ejercicios/UD1 - Actividad presencial 3 (agencia de turismo).md` | **Actividad presencial 3 pendiente**: crear `agencia_turismo.xml` (propietarios y casas rurales). Fuente: `Anexos/agencia_turismo.pdf`. Plantillas vacías: `agencia_turismp.xml` e `instituto.xml` (nueva) |
| `Ejercicios/UD1 - Supuesto tienda (XML).md` | Supuesto de tienda informática **a modo plantilla** (sin datos): `tienda.xml` (corregida: productos, clientes, compras con fecha, proveedores) y `curriculum.xml`. Fuente: `Anexos/supuesto tienda.txt` (nueva) |

### 4.6 Prevención de riesgos laborales — nueva (módulo transversal)

| Nota | Contenido |
|---|---|
| `_Índice Prevención de riesgos laborales.md` | Índice de la asignatura |
| `UD1 - Conceptos básicos de PRL.md` | RA-2 Seguridad y salud laboral: salud, daños, factores de riesgo, medidas de prevención/protección, riesgo eléctrico/incendio, agentes físicos/químicos/biológicos. Fuente (no en bóveda): presentación `IPE 1 LA PREVENCION DE RIESGOS...pptx` (nueva) |

### 4.7 Sostenibilidad — nueva (módulo transversal)

| Nota | Contenido |
|---|---|
| `_Índice Sostenibilidad.md` | Índice de la asignatura |
| `UD1 - Desarrollo sostenible y Agenda 2030.md` | Contexto histórico, sistema productivo y globalización, huella ecológica, desarrollo sostenible, marcos internacionales y ODS. Fuente (no en bóveda): presentación `Presentacion aula Unidad 1 ok (2).ppsx` (nueva) |

### 4.8 Digitalización — ⚠️ PENDIENTE
- Solo `_Índice Digitalización.md` (estado: pendiente).

---

## 5. Convenciones de las notas

1. **Carpeta por asignatura**, un `.md` por tema/unidad, prefijo de orden: `UD1 -`, `T1 -`, `T2 -`, etc.
2. **Frontmatter YAML** al inicio de cada nota con `tags` (lista), `asignatura`, y campos opcionales `unidad`, `tema`, `subtema` (o `tipo`). Ejemplo:

```yaml
---
tags:
  - sistemas-informaticos
  - tema1
  - arquitectura
  - von-neumann
asignatura: Sistemas informáticos
tema: 1
subtema: Modelo de Von Neumann
---
```

3. **Índices** llamados `_Índice <Nombre>.md` enlazan todas las notas de la asignatura con la barra `_` inicial (para que aparezcan primero en orden alfabético).
4. **Enlaces entre notas** únicamente con wikilinks `[[Nombre de la nota]]` o `[[Nombre|Texto visible]]`. Se resuelven **por nombre de nota**, así que mover ficheros de carpeta **no rompe los enlaces** (aunque en los índices se usa ruta completa `[[Carpeta/Nota|Texto]]` cuando hay notas con nombres repetidos).
5. **Footer** obligatorio al final de cada nota: `← Volver a [[_Índice <Asignatura>]]`.
6. **Callouts** de Obsidian: `> [!note]`, `> [!tip]`, `> [!important]`, `> [!warning]`.
7. Sección **"Ver también"** al final con wikilinks a notas relacionadas.
8. **Tablas** para comparativas, solucionarios y datos estructurados.
9. **Bloques de código** con fence (```` ```java ````, ```` ```xml ````, ``text``, `bash`…) para ejemplos.
10. **Subcarpeta `Ejercicios/`**: prácticas, trabajos y tests **resueltos** (tags `ejercicios`, `trabajo`, `preguntas`, `test`).
11. **Subcarpeta `Anexos/`**: PDFs/docx fuente de las notas. **Solo versiones resueltas/rellenas.** ⚠️ **NO se añaden presentaciones (`.ppsx`/`.pptx`)**: pesan mucho; se citan como fuente externa con su ruta y no se copian.
12. **Notas de referencia/transversales** con `_` inicial (p. ej. `_Programación didáctica SI.md`).

## 6. Taxonomía de tags

- **Por asignatura:** `asignatura` (genérico de índices), `sistemas-informaticos`, `programacion`, `bases-de-datos`, `digitalizacion`, `entornos-de-desarrollo`, `lenguajes-de-marcas`, `sostenibilidad`, `prevencion-riesgos`.
- **Por unidad/tema:** `tema1`, `tema2`, `ud1`.
- **Generales/hub:** `hub`, `general`, `guia`, `colaboracion`, `plantilla`, `evaluacion`, `programacion-didactica`.
- **Sistemas informáticos:** arquitectura, arquitecturas, von-neumann, cpu, hardware, memoria, placa-base, bios, post, software, sistema-operativo, sistemas-operativos, kernel, monolitico, microkernel, funciones, tipos, instalacion, arranque, gestor-arranque, particiones, actualizaciones, windows-update, ubuntu, windows, linux, macos, virtualizacion, virtualbox, maquinas-virtuales, conectores.
- **Programación:** java, identificadores, comentarios, consola, scanner, entrada-datos, tipos-datos, tipos, estructuras-control, condicionales, bucles, switch.
- **Bases de datos:** ficheros, formatos, almacenamiento, sgbd, entidad-relacion, modelado.
- **Lenguajes de marcas:** xml, atributos.
- **Entornos de desarrollo:** cuestiones-previas, actividades.
- **Sostenibilidad:** desarrollo-sostenible, agenda-2030.
- **Prevención de riesgos laborales:** salud-laboral.
- **Ejercicios/practicas:** ejercicios, trabajo, preguntas, test, resuelto.

## 7. Observaciones operativas

- **No leer todos los archivos innecesariamente:** con este README + el índice de la asignatura concreta suele bastar.
- **Mover/renombrar notas es seguro** para los wikilinks (se resuelven por nombre), pero conviene actualizar el índice correspondiente.
- Los adjuntos se copian a `Anexos/` (solo versiones rellenas) para que la bóveda no dependa de rutas externas.
- **Fuentes del curso** (fuera de la bóveda) en `/home/alex/Escritorio/1 DAM/` por asignatura: PDFs de documentación, libros (`Sistemas_Informaticos*.pdf`), proyectos IntelliJ y trabajos entregados.
- Asignatura totalmente pendiente: **Digitalización**.

## 8. Cambios recientes (para detectar desincronización del README)

- Añadido contenido a **Bases de datos**, **Entornos de desarrollo** y **Lenguajes de marcas** (antes vacías).
- Añadidos **Ejercicios/** y **Anexos/** a Programación y Sistemas informáticos.
- Creadas notas de ejercicio/test resueltos y notas de evaluación del módulo.
- **Programación:** ampliada la nota de ejemplos con `DatosPrimitivos.java` y `OperadoresLogicos.java`.
- **Programación (2ª pasada):** nueva nota `UD1 - JDK, JRE y JVM.md` (Esquema JDK.pdf a Anexos), ejemplos nuevos `Conversiones`, `Ejercicio1`, `Ejercicio2`, y nueva nota `Enunciados de práctica.md` (17 ejercicios pendientes).
- **Programación (3ª pasada):** los 19 ejercicios resueltos → nueva nota `Soluciones de práctica.md` (todo el código) y el checklist de enunciados pasa a "resueltos"; nota Scanner ampliada con `close()` (Anexo V); nueva unidad **UD2 Estructura condicional** (`UD2 - Estructura condicional (if-else).md` + `Ejercicios/UD2 - Ejemplos if-else.md`, proyecto `prog-ud2`).
- **Lenguajes de marcas:** nueva `Ejercicios/UD1 - Actividad presencial 3 (agencia de turismo).md` (pendiente) + `Anexos/agencia_turismo.pdf`.
- **Bases de datos:** extraídos `tema1-main.zip` y `tema2-main.zip` → nueva `UD1 - Almacenamiento de datos y SGBD.md` y nueva `UD2 - Modelo Entidad-Relación.md` (zips también como fuente en `Anexos/`).
- **Entornos de desarrollo:** nueva `Ejercicios/UD1 - ED01 Actividades.md` (cuestionario pendiente).
- **Sistemas informáticos:** nueva `Ejercicios/UD1 - Conectores y dispositivos.md` (tabla resuelta) + docx a `Anexos/`.
- **Módulos nuevos:** creadas **Sostenibilidad/** (`UD1 - Desarrollo sostenible y Agenda 2030.md`) y **Prevención de riesgos laborales/** (`UD1 - Conceptos básicos de PRL.md`), con sus presentaciones en `Anexos/` e índices.
- **Programación (4ª pasada):** ampliada UD2 con bucles y `switch` → nuevas notas `UD2 - Bucles (while, do-while, for).md` y `UD2 - Selección múltiple (switch).md` + `Ejercicios/UD2 - Ejemplos bucles y switch.md` (5 programas resueltos; `EjercicioBucles1` pendiente).
- **Lenguajes de marcas:** corregido `tienda.xml` (estaba mal formado) → nueva `Ejercicios/UD1 - Supuesto tienda (XML).md` **a modo plantilla** (sin datos: `tienda.xml`, `curriculum.xml`) + `Anexos/supuesto tienda.txt`.
- **Sistemas informáticos:** nuevas `T1 - Memorias y velocidad de almacenamiento.md` y `T1 - Procesadores y rendimiento.md` + `Ejercicios/T1 - Problemas de procesadores.md` y `Ejercicios/UD1 - Arranque y configuración de dispositivos.md` (ambos pendientes); 4 fuentes nuevas en `Anexos/` (`memorias.pdf`, `problemas_procesadores.pdf`, `Esquema_memorias.jpg`, `UD1_Arranque_Configuracion_Dispositivos.docx`).
- **Convención de `Anexos/`:** ya no se añaden presentaciones (`.ppsx`/`.pptx`). Eliminadas `Sostenibilidad/Anexos/Presentacion aula Unidad 1 ok (2).ppsx` y `Prevención de riesgos laborales/Anexos/IPE 1 ... .pptx` (se citan como fuente externa).
- **Web pública:** cada vez que se suba contenido a este repo (`git push` a `main`) hay que **regenerar y actualizar la web** en la rama `gh-pages` (Fase 3 del plan): `python3 web/build_web.py` y `git push origin gh-pages`. La web se genera con **cero dependencias** (Python estándar) y NO se commitea el HTML en `main` (solo el script `web/build_web.py`).
- Si ves algo nuevo en la bóveda que no está reflejado aquí, actualiza este README.