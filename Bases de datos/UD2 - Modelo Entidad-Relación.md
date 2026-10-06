---
tags:
  - bases-de-datos
  - ud2
  - entidad-relacion
  - modelado
asignatura: Bases de datos
unidad: UD2
tema: Modelo Entidad-Relación
---

# UD2 — Modelo Entidad-Relación (E/R)

Fuente: material `tema2-main.zip` (`Bases de datos/Anexos/`). Tema: interpretación de diagramas E/R y modelado conceptual.

La **conversión de diagramas E/R a tablas** y la **normalización** se tratan en [[UD3 - Paso a tablas y normalización]].

## Modelado de datos

El modelado de datos es el proceso de diseño y representación de la estructura de una base de datos: identificar entidades, sus atributos y las relaciones entre ellas.

| Nivel | Qué define |
|---|---|
| **Conceptual** | Entidades y sus relaciones (modelo abstracto de la realidad) |
| **Lógico** | Tablas, atributos, claves primarias y foráneas, relaciones entre tablas |
| **Físico** | Implementación en el SGBD: almacenamiento, indexación, rendimiento |

Los diagramas E/R corresponden al **nivel conceptual**.

## Diagramas E/R

Representan gráficamente entidades, atributos y relaciones. Herramientas y notaciones:

- **Notación de Chen** — rectángulos (entidades), elipses (atributos), rombos (relaciones). La más usada.
- **Notación Crow's Foot** — líneas con formas en los extremos.
- **Notación UML** — diagramas de clases.

## Entidades

Objetos o conceptos del mundo real con existencia independiente e identificación única ("Cliente", "Producto", "Pedido"). Criterios: existencia independiente, identificación única, relevancia para el sistema.

> [!note] Representación en Chen
> Entidad → **rectángulo**; atributo → **elipse** (conectada a la entidad); relación → **rombo**. Clave primaria → elipse **subrayada**; clave candidata → subrayado discontinuo.

### Entidad fuerte y débil

- **Fuerte** — existe por sí sola. Rectángulo de línea simple.
- **Débil** — depende de una entidad fuerte para su existencia (p. ej. "Detalle de Pedido" depende de "Pedido"). Rectángulo de **doble línea**.
- Relaciones: de **identificación** (la débil no puede existir sin la fuerte; rombo de doble línea) o de **existencia** (rombo de línea simple).

## Atributos

Propiedades que describen a una entidad. Tienen nombre, tipo y valor.

### Simples vs. compuestos

- **Simple** — no se puede descomponer (p. ej. "Nombre").
- **Compuesto** — se descompone en subatributos (p. ej. "Dirección" → calle, número, ciudad, CP). Las elipses de los subatributos conectan con la elipse del compuesto.

### Tipos de clave

| Clave | Definición | En el diagrama |
|---|---|---|
| **Primaria** | Identifica de forma única cada instancia | Elipse subrayada |
| **Foránea** | Establece relación con otra entidad (atributo que referencia la clave de otra entidad) | Línea que conecta con la entidad principal |
| **Candidata** | Puede ser primaria pero no se ha elegido | Subrayado discontinuo |

## Relaciones

Asociación entre dos o más entidades (p. ej. "Cliente" **Realiza** "Pedido").

### Cardinalidad

Número de instancias de una entidad asociadas con una instancia de la otra. Siempre hay dos, una por entidad.

- **1:1** (uno a uno) — un Empleado tiene un Carnet; el Carnet pertenece a un único Empleado.
- **1:N** (uno a muchos) — un Cliente realiza muchos Pedidos, pero un Pedido solo es de un Cliente.
- **N:M** (muchos a muchos) — un Estudiante se inscribe en muchos Cursos y un Curso tiene muchos Estudiantes. Requiere **tabla intermedia** al pasar a tablas. Símbolo: N/M.

### Participación

- **Total** (obligatoria) — todas las instancias deben participar. Línea continua.
- **Parcial** (opcional) — algunas pueden no participar. Línea discontinua.

### Atributos de la relación

Describen propiedades de la relación en sí, no de las entidades (p. ej. "Fecha de Pedido" en "Realiza"). Elipses conectadas al rombo.

### Relaciones reflexivas y ternarias

- **Reflexiva (recursiva)** — involucran a la misma entidad (p. ej. un Empleado supervisa a otros Empleados). Rombo conectado a la misma entidad.
- **Ternaria (n-aria)** — involucran a tres o más entidades. No recomendable: es mejor descomponerla en varias relaciones binarias.

## E/R extendido

Version avanzada del diagrama E/R para representar **herencia**, **generalización** y **especialización** (entidades padre e hijas vía un triángulo):

- **Herencia** — la entidad hija hereda atributos y relaciones de la entidad padre (p. ej. "Persona" → "Profesor" y "Estudiante"). Puede ser **total** o **parcial**.
- **Generalización** — proceso de abstracción: identificar características comunes de varias entidades hijas y agruparlas en una entidad padre.
- **Especialización** — proceso de refinamiento: identificar características específicas y crear subentidades.

> [!note] Notación de propiedades (símbolos en el triángulo)
> - **Parcialidad**: generalización/specialización **parcial** → línea discontinua hacia el triángulo (no todas las entidades padre tienen hijas); **total** → todas las hijas participan.
> - **Solapamiento**: una entidad hija puede pertenecer a **más de una entidad padre** → símbolo **círculo**; **sin solapamiento** → las hijas pertenecen a una única padre.
> - **Exclusividad**: **exclusiva** (una hija solo en una padre) → **línea recta**; **no exclusiva** (una hija en varias padre) → **línea curvada**.

## Ejercicios (del tema)

1. **Alquiler de coches** — Cliente (nombre, dirección, teléfono) / Coche (marca, modelo, año); relación *alquiler* (fecha inicio, fin, precio total).
2. **Biblioteca** — Socio (nombre, dirección, teléfono) / Libro (título, autor, año); relación *préstamo* (fecha inicio, fin).
3. **Módulos (ternaria)** — Módulo, Profesor, Alumno; relación de asignación (fecha inicio, fin).
4. **Distribución (atributos y claves)** — Vehículo (identificación única, marca, modelo, año) / Conductor (nombre, dirección, teléfono) / Destino (nombre, dirección); relación *transporte* (fecha inicio, fin, precio).

## Ver también

- [[UD1 - Almacenamiento de datos y SGBD|Almacenamiento, ficheros y SGBD]] — base de la unidad anterior
- [[UD1 - Ficheros y formatos|Ficheros y formatos]]
- [[UD3 - Paso a tablas y normalización|Paso a tablas y normalización]] — conversión E/R a tablas y formas normales
- [[_Índice Bases de datos]]

---

← Volver a [[_Índice Bases de datos]]