---
tags:
  - lenguajes-de-marcas
  - ud1
  - xml
  - dtd
  - ejercicios
asignatura: Lenguajes de marcas
unidad: UD1
tema: Ejercicios DTD (1-24)
---

# UD1 — Ejercicios DTD (1-24)

Colección de 24 documentos XML con su **DTD interno** (el 24 usa uno externo). Fuente: `Anexos/Ejercicios_DTD.zip`; ficheros copiados en `Ejercicios/DTD/` (y `Ejercicios/DTD/DTDs/ligaDeFutbol.dtd`). Todos validan con `xmllint --valid`.

> [!info] Qué se practica
> Modelos de contenido (`,`, `|`, `?`, `*`, `+`), elementos `EMPTY`, `#PCDATA` y `ANY`, y atributos `CDATA`, `ID`, `IDREF(S)`, `NMTOKEN(S)` y enumeraciones.

## Resumen de los 24 ejercicios

| # | Documento | Qué modela | Clave DTD |
|---|---|---|---|
| 01 | `numeros` | Lista de números | `numero+` · `#PCDATA` |
| 02 | `escritores` | Escritores con nombre y nacimiento | Secuencia `(nombre, nacimiento)` |
| 03 | `musicos` | Músicos con apodo **o** nombre | `apodo?` · `nombre?` (opcionales) |
| 04 | `agenda` | Contactos con fijos (0-N) y móviles (1-N) | `telefonoFijo*` · `telefonoMovil+` |
| 05 | `sistemaSolar` | Planeta, satélite o asteroide | Elección `(planeta \| satelite \| asteroide)` |
| 06 | `aeropuertos` | Aeropuertos con estado de cierre | `cerrado?` + `EMPTY` |
| 07 | `vuelos` | Origen/destino en cualquier orden | `((origen, destino) \| (destino, origen))` |
| 08 | `reyes` | Reyes y reinas | `(rey \| reina)*` |
| 09 | `paises` | Pertenencia a UE/OTAN | Atributos implícitos como elementos `EMPTY` opcionales |
| 10 | `colores` | Color con código RGB o CMYK | `codigo (rgb \| cmyk)` |
| 11 | `contabilidad` | Ingresos y gastos | `(ingreso \| gasto)` con elementos `EMPTY` |
| 12 | `mensajes` | Mensajes con texto libre/HTML | `texto ANY` |
| 13 | `persona` | Persona vacía con DNI opcional | `EMPTY` + `CDATA #IMPLIED` |
| 14 | `cuadros` | Cuadros con título único y autor | `titulo ID #REQUIRED` |
| 15 | `listaCompra` | Ítems de la compra | `EMPTY` + dos `CDATA #REQUIRED` |
| 16 | `futbol` | Jugadores con nombre y código | `nombre NMTOKENS` · `codigo ID` |
| 17 | `futbol` | Jugadores y equipos | `jugadores IDREFS` |
| 18 | `libro` | Libro con autor | `autor NMTOKENS #REQUIRED` |
| 19 | `inventores` | Inventores e inventos | `#REQUIRED` + `#IMPLIED` |
| 20 | `cosasPorHacer` | Tareas con fechas | `#PCDATA` + atributos `CDATA` |
| 21 | `albumesMortadelo` | Álbumes por año | Enumeración `(1969\|…\|1974)` |
| 22 | `ligaDeFutbol` | Partidos con goles como elementos | `(local, visitante)` |
| 23 | `ligaDeFutbol` | Partidos con goles como atributos | `ATTLIST local goles CDATA #REQUIRED` |
| 24 | `ligaDeFutbol` | Partidos vacíos con 4 atributos | **DTD externo** `DTDs/ligaDeFutbol.dtd` |

## Conceptos, con ejemplos

### Cardinalidad `+`, `*`, `?`

```dtd
<!ELEMENT numeros (numero+)>              <!-- uno o más -->
<!ELEMENT agenda (contacto+)>
<!ELEMENT contacto (nombre, telefonoFijo*, telefonoMovil+)>
<!ELEMENT aeropuerto (nombre, cerrado?)>  <!-- cero o uno -->
```

- `+` obliga a que aparezca **al menos una vez**.
- `*` permite **cero o más**.
- `?` permite **cero o una**.

### Elección `|`

```dtd
<!ELEMENT cuerpo (planeta | satelite | asteroide)>
<!ELEMENT reyes (rey | reina)*>
<!ELEMENT codigo (rgb | cmyk)>
<!ELEMENT apunte ((ingreso | gasto), fecha, cantidad, concepto)>
```

Solo se permite **uno** de los elementos separados por `|`.

### Orden alternativo

`ejer07` permite las dos secuencias posibles agrupándolas:

```dtd
<!ELEMENT vuelo ((origen, destino) | (destino, origen))>
```

### Elementos vacíos y opcionales

```dtd
<!ELEMENT pais (nombre, unionEuropea?, otan?)>
<!ELEMENT unionEuropea EMPTY>
<!ELEMENT otan EMPTY>

<!ELEMENT cerrado EMPTY>
<!ELEMENT aeropuerto (nombre, cerrado?)>
```

En el XML se escriben como `<cerrado />` o `<cerrado></cerrado>`.

### `ANY`

```dtd
<!ELEMENT texto ANY>
<!ELEMENT strong (#PCDATA)>
```

`ANY` permite cualquier contenido. En `ejer12` se declara `strong` porque aparece dentro de `texto` y el validador debe conocerlo.

### Atributos `CDATA`

```dtd
<!ELEMENT persona EMPTY>
<!ATTLIST persona dni CDATA #IMPLIED>

<!ELEMENT item EMPTY>
<!ATTLIST item nombre CDATA #REQUIRED>
<!ATTLIST item cantidad CDATA #REQUIRED>
```

- `#IMPLIED`: el atributo puede faltar.
- `#REQUIRED`: el atributo es obligatorio.

### `ID`, `IDREF` e `IDREFS`

```dtd
<!ELEMENT cuadro EMPTY>
<!ATTLIST cuadro titulo ID #REQUIRED autor CDATA #REQUIRED>

<!ELEMENT jugador EMPTY>
<!ATTLIST jugador nombre NMTOKENS #REQUIRED codigo ID #REQUIRED>

<!ELEMENT equipo EMPTY>
<!ATTLIST equipo nombre CDATA #REQUIRED jugadores IDREFS #IMPLIED>
```

- `ID`: valor único, empieza por letra/`_`, sin espacios.
- `IDREF`: referencia a un `ID` existente.
- `IDREFS`: lista de referencias separadas por espacios (`jugadores="jc dam"`).

### `NMTOKEN` y `NMTOKENS`

```dtd
<!ATTLIST jugador nombre NMTOKENS #REQUIRED>
<!ATTLIST libro autor NMTOKENS #REQUIRED>
```

`NMTOKENS` permite una **lista de nombres XML** separados por espacios, sin que sean únicos. Es lo que permite `nombre="Mario Vargas Llosa"`.

### Enumeraciones

```dtd
<!ATTLIST album fecha (1969|1970|1971|1972|1973|1974) #REQUIRED>
```

El valor debe ser exactamente uno de los de la lista. Es la única forma de restringir valores en DTD (no hay tipos numéricos ni fechas).

### DTD externo

`ejer24` enlaza un DTD externo:

```dtd
<!ELEMENT ligaDeFutbol (partido*)>
<!ELEMENT partido EMPTY>
<!ATTLIST partido localNombre CDATA #REQUIRED>
<!ATTLIST partido localGoles CDATA #REQUIRED>
<!ATTLIST partido visitanteNombre CDATA #REQUIRED>
<!ATTLIST partido visitanteGoles CDATA #REQUIRED>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ligaDeFutbol SYSTEM "DTDs/ligaDeFutbol.dtd">
<ligaDeFutbol>
    <partido localNombre="Nottingham Presa" localGoles="0"
             visitanteNombre="Inter de Mitente" visitanteGoles="1" />
</ligaDeFutbol>
```

> [!warning] El DTD externo faltaba en la carpeta suelta
> En `Ejercicios_DTD/Ejercicios/` no aparecía `DTDs/ligaDeFutbol.dtd`, pero sí dentro de `Ejercicios_DTD.zip`. Se ha extraído a `Ejercicios/DTD/DTDs/` para que `ejer24.xml` valide.

## Validación

```bash
xmllint --noout --valid ejer01.xml
```

Todos los ejercicios (01-24) validan. Para `ejer24` hay que ejecutar el comando desde `Ejercicios/DTD/` (o ajustar la ruta del `SYSTEM`), porque el DTD se referencia como `DTDs/ligaDeFutbol.dtd`.

## Ver también

- [[UD1 - DTD (validación de XML)|Teoría de DTD]]
- [[Lenguajes de marcas/Ejercicios/UD1 - Supuesto agenda (DTD)|Supuesto agenda]]
- [[Lenguajes de marcas/Ejercicios/UD1 - Supuesto recetas (DTD)|Supuesto recetas]]
- [[Lenguajes de marcas/Ejercicios/UD1 - Ejemplos XML|Documentos XML de UD1]]
- [[_Índice Lenguajes de marcas]]

---

← Volver a [[_Índice Lenguajes de marcas]]
