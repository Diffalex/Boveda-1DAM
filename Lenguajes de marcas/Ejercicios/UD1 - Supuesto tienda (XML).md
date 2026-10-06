---
tags:
  - lenguajes-marcas
  - xml
  - ud1
  - ejercicios
  - plantilla
asignatura: Lenguajes de marcas
unidad: UD1
tema: Supuesto tienda (XML)
---

# UD1 — Supuesto tienda (XML)

Supuesto de modelado de una **tienda informática**. En este ejercicio **no se rellenan datos**: los documentos se entregan **a modo plantilla** (solo la estructura del árbol XML, sin contenido). Fuente: `Anexos/supuesto tienda.txt`.

## Enunciado

Se desea informatizar la gestión de una tienda informática:

- **Productos** de la tienda: código, descripción, precio y número de existencias.
- **Clientes**: código, nombre, apellidos, dirección y teléfono.
- Un cliente puede comprar **varios productos** y un mismo producto puede ser comprado por **varios clientes** (relación N:M). Cada compra queda **registrada con su fecha**.
- **Proveedores** (los que suministran): código, nombre, apellidos, dirección, provincia y teléfono. Un mismo producto puede ser suministrado por **varios proveedores**.

## Estado de las plantillas

| Fichero | Estado |
|---|---|
| `tienda.xml` | ✔ Estructura a modo plantilla, bien formada (corregida) |
| `curriculum.xml` | ✔ Estructura completa a modo plantilla |

> [!warning] Instrucción de clase: modo plantilla
> En estas actividades **no hay que rellenar los datos**; se pide dejar la estructura (`<elemento></elemento>`) vacía. El objetivo es que el árbol XML esté **bien formado** y refleje las entidades y relaciones del supuesto.

### `tienda.xml` (corregida)

La versión original del alumno solo tenía `<tienda>` con un `<` suelto y no estaba bien formada. Se ha corregido con la estructura del supuesto:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<tienda>
    <productos>
        <producto>
            <codigo></codigo>
            <descripcion></descripcion>
            <precio></precio>
            <existencias></existencias>
        </producto>
    </productos>

    <clientes>
        <cliente>
            <codigo></codigo>
            <nombre></nombre>
            <apellidos></apellidos>
            <direccion></direccion>
            <telefono></telefono>
        </cliente>
    </clientes>

    <compras>
        <compra>
            <codigo_cliente></codigo_cliente>
            <codigo_producto></codigo_producto>
            <fecha></fecha>
        </compra>
    </compras>

    <proveedores>
        <proveedor>
            <codigo></codigo>
            <nombre></nombre>
            <apellidos></apellidos>
            <direccion></direccion>
            <provincia></provincia>
            <telefono></telefono>
        </proveedor>
    </proveedores>
</tienda>
```

La entidad `compra` registra la relación N:M **clientes ↔ productos** con la fecha; `proveedores` queda como entidad independiente (un producto puede tener varios suministradores).

### `curriculum.xml`

Plantilla de currículum vitae en XML (datos de persona, contacto, competencias, formación y experiencia) ya estructurada y bien formada.

## Ver también

- [[Lenguajes de marcas/Ejercicios/UD1 - Ejemplos XML|Ejemplos XML]] — ficheros resueltos (Biblioteca y Clínica)
- [[Lenguajes de marcas/UD1 - Atributos en XML|Atributos en XML]] — teoría de atributos vs elementos
- [[Lenguajes de marcas/Ejercicios/UD1 - Actividad presencial 3 (agencia de turismo)|Actividad presencial 3 (agencia de turismo)]] — otro supuesto pendiente a modo plantilla
- [[_Índice Lenguajes de marcas|Índice de Lenguajes de marcas]]

---

← Volver a [[_Índice Lenguajes de marcas]]