---
tags:
  - bases-de-datos
  - ud3
  - paso-a-tablas
  - normalizacion
  - modelo-relacional
  - claves
  - restricciones
asignatura: Bases de datos
unidad: UD3
tema: Paso a tablas y normalización
---

# UD3 — Paso a tablas y normalización

Fuente: `tema2-main.zip` (paso a tablas y normalización), en `Anexos/`. Material original de **Víctor Suárez** (IES Puebla de Vicar), licencia **CC BY-NC-SA 4.0**; este resumen lo adapta y corrige.

> [!note] Continuación
> La definición física con SQL (`CREATE TABLE`, tipos, restricciones y ejemplo) se estudia en [[UD4 - SQL (DDL)|UD4 — SQL (DDL)]].

> [!info] Contenido
> 1. Del E/R al modelo relacional
> 2. Claves y restricciones
> 3. Paso a tablas
> 4. Normalización

## Del E/R al modelo relacional

El diseño de una base de datos recorre tres niveles:

| Nivel | Representación | Qué define | Dependencia |
|---|---|---|---|
| **Conceptual** | Diagrama E/R | Entidades, atributos y relaciones | Independiente del SGBD |
| **Lógico** | Esquema relacional | Tablas, columnas, PK, UK y FK | Independiente del SGBD |
| **Físico** | SQL | Tipos de datos, restricciones, índices y almacenamiento | Depende del SGBD |

En este tema se trabaja el paso del **nivel conceptual** ([[UD2 - Modelo Entidad-Relación|E/R]]) al **lógico** (tablas) y al **físico** (SQL).

El **modelo relacional** organiza la información en **tablas** (relaciones), formadas por **filas** (registros o tuplas) y **columnas** (atributos). Las tablas se relacionan mediante **claves primarias** y **claves foráneas**.

> [!note] E/R vs. relacional
> El E/R es una representación **abstracta y conceptual** de la realidad. El modelo relacional es una representación **concreta y estructurada**: tablas que se implementarán en el SGBD.

### Diagrama relacional

Un **diagrama relacional simple** muestra las tablas, sus atributos, las claves (PK, UK, FK) y las relaciones:

```text
Usuarios (id PK, nombre, email, telefono, id_rol FK → Roles.id)
Roles    (id PK, nombre)
```

Un **diagrama relacional completo** añade el **dominio** de cada atributo (tipo de dato) y las **restricciones de integridad**:

```text
Usuarios (id INT PK, nombre VARCHAR(60), email VARCHAR(70),
          telefono VARCHAR(10), id_rol INT FK → Roles.id)
Roles    (id INT PK, nombre VARCHAR(60))
```

> [!warning] Tipos del diagrama original
> El material usa `NUMBER(13)` y `VARCHAR2`, propios de Oracle. En MySQL se utilizan `INT` y `VARCHAR(n)`. En este resumen se emplean los tipos de MySQL.

## Claves y restricciones

### Claves

| Clave | Regla | ¿Cuántas por tabla? |
|---|---|---|
| **Primaria (PK)** | Identifica de forma única cada fila; no admite `NULL` ni duplicados | Una |
| **Única (UK)** | Valores únicos; puede haber varias y **admite `NULL`** (MySQL permite varios `NULL`) | Varias |
| **Foránea (FK)** | Referencia la PK o UK de otra tabla; puede ser `NULL` | Varias |
| **Candidata** | Atributo que podría ser PK pero no se ha elegido | Varias |
| **Compuesta** | PK o UK formada por varias columnas | Según diseño |

> [!important] PK y UK no son equivalentes
> La **PK** es única y **no nula**. Una **UK** también es única, pero puede contener `NULL` (en MySQL, varias filas pueden tener `NULL`). El material se contradice en este punto; prevalece el comportamiento de MySQL.

### Restricciones de integridad

| Tipo | Qué garantiza | Se implementa con |
|---|---|---|
| **Integridad de entidad** | La PK existe, es única y no nula | `PRIMARY KEY` |
| **Integridad referencial** | Una FK apunta a una fila existente o es `NULL` | `FOREIGN KEY` |
| **Integridad de dominio** | El valor pertenece al tipo y rango permitidos | Tipo de dato, `NOT NULL`, `CHECK`, `DEFAULT` |
| **Reglas de negocio** | Condiciones propias de la organización | `CHECK` o lógica de la aplicación |

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

- [[UD4 - SQL (DDL)|SQL (DDL)]] — definición física: `CREATE TABLE`, tipos, restricciones y ejemplo
- [[UD2 - Modelo Entidad-Relación|Modelo Entidad-Relación]] — modelado previo
- [[UD1 - Almacenamiento de datos y SGBD|Almacenamiento, ficheros y SGBD]]
- [[_Índice Bases de datos]]

---

← Volver a [[_Índice Bases de datos]]
