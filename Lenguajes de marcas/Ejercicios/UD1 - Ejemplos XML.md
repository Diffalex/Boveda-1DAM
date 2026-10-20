---
tags:
  - lenguajes-de-marcas
  - ud1
  - xml
  - ejercicios
  - trabajo
asignatura: Lenguajes de marcas
unidad: UD1
tema: Documentos XML del curso
subtema: Ejemplos y plantillas
---

# UD1 — Documentos XML del curso

Nueve documentos de la unidad, copiados en `Ejercicios/`. Unos están resueltos y otros son **plantillas vacías** para practicar. Los DTD de la unidad se trabajan en [[UD1 - DTD (validación de XML)|UD1 — DTD]].

| Fichero | Tipo | Contenido | Idea clave |
|---|---|---|---|
| `Biblioteca.xml` | Resuelto | 4 libros con autores, precio y páginas | ISBN como atributo identificativo |
| `Clinica.xml` | Resuelto | 3 pacientes con datos personales | Todo como elementos |
| `agencia_turismo.xml` | Plantilla | Propietario, clientes, casas y reservas | Atributos `nif`, `dni`, `codigo` |
| `Alquileres.xml` | Plantilla | Empresa, vehículos, clientes y alquileres | Claves compuestas (matrícula + DNI) |
| `biblioteca_fp.xml` | Plantilla | Autores, libros, alumnos y préstamos | Referencias con `id_autor`, `id_libro`… |
| `instituto.xml` | Plantilla | Profesores, módulos, alumnos y cursos | Relaciones 1:N y N:M por referencias |
| `relaciones.xml` | Ejemplo | Cuatro supuestos de cardinalidad | Cómo modelar 1:N, N:M y 1:1 |
| `curriculum.xml` | Plantilla | Currículum con datos personales, formación y experiencia | Estructura completa sin rellenar |
| `tienda.xml` | Plantilla | Tienda con productos, clientes, compras y proveedores | Relación N:M mediante `compra` |

> [!note] Plantillas sin datos
> `agencia_turismo.xml`, `Alquileres.xml`, `biblioteca_fp.xml` e `instituto.xml` tienen la estructura creada pero los valores vacíos. Sirven para practicar el rellenado y, más adelante, su DTD.

## 1. Biblioteca (`Biblioteca.xml`)

Usa el **atributo `ISBN`** para identificar cada libro y **elementos** para el contenido estructurado.

```xml
<libro ISBN="9788419743442">
    <autores>
        <autor>RAFAL KOSIK</autor>
    </autores>
    <titulo>Cyberpunk 2077: No hay coincidencias</titulo>
    <editorial>Roca Editorial</editorial>
    <precio>22.70</precio>
    <num_paginas>416</num_paginas>
</libro>
```

> [!tip] ¿Por qué `ISBN` es atributo?
> Es un valor simple, único y no repetible que **identifica** el libro. Autores, título, precio y páginas son contenido estructurado → elementos.

## 2. Clínica (`Clinica.xml`)

Todos los datos del paciente son **elementos** (sin atributos): el DNI, la dirección, la provincia y el teléfono forman una jerarquía de contenido, no identificadores técnicos.

```xml
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
```

## 3. Agencia de turismo (`agencia_turismo.xml`)

Plantilla de la actividad presencial 3. El fichero original se llamaba `agencia_turismp.xml` (errata); en la bóveda se copió como `agencia_turismo.xml`.

```
agencia_turismo
├── propietario (nif)
│   ├── nombre, apellidos
│   ├── direccion (calle, numero, piso, codigoPostal, provincia)
│   ├── telefono
│   └── casa (codigo)
├── cliente (dni)
│   ├── nombre, apellidos, direccion, telefono, email
│   └── reserva (codigo)
└── casa (codigo)
    ├── nombre, direccion
    └── reserva (codigo)?
```

> [!warning] Diferencias con el enunciado
> La plantilla incluye `cliente` con una `reserva` y una `casa` con otra `reserva`, estructuras que no aparecían en el enunciado básico. Se conservan tal cual, pero conviene revisarlas al resolver la actividad. El `<!DOCTYPE agencia_turismo>` no tiene DTD asociado.

## 4. Alquileres (`Alquileres.xml`)

Plantilla de una empresa de alquiler de vehículos. La empresa tiene `CIF`, vehículos identificados por `Matricula` y clientes por `DNI`; los alquileres relacionan ambos.

```
empresa (CIF)
├── nombre, telefono_fijo, fax
├── vehiculos
│   └── vehiculo (Matricula)
│       └── marca, modelo, combustible, carroceria, precio_alquiler
├── clientes
│   └── cliente (DNI)
│       └── nombre_cliente, apellidos, domicilio…, telefono
└── alquileres_vehiculos
    └── alquiler_vehiculo (matricula, DNI, fecha, hora)
        └── num_dias, precio
```

> [!important] Correcciones de well-formedness
> El original tenía `<DOCTYPE Alquileres>` (sin `!` y con nombre distinto a la raíz `<empresa>`). Se corrigió a `<!DOCTYPE empresa>`. Sin ese arreglo el documento no era ni bien formado.

## 5. Biblioteca FP (`biblioteca_fp.xml`)

Plantilla con **referencias** entre bloques: autores y libros se definen una vez y se enlazan mediante atributos.

```xml
<autor id_autor="">
    <nombre></nombre>
    <nacionalidad></nacionalidad>
</autor>

<libro id_libro="">
    <titulo></titulo>
    <anio></anio>
    <genero></genero>
    <editorial></editorial>
    <autores>
        <autor ref_autor=""/>
    </autores>
</libro>

<prestamo id_prestamo="">
    <alumno ref_alumno=""/>
    <libro ref_libro=""/>
    <fecha_prestamo></fecha_prestamo>
    <fecha_devolucion></fecha_devolucion>
</prestamo>
```

> [!important] Correcciones de well-formedness
> El original tenía `<!Doctype biblioteca_fp>` (mayúsculas incorrectas) y `<titulo><titulo>` (sin cierre). Se corrigieron ambas; ahora es bien formado.

## 6. Instituto (`instituto.xml`)

Plantilla con tres niveles de información y referencias cruzadas:

```
instituto
├── profesores
│   └── profesor (DNI)
│       ├── nombre, direccion, telefono
│       └── modulos_impartidos
│           └── modulo (Codigo)
├── modulos
│   └── modulo (Codigo)
│       └── nombre
├── alumnos
│   └── alumno (Expediente)
│       ├── nombre, apellidos, fecha_nacimiento
│       └── modulos_matriculados
│           └── modulo (Codigo)
└── cursos
    └── curso (Nombre)
        ├── delegado (Expediente)
        └── grupo
            └── alumno (Expediente)
```

- Profesor → módulos: relación **N:M** (`modulos_impartidos`).
- Alumno → módulos: **N:M** (`modulos_matriculados`).
- Curso → alumnos: **1:N** (`grupo`).
- Curso → delegado: **1:1** (`delegado`, un alumno del grupo).
- Las referencias se guardan como atributos (`DNI`, `Codigo`, `Expediente`), no se repiten los datos completos.

## 7. Relaciones (`relaciones.xml`)

Documento didáctico con cuatro supuestos de cardinalidad, sin datos:

| Supuesto | Relación | Cómo se modela |
|---|---|---|
| 1 | Cliente → pedidos (**1:N**) | `pedidos` dentro de `cliente`; cada `pedido` con `cod_pedido` |
| 2 | Departamento → empleados (**1:N**) | `trabaja_en` con `cod_dpto` en cada empleado |
| 3 | Alumnos ↔ asignaturas (**N:M**) | Cada alumno referencia asignaturas y cada asignatura referencia alumnos |
| 4 | Cliente ↔ dirección (**1:1**) | Una dirección dentro del cliente, o referencia única |

> [!tip] Regla práctica
> - **1:N**: el “muchos” guarda la referencia al “uno”.
> - **N:M**: hace falta una tabla/intermediario (o referencias cruzadas).
> - **1:1**: se puede anidar o usar una referencia única.

## 8. Currículum (`curriculum.xml`)

Plantilla de currículum con datos personales, contacto, competencias, formación y experiencia. Ejemplo de anidación de bloques repetidos (varios puestos, varias competencias). Está **sin rellenar**: solo estructura.

## 9. Tienda (`tienda.xml`)

Plantilla de tienda informática con productos, clientes, compras y proveedores. La entidad `compra` relaciona clientes y productos (N:M) y añade la fecha. Se analiza en detalle en [[Lenguajes de marcas/Ejercicios/UD1 - Supuesto tienda (XML)|UD1 — Supuesto tienda]].

## Ver también

- [[UD1 - Atributos en XML|Análisis del uso de atributos en XML]]
- [[UD1 - DTD (validación de XML)|Validación de XML con DTD]]
- [[Lenguajes de marcas/Ejercicios/UD1 - Ejercicios DTD (1-24)|Ejercicios DTD (1-24)]]
- [[Lenguajes de marcas/Ejercicios/UD1 - Actividad presencial 3 (agencia de turismo)|Actividad presencial 3 — agencia de turismo]]
- [[Lenguajes de marcas/Ejercicios/UD1 - Supuesto tienda (XML)|Supuesto tienda]]
- [[_Índice Lenguajes de marcas]]

---

← Volver a [[_Índice Lenguajes de marcas]]
