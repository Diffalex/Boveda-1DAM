---
tags:
  - bases-de-datos
  - ud3
  - paso-a-tablas
  - normalizacion
  - modelo-relacional
asignatura: Bases de datos
unidad: UD3
tema: Paso a tablas y normalización
---

# UD3 — Paso a tablas y normalización

Fuente: material `tema2-main.zip` (`Bases de datos/Anexos/`). Una vez diseñado el modelo entidad-relación ([[UD2 - Modelo Entidad-Relación|UD2]]), se convierte en **tablas** (paso a tablas) y después se **normaliza** para evitar redundancias.

> [!info] Contenido
> 1. El modelo relacional (tablas, claves)
> 2. Paso a tablas: entidades, relaciones y casos especiales
> 3. Normalización: dependencias funcionales y formas normales (1FN, 2FN, 3FN)

## Modelo relacional

Organiza la información en **tablas** (relaciones), formadas por **filas** (registros) y **columnas** (atributos). Las tablas se relacionan mediante **claves primarias** y **claves foráneas**.

Se confunde a veces con el modelo E/R, pero son distintos:

- **E/R** → representación **abstracta y conceptual** de la realidad.
- **Relacional** → representación **concreta y estructurada**: tablas que se implementarán en el SGBD.

### Notación de claves

- **Clave primaria (PK)** → se indica con el símbolo `PK` junto al atributo (y en el paso a tablas, subrayando el atributo).
- **Clave foránea (FK)** → se indica con `FK` junto al atributo + una flecha hacia la tabla que referencia.

Ejemplo de tabla con PK y FK:

`Usuario (id_usuario, nombre, email, id_rol)` → se subraya la PK `id_usuario` y se marca `id_rol` como FK hacia la tabla de Roles.

## Paso a tablas

Transforma cada componente del modelo E/R en tablas, definiendo atributos, claves y relaciones.

### Entidades

Cada **entidad** → una **tabla**; cada **atributo** → una **columna**. Toda tabla necesita una **clave primaria**.

### Relaciones (según cardinalidad)

| Cardinalidad | Cómo se materializa |
|---|---|
| **1:1** | La FK se añade en **cualquiera de las dos** tablas |
| **1:N** | La FK se añade en la tabla del **lado N** |
| **N:M** | Se crea una **tabla intermedia** con las PK de ambas tablas; si la relación tiene atributos, van en la intermedia |

### Relaciones especiales

- **Recursivas (reflexivas)** — la FK se añade en la propia tabla y referencia a la misma tabla (p. ej. `Employee.jefe → Employee.id`).
- **Especialización/generalización** — según si la relación es **total/parcial** y **disjunta/superpuesta**:
  - *Total* → se añade la FK en la tabla de la entidad general o se crea una tabla intermedia.
  - *Parcial* → se añade la FK en la tabla de la entidad especializada o se crea una tabla intermedia.

## Normalización

Proceso de diseño que **organiza los datos para minimizar la redundancia** y mejorar su **integridad**, aplicando reglas llamadas **formas normales** (de 1FN a 5FN).

> [!tip] Dependencias funcionales
> Se representan como **A → B**: el atributo (o conjunto) A determina de forma única el valor de B. Ejemplo: `id_empleado → nombre`. Identificarlas es el paso previo para normalizar correctamente.

> [!important] No siempre hace falta la forma normal máxima
> A veces mantener cierta redundancia mejora el rendimiento de las consultas. En el curso se pide llegar hasta **3FN**.

### 1FN — Primera forma normal

Una tabla está en 1FN si:

- Todos los atributos contienen valores **atómicos** (una celda = un único valor indivisible; no listas ni conjuntos).
- **No existen grupos de atributos repetidos** en la misma fila ni filas duplicadas.

> [!note] Ejemplo
> Tabla `Empleado` con atributo `Teléfonos` con varios números en una celda → se crea una tabla separada `Teléfonos` con un registro por número.

### 2FN — Segunda forma normal

Debe cumplir **1FN** y además:

- **Ningún atributo no clave depende parcialmente de la clave primaria** (si la PK es compuesta, ningún atributo no clave debe depender solo de una parte).

> [!note] Ejemplo
> `CP, Localidad, Provincia` dependen solo del `id_empleado`, no de toda la PK → se separa una tabla `Localidades`.

### 3FN — Tercera forma normal

Debe cumplir **2FN** y además:

- **Ningún atributo no clave depende de otro atributo no clave** (sin **dependencias transitivas**): A depende de B y B de la PK C → A depende de C a través de B.

> [!note] Ejemplo
> En `Localidades`, `Provincia` depende de `Localidad`, que depende de la PK → se divide en dos tablas para que cada atributo no clave dependa directamente de la PK.

### Formas normales superiores (4FN y 5FN)

- **4FN / Forma Normal de Boyce-Codd (FNBC)** — elimina **dependencias multivaluadas**.
- **5FN** — elimina **dependencias de unión**.

Se conocen para diseños complejos, pero **en el curso solo se pide llegar a 3FN**.

## Ver también

- [[UD2 - Modelo Entidad-Relación|Modelo Entidad-Relación]] — modelado previo (entidades, atributos, relaciones)
- [[UD1 - Almacenamiento de datos y SGBD|Almacenamiento, ficheros y SGBD]]
- [[_Índice Bases de datos]]

---

← Volver a [[_Índice Bases de datos]]