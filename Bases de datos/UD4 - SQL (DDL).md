---
tags:
  - bases-de-datos
  - ud4
  - sql
  - ddl
  - mysql
  - restricciones
asignatura: Bases de datos
unidad: UD4
tema: SQL (DDL)
---

# UD4 — SQL (DDL)

Fuente: `tema3-main.zip` (Tema 3: El Lenguaje SQL. Definición de datos), en `Anexos/`. Material original de **Víctor Suárez** (IES Puebla de Vicar), licencia **CC BY-NC-SA 4.0**; este resumen lo adapta y corrige.

> [!info] Contenido
> 1. SQL y tipos de sentencias
> 2. DDL
> 3. `CREATE TABLE`
> 4. Tipos de datos en MySQL
> 5. Restricciones
> 6. Ejemplo `usuarios_roles`
> 7. Errores comunes

> [!note] Requisito
> Para el diseño de tablas y la normalización, consulta [[UD3 - Paso a tablas y normalización|UD3 — Paso a tablas y normalización]]. Esta unidad se centra en **DDL**; no incluye DML ni consultas.

## SQL

**SQL** (*Structured Query Language*) es el lenguaje estándar para definir, manipular y consultar bases de datos relacionales. Nació en IBM en los años 70 y es un lenguaje **declarativo**: se indica *qué* se quiere, no *cómo* obtenerlo.

En el curso se utiliza **MySQL** (con MySQL Workbench), aunque la mayor parte de la sintaxis es común a otros SGBD.

### Tipos de sentencias

| Tipo | Nombre | Sentencias | Para qué |
|---|---|---|---|
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Definir y modificar la estructura |
| **DML** | Data Manipulation Language | `SELECT`, `INSERT`, `UPDATE`, `DELETE` | Manipular los datos |
| **TCL** | Transaction Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Controlar transacciones |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` | Gestionar permisos |

Este tema se centra en **DDL**: crear la estructura de la base de datos, no rellenarla.

## DDL

| Sentencia | Función | Ejemplo |
|---|---|---|
| `CREATE` | Crea bases de datos, tablas, índices o vistas | `CREATE TABLE ...` |
| `ALTER` | Modifica la estructura de un objeto existente | `ALTER TABLE ... ADD ...` |
| `DROP` | Elimina el objeto y todos sus datos | `DROP TABLE ...` |
| `TRUNCATE` | Vacía una tabla pero conserva su estructura | `TRUNCATE TABLE ...` |

> [!warning] DDL y transacciones
> En MySQL, las sentencias DDL provocan un **commit implícito**: no se pueden deshacer con `ROLLBACK`. Hay que extremar las precauciones con `DROP` y `TRUNCATE`.

### `DROP` vs. `TRUNCATE` vs. `DELETE`

| | `DROP TABLE` | `TRUNCATE TABLE` | `DELETE FROM` |
|---|---|---|---|
| Elimina | Estructura y datos | Todos los datos | Filas seleccionadas |
| ¿Se puede deshacer? | No | No (DDL) | Sí, si hay transacción |
| ¿Admite `WHERE`? | No | No | Sí |
| `AUTO_INCREMENT` | Desaparece | Se reinicia | No se reinicia |
| Velocidad | Rápida | Muy rápida | Más lenta |

### `CREATE TABLE`

```sql
CREATE TABLE [IF NOT EXISTS] [esquema.]nombre_tabla (
    columna1 tipo_dato [restricciones],
    columna2 tipo_dato [restricciones],
    ...
    columnaN tipo_dato [restricciones],
    [restricciones de tabla]
);
```

- `IF NOT EXISTS` evita el error si la tabla ya existe. En MySQL **no** existe `IF EXISTS` para `CREATE`.
- El esquema es opcional; si se omite, se usa el de la base de datos activa.
- Los nombres de tablas y columnas deben empezar por letra y pueden contener letras, números y `_`; no se admiten espacios.
- Los nombres de tabla son únicos dentro del esquema; los de columna, dentro de la tabla.

### Tipos de datos en MySQL

| Tipo | Uso | Ejemplo |
|---|---|---|
| `INT`, `BIGINT` | Números enteros | `id INT` |
| `DECIMAL(p, s)` | Decimales exactos (precisión y escala) | `precio DECIMAL(10,2)` |
| `VARCHAR(n)` | Texto variable de hasta `n` caracteres | `nombre VARCHAR(60)` |
| `CHAR(n)` | Texto fijo de `n` caracteres | `codigo CHAR(2)` |
| `TEXT` | Texto largo sin límite práctico | `descripcion TEXT` |
| `DATE` | Fecha (`YYYY-MM-DD`) | `fecha_alta DATE` |
| `TIME` | Hora | `hora TIME` |
| `DATETIME` | Fecha y hora | `creado DATETIME` |
| `TIMESTAMP` | Marca temporal | `actualizado TIMESTAMP` |
| `BOOLEAN` | Booleano; en MySQL es alias de `TINYINT(1)` | `activo BOOLEAN` |
| `BLOB` | Datos binarios | `imagen BLOB` |

> [!note] Tipos de otros SGBD
> `NUMBER` y `VARCHAR2` son de Oracle, no de MySQL. `VARCHAR2` aparece en algunos ejemplos del material; en MySQL se usa `VARCHAR`.

### Restricciones

| Restricción | Qué hace |
|---|---|
| `PRIMARY KEY` | Identifica cada fila; única y no nula; solo una por tabla |
| `FOREIGN KEY` | Referencia la PK/UK de otra tabla y mantiene la integridad referencial |
| `UNIQUE` | Impide valores duplicados; admite `NULL` y puede haber varias |
| `NOT NULL` | Obliga a que la columna tenga un valor |
| `DEFAULT` | Valor que se aplica si no se indica otro |
| `CHECK` | Condición que debe cumplir el valor (MySQL 8.0.16+) |
| `AUTO_INCREMENT` | Genera un entero consecutivo automáticamente |
| `CONSTRAINT nombre` | Asigna un nombre a una restricción |

#### Claves

```sql
PRIMARY KEY (columna)
PRIMARY KEY (columna1, columna2)          -- clave compuesta
FOREIGN KEY (columna_foranea) REFERENCES tabla_referenciada(columna)
```

- La tabla referenciada debe crearse **antes** que la que contiene la FK.
- La columna referenciada debe ser PK o UK.
- Una FK puede ser `NULL` si la relación es opcional.
- MySQL/InnoDB exige un índice en la columna de la FK; si no existe, lo crea automáticamente.

#### Acciones de clave foránea

| Acción | Al borrar o actualizar la fila referenciada |
|---|---|
| `CASCADE` | Propaga el cambio a las filas relacionadas |
| `SET NULL` | Pone la FK a `NULL` (la columna debe admitir nulos) |
| `RESTRICT` | Impide la operación si hay filas relacionadas |
| `NO ACTION` | Equivale a `RESTRICT` en MySQL |

```sql
FOREIGN KEY (id_rol) REFERENCES Roles(id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
```

Si no se indica acción, MySQL aplica `RESTRICT`/`NO ACTION`.

#### `NOT NULL`, `DEFAULT`, `CHECK`, `UNIQUE` y `AUTO_INCREMENT`

- **`NOT NULL`**: la PK ya es `NOT NULL` implícitamente.
- **`DEFAULT`**: se puede combinar con `NOT NULL` para asegurar un valor.
- **`CHECK`**: en MySQL solo se aplica desde la versión **8.0.16**; antes se aceptaba pero se ignoraba.
- **`UNIQUE`**: no garantiza integridad referencial; para eso está la FK.
- **`AUTO_INCREMENT`**: solo en columnas numéricas, una por tabla, y debe estar indexada (normalmente es la PK).

#### Claves compuestas y restricciones nombradas

```sql
CREATE TABLE Matriculas (
    id_alumno INT,
    id_asignatura INT,
    curso VARCHAR(9),
    nota DECIMAL(4,2),
    PRIMARY KEY (id_alumno, id_asignatura, curso),
    CONSTRAINT fk_mat_alumno FOREIGN KEY (id_alumno) REFERENCES Alumnos(id),
    CONSTRAINT fk_mat_asignatura FOREIGN KEY (id_asignatura) REFERENCES Asignaturas(id),
    CONSTRAINT chk_nota CHECK (nota BETWEEN 0 AND 10)
);
```

Nombrar las restricciones facilita identificarlas y modificarlas después. El nombre debe ser único en la base de datos.

### Ejemplo: `usuarios_roles`

```sql
CREATE DATABASE IF NOT EXISTS usuarios_roles;
USE usuarios_roles;

CREATE TABLE Roles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(60) NOT NULL
);

CREATE TABLE Usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15),
    id_rol INT,
    CONSTRAINT FK_Usuarios_Roles FOREIGN KEY (id_rol)
        REFERENCES Roles(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

SHOW TABLES;
DESCRIBE Usuarios;
```

> [!note] Decisiones del ejemplo
> - `Roles` se crea antes que `Usuarios` porque `Usuarios` la referencia.
> - `email` es `NOT NULL UNIQUE`: no puede faltar ni repetirse.
> - `id_rol` admite `NULL` y usa `ON DELETE SET NULL`: si se borra un rol, los usuarios quedan sin rol. Si se prefiere impedir el borrado, se usa `RESTRICT`.
> - `AUTO_INCREMENT` genera los identificadores automáticamente.

Para modificar la estructura:

```sql
ALTER TABLE Usuarios ADD fecha_alta DATE;
```

Para eliminar las tablas, primero la que contiene la FK:

```sql
DROP TABLE IF EXISTS Usuarios;
DROP TABLE IF EXISTS Roles;
```

## Errores comunes del material

| Punto | Problema | Corrección |
|---|---|---|
| `CREATE TABLE Roles (...)` | Coma final antes del `)` → sentencia inválida | Eliminar la coma |
| `UNIQUE` y `NULL` | Un apartado dice que no admite nulos y otro que sí | En MySQL, `UNIQUE` admite varios `NULL`; la PK no |
| `NUMBER`, `VARCHAR2` | Son tipos de Oracle | Usar `INT`, `VARCHAR` en MySQL |
| `IF [NOT] EXISTS` | No es sintaxis exacta de MySQL | `IF NOT EXISTS` |
| `CHECK` | Se presenta como siempre aplicado | Solo se aplica desde MySQL 8.0.16 |
| `CREATE TABLE` sin `USE` | Error si no hay base de datos activa | Crear y seleccionar la BD antes |

> [!tip] Buenas prácticas
> - Elige el tipo de dato más ajustado y define la PK desde el principio.
> - Nombra las restricciones (`CONSTRAINT`) y documenta las decisiones.
> - Crea las tablas en orden de dependencias.
> - Haz copia de seguridad antes de `DROP` o `TRUNCATE`.
> - No uses `SELECT *` en producción; en este tema basta con `SHOW TABLES` y `DESCRIBE`.

## Referencias

- [W3Schools — SQL](https://www.w3schools.com/sql/)
- [DataCamp — Comandos DDL en SQL](https://www.datacamp.com/es/tutorial/sql-ddl-commands)
- [MySQL 8.0 — CREATE TABLE](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [MySQL 8.0 — FOREIGN KEY](https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html)

## Ver también

- [[UD3 - Paso a tablas y normalización|Paso a tablas y normalización]] — diseño lógico y normalización
- [[UD2 - Modelo Entidad-Relación|Modelo Entidad-Relación]] — modelado previo
- [[_Índice Bases de datos]]

---

← Volver a [[_Índice Bases de datos]]
