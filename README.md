# Bóveda 1DAM — Apuntes de 1º de DAM

Colección de apuntes de clase de **1º de Desarrollo de Aplicaciones Multiplataforma (DAM)**, escrita en **Markdown** y enlazada con *wikilinks* de Obsidian (`[[…]]`). El contenido se edita desde Obsidian y se comparte con la clase a través de este repositorio.

La bóveda también se publica como web estática en:

**https://diffalex.github.io/Boveda-1DAM/**

## Contenido

Apuntes de las asignaturas del curso:

- **Programación** (Java): UD1 completa, UD2 (condicionales, `switch` y bucles) y UD3 (POO: clases, objetos, métodos, fechas y excepciones).
- **Sistemas informáticos**: T1 (fundamentos y máquinas virtuales) y T2 (sistemas operativos) con ejercicios y test resueltos.
- **Bases de datos**: UD1 (ficheros y SGBD), UD2 (modelo Entidad-Relación), UD3 (paso a tablas y normalización) y UD4 (SQL/DDL).
- **Lenguajes de marcas**: UD1 (XML, atributos, DTD, ejercicios y supuestos de agenda/recetas).
- **Entornos de desarrollo**: UD1.
- **Sostenibilidad** y **Prevención de riesgos laborales**: UD1 de cada módulo.
- **Digitalización**: pendiente de contenido.

## Estructura

Cada asignatura es una carpeta con una nota por tema o unidad, un índice `_Índice <Asignatura>.md` y (cuando existe) subcarpetas `Ejercicios/` y `Anexos/`.

```
Boveda Dam/
├── README.md
├── 00 - General/               hub y guías transversales
├── Bases de datos/
├── Digitalización/
├── Entornos de desarrollo/
├── Lenguajes de marcas/
├── Prevención de riesgos laborales/
├── Programación/
├── Sistemas informáticos/
└── Sostenibilidad/
```

El **punto de entrada recomendado** es `00 - General/Asignaturas 1 DAM.md`, que enlaza los índices de todas las asignaturas.

## Cómo usar

1. Clona el repositorio.
2. Abre la carpeta como bóveda en **Obsidian**.
3. La guía de colaboración está en `00 - General/GUIA_CLASE.md`.

## Web pública

El sitio estático se genera con `web/build_web.py`, un script de **Python sin dependencias** (solo biblioteca estándar). Cada *push* a `main` ejecuta el workflow `.github/workflows/pages.yml`, que regenera la web y la publica en **GitHub Pages** automáticamente. El HTML generado no se almacena en el repositorio.