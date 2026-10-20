---
tags:
  - lenguajes-de-marcas
  - ud1
  - xml
  - dtd
  - recetas
asignatura: Lenguajes de marcas
unidad: UD1
tema: Supuesto recetas (validación con DTD)
---

# UD1 — Supuesto recetas (DTD)

Práctica de recetas con DTD externo. Hay **dos versiones** del enunciado y conviene no mezclarlas:

| Versión | Enunciado | Modelo |
|---|---|---|
| **4.1** | `Anexos/supuestoRecetasValidacion.pdf` | `receta` con atributo `nombre`; `ingrediente` con hijos `nombre` y `cantidad` |
| **4.2** | `Anexos/Supuesto_recetas.pdf` | `nombre` como elemento; `ingrediente` con texto y atributos opcionales; pasos con `ID` |

La versión vigente y completa es la **4.2**. En el material del curso, el `recetas.dtd` original correspondía a 4.1, mientras que `recetas_dtd.xml` ya seguía 4.2: por eso no validaban juntos.

## Versión 4.1 (modelo inicial)

```
recetas (receta*)
└── receta                    attrs: nombre, numero_raciones, dificultad
    ├── ingredientes (ingrediente+)
    │   └── ingrediente
    │       ├── nombre
    │       └── cantidad      attr: unidad (obligatorio)
    └── elaboracion (paso*)
        └── paso              attr: cod_paso (CDATA)
```

```dtd
<?xml version="1.0" encoding="UTF-8"?>
<!ELEMENT recetas (receta*)>
<!ELEMENT receta (ingredientes, elaboracion)>
<!ATTLIST receta nombre CDATA #REQUIRED numero_raciones CDATA #REQUIRED dificultad CDATA #REQUIRED>
<!ELEMENT ingredientes (ingrediente+)>
<!ELEMENT ingrediente (nombre, cantidad)>
<!ELEMENT nombre (#PCDATA)>
<!ELEMENT cantidad (#PCDATA)>
<!ATTLIST cantidad unidad CDATA #REQUIRED>
<!ELEMENT elaboracion (paso*)>
<!ELEMENT paso (#PCDATA)>
<!ATTLIST paso cod_paso CDATA #REQUIRED>
```

Ficheros: `Ejercicios/DTD/recetas/recetas_41.dtd` y `recetas_41.xml` (plantilla original).

## Versión 4.2 (modelo final)

```
recetas (receta+)
└── receta                    attrs: numero_raciones, dificultad (enum, "media")
    ├── nombre (#PCDATA)
    ├── ingredientes (ingrediente+)
    │   └── ingrediente (#PCDATA)   attrs opcionales: cantidad, unidad
    └── elaboracion (paso+)
        └── paso (#PCDATA)          attr: cod_paso ID (único, obligatorio)
```

```dtd
<?xml version="1.0" encoding="UTF-8"?>
<!ELEMENT recetas (receta+)>
<!ELEMENT receta (nombre, ingredientes, elaboracion)>
<!ATTLIST receta
    numero_raciones CDATA #REQUIRED
    dificultad (baja | media | alta) "media">
<!ELEMENT nombre (#PCDATA)>
<!ELEMENT ingredientes (ingrediente+)>
<!ELEMENT ingrediente (#PCDATA)>
<!ATTLIST ingrediente
    cantidad CDATA #IMPLIED
    unidad CDATA #IMPLIED>
<!ELEMENT elaboracion (paso+)>
<!ELEMENT paso (#PCDATA)>
<!ATTLIST paso cod_paso ID #REQUIRED>
```

Ficheros: `Ejercicios/DTD/recetas/recetas.dtd`, `recetas.xml` (plantilla vacía válida) y `recetas_dtd.xml` (instancia completa).

### Cambios de 4.1 a 4.2

| Aspecto | 4.1 | 4.2 |
|---|---|---|
| Nº de recetas | `receta*` (0 o más) | `receta+` (1 o más) |
| Nombre de la receta | Atributo `nombre` | Elemento `nombre` |
| Ingrediente | Hijos `nombre` + `cantidad` | Texto libre + atributos `cantidad`/`unidad` opcionales |
| Unidad | Obligatoria en `cantidad` | Opcional (`#IMPLIED`) |
| Nº de pasos | `paso*` (0 o más) | `paso+` (1 o más) |
| `cod_paso` | `CDATA #REQUIRED` | `ID #REQUIRED` (único, empieza por letra/`_`) |
| `dificultad` | `CDATA #REQUIRED` | Enumeración `baja\|media\|alta`, por defecto `media` |

### Decisiones de diseño

- **`dificultad` enumerada** restringe los valores y evita erratas; el valor por defecto `"media"` hace que el atributo sea opcional.
- **`cod_paso` como `ID`** garantiza que no se repitan códigos de paso. Al ser `ID`, no puede empezar por dígito ni contener espacios.
- **`cantidad`/`unidad` opcionales** permiten ingredientes como “sal” o “agua” sin medida exacta.
- **`receta+` y `paso+`** obligan a que el documento tenga contenido real; una receta sin pasos no tiene sentido.

## Instancia válida

`recetas_dtd.xml` incluye varias recetas y cubre todas las posibilidades: ingredientes con ambos atributos, con uno solo y sin ninguno; recetas con un paso y con varios; y las tres dificultades, además de una receta **sin** `dificultad` para comprobar el valor por defecto `"media"`. Fragmento:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE recetas SYSTEM "recetas.dtd">
<recetas>
    <receta numero_raciones="4" dificultad="media">
        <nombre>Ensalada de tomate</nombre>
        <ingredientes>
            <ingrediente cantidad="3" unidad="piezas">Tomates maduros</ingrediente>
            <ingrediente cantidad="100" unidad="mililitros">Aceite de oliva virgen extra</ingrediente>
            <ingrediente cantidad="10" unidad="gramos">Sal</ingrediente>
        </ingredientes>
        <elaboracion>
            <paso cod_paso="p01">Lavar y cortar los tomates en rodajas.</paso>
            <paso cod_paso="p02">Aliñar con aceite y sal.</paso>
        </elaboracion>
    </receta>
</recetas>
```

## Validación

Desde `Ejercicios/DTD/recetas/`:

```bash
xmllint --noout --valid recetas.xml
xmllint --noout --valid recetas_dtd.xml
xmllint --noout --valid recetas_41.xml
```

Resultados: los tres pasan. `recetas_41.xml` valida contra `recetas_41.dtd`.

### Validación errónea (para la entrega)

El enunciado 4.2 pide **una captura comentada** de una validación fallida. Pruebas útiles:

| Cambio | Error esperado |
|---|---|
| `cod_paso="1"` | `ID` no válido: debe empezar por letra o `_` |
| Repetir `cod_paso="p01"` | `ID` duplicado |
| `dificultad="muy alta"` | Valor fuera de la enumeración |
| Quitar `numero_raciones` | Falta un atributo `#REQUIRED` |
| Poner `ingredientes` antes de `nombre` | El contenido no sigue el orden del DTD |
| Añadir `cantidad` a `receta` | Atributo no declarado |

> [!warning] Pendiente de la entrega
> No se incluye la captura de error en el material; hay que generarla con NetBeans o `xmllint` y comentar la causa.

## Correcciones aplicadas en la bóveda

- `recetas.dtd` original (modelo 4.1) se conserva como `recetas_41.dtd`; el `recetas.dtd` de la bóveda es el **4.2 oficial**.
- `recetas.xml` original (plantilla 4.1) se conserva como `recetas_41.xml`; se añadió un `recetas.xml` con la estructura 4.2.
- `recetas_dtd.xml` traía `<!DOCTYPE recetas SYSTEM "recetas.dtd"/>` (autocierre inválido). Se corrigió a `... "recetas.dtd">`; sin ese arreglo **no era ni bien formado**.
- El ZIP del supuesto no incluye los DTD; se conservan igualmente en `Anexos/`.

## Rúbrica

| Criterio | Dónde se cumple |
|---|---|
| DTD correctamente creado | `recetas.dtd` |
| Validez sintáctica del DTD | `xmllint --noout recetas.dtd` / Check DTD |
| XML y DTD enlazados | `recetas_dtd.xml` con `SYSTEM "recetas.dtd"` |
| XML validado e instanciado | `recetas_dtd.xml`, todas las posibilidades |
| Validación errónea | Pendiente de captura |

## Ver también

- [[UD1 - DTD (validación de XML)|Teoría de DTD]]
- [[Lenguajes de marcas/Ejercicios/UD1 - Ejercicios DTD (1-24)|Ejercicios DTD (1-24)]]
- [[Lenguajes de marcas/Ejercicios/UD1 - Supuesto agenda (DTD)|Supuesto agenda]]
- [[_Índice Lenguajes de marcas]]

---

← Volver a [[_Índice Lenguajes de marcas]]
