---
tags:
  - bases-de-datos
  - ud1
  - almacenamiento
  - sgbd
asignatura: Bases de datos
unidad: UD1
tema: Almacenamiento de datos, ficheros y SGBD
---

# UD1 — Almacenamiento, ficheros y SGBD

Fuente: material `tema1-main.zip` (`Bases de datos/Anexos/`).

## Datos vs. información

- **Datos** — hechos, cifras o detalles sin procesar que carecen de significado por sí mismos.
- **Información** — el resultado de procesar y organizar los datos, lo que les da significado y utilidad para la toma de decisiones.

## Memoria y almacenamiento

| | Memoria | Almacenamiento |
|---|---|---|
| Función | Datos y programas **en uso activo** | Guardar información **de forma permanente** |
| Velocidad | Rápida | Más lento |
| Volatilidad | **Volátil** (pierde el contenido al apagarse) | **No volátil** (lo retiene) |

- **RAM** — memoria principal, volátil.
- **ROM** — solo lectura, no volátil (instrucciones y datos inalterables).
- **Caché** — alta velocidad para datos usados con frecuencia.
- **Memoria externa** — HDD/SSD, USB, tarjetas, discos ópticos, cintas magnéticas.

## Almacenamiento en la nube y redes

- **Cloud Storage** — datos en servidores remotos accesibles por Internet.
- **SAN** — redes especializadas que conectan servidores y almacenamiento (alto rendimiento empresarial).
- **NAS** — dispositivo de almacenamiento en la red accesible por varios usuarios.

## Modelos de almacenamiento

- **Basado en ficheros** — datos en archivos dentro de carpetas.
- **Basado en bloques** — datos divididos en bloques de tamaño fijo.
- **Basado en objetos** — datos + metadatos como objetos (escalable, típico de la nube).

## Seguridad, integridad y respaldo

Cifrado, control de acceso, respaldo y recuperación, redundancia (RAID, replicación), monitoreo y auditoría.

## Ficheros

Un **fichero** es un conjunto de datos almacenados en un dispositivo de almacenamiento. Tiene **nombre único** (obligatorio) y **extensión** (opcional, identifica el tipo de contenido).

- **Ficheros de texto** — texto plano legible (`.txt`, `.csv`, `.log`); pueden usar lenguajes de marcado (HTML, XML, Markdown).
- **Ficheros binarios** — no legibles directamente (ejecutables, imágenes, audio, vídeo, bibliotecas, datos).

### Ficheros de datos: de campo a archivo

- **Campo** — unidad más pequeña de información (un valor).
- **Registro** — conjunto de campos que representan una entidad.
- **Archivo** — conjunto de registros relacionados.

### Según su uso

- **Fichero maestro** — información principal y estructurada de una entidad.
- **Fichero de transacciones** — eventos o transacciones que ocurren.
- **Fichero histórico** — información archivada (clientes inactivos, históricos…).

### Acceso a ficheros

| Acceso | Cómo funciona | Ventaja | Inconveniente |
|---|---|---|---|
| **Secuencial** | Se lee/escribe uno tras otro | Máximo aprovechamiento del espacio; ideal para procesos *batch* | Búsqueda lenta O(N); modificar un registro intermedio exige recrear el fichero |
| **Aleatorio** | Cualquier orden, sin recorrer de principio | Acceso rápido a registros concretos | Requiere estructura de índices, más recursos |
| **Directo (indexado)** | Acceso por dirección/identificador con índice | Combinación de ambos; acceso rápido | Gestión más compleja |

Un fichero indexado se divide en **datos** e **índice**.

### Tipos de índices

- **Denso** — una entrada por cada registro.
- **No denso (esparcido)** — una entrada por cada bloque/página.
- **ISAM** — índice multinivel rígido ligado a la física del disco.
- **Árboles B+** — auto-balanceados; los datos en las hojas, los nodos internos forman el índice. Es el **estándar** en motores de BD modernos.

## Bases de datos

Una **base de datos (BD)** es un sistema organizado de almacenamiento de información que permite gestionar grandes volúmenes de datos de manera eficiente.

### Inconvenientes de los ficheros (que resuelve la BD)

Dificultad para mantener la **integridad**; **redundancia** de datos; **consultas complejas** difíciles; **dependencia** entre datos y programa; problemas de **acceso concurrente**; **falta de seguridad** y control de acceso.

### Tipos de BD

- **Relacionales (RDB)** — tablas con filas y columnas, y SQL.
- **Orientadas a objetos (OODB)** — datos como objetos con sus métodos.
- **Jerárquicas** — estructura de árbol (un padre, varios hijos).
- **NoSQL** — grandes volúmenes de datos no estructurados / semi-estructurados.

Según su estructura: **estáticas**, **dinámicas** o **distribuidas**.

## Modelos de datos

Jerárquico, de **red**, relacional (el más usado), orientado a objetos, NoSQL, multidimensional (BI) y de **grafos**.

### Modelo relacional

- **Tablas** — representan entidades.
- **Filas (registros)** — instancias de la entidad.
- **Columnas (atributos)** — propiedades.
- **Claves** — primarias (identifican el registro de forma única) y **foráneas** (establecen relaciones entre tablas).

## SGBD

Un **SGBD** (Sistema Gestor de Bases de Datos) es el software que permite crear, administrar y manipular bases de datos.

### Funciones principales

- Definición de estructuras de datos (tablas, campos, relaciones, restricciones).
- Gestión de usuarios y permisos.
- Optimización del rendimiento (indexación, consultas).
- Copias de seguridad y recuperación.
- Manejo de **transacciones** con propiedades **ACID**: *Atomicidad, Consistencia, Aislamiento y Durabilidad*.

### Componentes

Motor de almacenamiento, procesador de consultas, gestor de transacciones y gestor de seguridad.

### Arquitectura (niveles)

**Físico** (almacenamiento), **lógico** (tablas y relaciones) y de **usuario** (interfaz). Según dónde residen los datos: **centralizados** o **distribuidos**.

### Catálogo de SGBD

- **Privativos** — Oracle Database, Microsoft SQL Server, IBM Db2.
- **Código abierto** — MySQL (y MariaDB, su fork), PostgreSQL, MongoDB (NoSQL).

## Big Data y Business Intelligence (BI)

- **Big Data** — gestión de datos masivos que no pueden procesarse con métodos tradicionales. Se caracteriza por las **3 V** (Volumen, Velocidad, Variedad) ampliadas con **Veracidad** y **Valor**.
- Arquitectura: **Data Warehouse** (datos estructurados, modelado dimensional), **Data Lake** (datos en su forma original), **Data LakeHouse** (híbrido).
- **BI** — transforma los datos en información útil para la decisión empresarial (dashboards e informes interactivos). Herramientas: Tableau, Power BI, QlikView, Apache Superset.

## Normativa y protección de datos

- **RGPD** — reglamento europeo de protección de datos.
- **Principios**: licitud/lealtad/transparencia, limitación de la finalidad, **minimización de datos**, exactitud, limitación del plazo de conservación, integridad y confidencialidad.
- **Aplicado al diseño de BD**: minimizar datos personales, permisos y roles, medidas de seguridad, procedimientos (consentimiento, auditorías, RAT, DPD/DPO, EIPD).

## Ver también

- [[UD1 - Ficheros y formatos|Ficheros y formatos]] — estructura interna de formatos binarios
- [[UD2 - Modelo Entidad-Relación|Modelo Entidad-Relación]] — siguiente unidad
- [[_Índice Bases de datos]]

---

← Volver a [[_Índice Bases de datos]]