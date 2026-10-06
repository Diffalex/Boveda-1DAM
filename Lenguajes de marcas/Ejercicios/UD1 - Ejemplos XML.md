---
tags:
  - lenguajes-de-marcas
  - ud1
  - xml
  - ejercicios
  - trabajo
asignatura: Lenguajes de marcas
unidad: UD1
tema: Ejemplos XML resueltos
subtema: Biblioteca y Clínica
---

# UD1 — Ejemplos XML (resueltos)

Ejercicios de la práctica UD1. Ficheros fuente en esta misma carpeta: `Biblioteca.xml` y `Clinica.xml`.

## Ejemplo 1: Biblioteca (`Biblioteca.xml`)

Usa el **atributo `ISBN`** para identificar cada libro (información identificativa → atributo) y **elementos** para el contenido estructurado del libro.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<libros>
    <libro ISBN="9788419743442">
        <autores>
            <autor>RAFAL KOSIK</autor>
        </autores>
        <titulo>Cyberpunk 2077: No hay coincidencias</titulo>
        <editorial>Roca Editorial</editorial>
        <precio>22.70</precio>
        <num_paginas>416</num_paginas>
    </libro>
    <libro ISBN="9788466356169">
        <autores>
            <autor>Albert Camus</autor>
        </autores>
        <titulo>El hombre rebelde</titulo>
        <editorial>Debolsillo</editorial>
        <precio>13.25</precio>
        <num_paginas>384</num_paginas>
    </libro>
</libros>
```

> [!note] ¿Por qué `ISBN` es atributo?
> El ISBN sirve para **identificar/clasificar** cada libro: es un valor simple, único y no repetible. El resto de datos (autores, título, precio…) son **contenido estructurado** → elementos.

## Ejemplo 2: Clínica (`Clinica.xml`)

Todos los datos del paciente se representan como **elementos** (sin atributos), porque son contenido estructurado y jerárquico (dni, dirección, provincia, etc.).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<pacientes>
    <paciente>
        <nombre>Alejandro</nombre>
        <apellidos>Escobar Valero</apellidos>
        <dni>54462437R</dni>
        <direccion>Cmno chozas, 41</direccion>
        <poblacion>Matagorda</poblacion>
        <provincia>Almeria</provincia>
        <codigo_postal>04715</codigo_postal>
        <telefono>688235745</telefono>
        <fecha_nacimiento>23/11/2001</fecha_nacimiento>
    </paciente>
</pacientes>
```

## Supuestos pendientes (sin rellenar)

Los ficheros `Alquileres.xml` (empresa de alquiler de vehículos) y `relaciones.xml` (relaciones/cardinalidades tipo BBDD) quedan como plantillas de práctica **sin resolver**.

## Ver también

- [[UD1 - Atributos en XML|Análisis del uso de atributos en XML]] — teoría de cuándo usar atributos vs elementos
- [[_Índice Lenguajes de marcas]] — índice de la asignatura

---

← Volver a [[_Índice Lenguajes de marcas]]