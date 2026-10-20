---
tags:
  - lenguajes-de-marcas
  - ud1
  - xml
  - dtd
  - validacion
asignatura: Lenguajes de marcas
unidad: UD1
tema: Validación de documentos XML con DTD
---

# UD1 — Validación de XML con DTD

Fuente: `Anexos/Lenguaje_DTD_Resumen.pdf`. Un documento XML puede estar **bien formado** y, aun así, no ser **válido**: el DTD (*Document Type Definition*) define la gramática que debe cumplir.

> [!info] Contenido
> 1. Bien formado vs válido
> 2. Asociar un DTD con `<!DOCTYPE>`
> 3. Declaración de elementos y cardinalidades
> 4. Declaración de atributos y sus tipos
> 5. Entidades
> 6. Validación con herramientas
> 7. Ejemplo completo
> 8. Limitaciones del DTD

## 1. Bien formado vs válido

| Concepto | Qué comprueba | Quién lo exige |
|---|---|---|
| **Bien formado** | Sintaxis XML: etiquetas cerradas, anidación correcta, un único raíz, atributos entrecomillados | Cualquier parser XML |
| **Válido** | Además, cumple las reglas del DTD: elementos permitidos, orden, cardinalidad, atributos obligatorios, tipos… | Parser **validador** + DTD |

Un XML bien formado sin DTD **no se puede validar**. La validación siempre es contra una definición (DTD, XSD…).

## 2. Asociar un DTD: `<!DOCTYPE>`

El DTD se declara en el **prólogo** del XML, después de la declaración `<?xml?>` y antes del elemento raíz.

**DTD interno** (las reglas van dentro del propio XML):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE numeros [
    <!ELEMENT numeros (numero+)>
    <!ELEMENT numero (#PCDATA)>
]>
<numeros>
    <numero>25</numero>
</numeros>
```

**DTD externo** (archivo `.dtd` aparte):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE recetas SYSTEM "recetas.dtd">
<recetas>
    ...
</recetas>
```

- `SYSTEM` indica que el DTD está en un archivo local (ruta relativa o absoluta).
- El nombre que sigue a `<!DOCTYPE` debe coincidir con el **elemento raíz** del XML.
- También existe `PUBLIC "id" "uri"` para DTDs públicos con identificador normalizado (no se usa en los ejercicios).

> [!warning] Errores típicos
> - `<!DOCTYPE raiz ... />` **no** es válido: el `DOCTYPE` no se autocierra.
> - `<!Doctype ...>` **no** existe: XML distingue mayúsculas y minúsculas.
> - Si el nombre del `DOCTYPE` no coincide con la raíz, el documento no es válido.

## 3. Declaración de elementos

Sintaxis:

```
<!ELEMENT nombreElemento (modelo de contenido)>
```

### 3.1 Elementos con hijos

Se indica la **secuencia ordenada** de hijos y su cardinalidad:

| Operador | Significado | Ejemplo |
|---|---|---|
| `,` | Secuencia: todos, en ese orden | `(nombre, telefono, direccion)` |
| `\|` | Elección: uno de ellos | `(DNI \| CIF)` |
| `()` | Agrupa una expresión | `(nombre, (DNI \| CIF))` |
| `?` | Opcional: 0 o 1 vez | `direccion?` |
| `*` | 0 o más veces | `telefono*` |
| `+` | 1 o más veces | `contacto+` |
| sin operador | Exactamente 1 vez | `nombre` |

Ejemplos:

```dtd
<!ELEMENT agenda (nombre, telefono, direccion?)>
<!ELEMENT cliente (nombre, (DNI | CIF))>
<!ELEMENT contactos (contacto+)>
<!ELEMENT agenda (nombre, telefono*, direccion?)>
```

> [!important] Orden y elección
> La coma implica **orden estricto**. Si se mezcla secuencia y elección, la elección va entre paréntesis: `(nombre, (DNI | CIF))`.
> `(a, b | c)` no significa lo que parece: hay que agrupar `(a, (b | c))`.

### 3.2 Elementos terminales

| Contenido | Significado |
|---|---|
| `(#PCDATA)` | Texto (datos alfanuméricos). Puede estar vacío. No puede contener `<`, `&`, etc. sin escapar |
| `EMPTY` | Elemento obligatoriamente vacío: `<cerrado />` |
| `ANY` | Cualquier contenido (elementos, texto…). Poco recomendable: no restringe nada |

```dtd
<!ELEMENT nombre (#PCDATA)>
<!ELEMENT cerrado EMPTY>
<!ELEMENT contenido ANY>
```

> [!note] `#PCDATA` no lleva atributos
> `(#PCDATA)` describe el **contenido** del elemento, no sus atributos. Los atributos se declaran aparte con `<!ATTLIST>`.

## 4. Declaración de atributos

Sintaxis:

```
<!ATTLIST elemento atributo tipo modificador>
```

Se pueden declarar varios atributos en un mismo `ATTLIST`:

```dtd
<!ATTLIST receta
    numero_raciones CDATA #REQUIRED
    dificultad (baja | media | alta) "media">
```

El **orden de los atributos** en el XML es indiferente.

### 4.1 Tipos de atributo

| Tipo | Qué admite | Reglas |
|---|---|---|
| **CDATA** | Texto libre (letras, números, espacios, símbolos) | Puede estar vacío |
| **Enumeración** `(a \| b \| c)` | Solo uno de los valores listados | Sin espacios ni comillas en la lista; puede llevar valor por defecto |
| **ID** | Identificador **único** en todo el documento | No puede repetirse; debe empezar por letra o `_`; sin espacios; solo letras, dígitos, `:`, `_`, `-`, `.`; solo `#REQUIRED` o `#IMPLIED` |
| **IDREF** | Referencia a un `ID` existente | El valor debe coincidir con un ID declarado en el documento |
| **IDREFS** | Lista de `IDREF` separados por espacios | Todos deben existir |
| **NMTOKEN** | Nombre XML no único | Letras, dígitos, `:`, `_`, `-`, `.`; sin espacios ni tildes; puede empezar por dígito |
| **NMTOKENS** | Lista de `NMTOKEN` separados por espacios | — |
| **ENTITY / ENTITIES** | Referencia a una entidad declarada | Se usa con entidades externas no textuales |

> [!warning] ID no es un número
> Un `ID` como `cod_persona="03"` **no es válido**: empieza por dígito. Habría que usar `p03` o declararlo como `CDATA`. Esta es la razón por la que la agenda del curso declara `cod_persona` como `CDATA`.

### 4.2 Modificadores

| Modificador | Significado |
|---|---|
| `#REQUIRED` | Obligatorio; sin valor por defecto |
| `#IMPLIED` | Opcional; sin valor por defecto |
| `#FIXED "valor"` | Si aparece, debe tener exactamente ese valor; si no aparece, se aplica |
| `"valor"` | Valor por defecto: el atributo es opcional y, si falta, toma ese valor |

```dtd
<!ATTLIST alumno codigo ID #REQUIRED>
<!ATTLIST alumno nivel NMTOKEN #IMPLIED>
<!ATTLIST alumno nacionalidad NMTOKEN #FIXED "Española">
<!ATTLIST receta dificultad (baja | media | alta) "media">
```

## 5. Entidades

Las entidades son como “variables” que se sustituyen por su contenido. Sirven para reutilizar texto o incluir contenido externo.

### 5.1 Entidades internas

```dtd
<!DOCTYPE saludo [
    <!ENTITY firma "Departamento de Atención al Cliente">
]>
<mensaje>
    <cuerpo>Gracias por contactar con nosotros.</cuerpo>
    <firma>&firma;</firma>
</mensaje>
```

### 5.2 Entidades externas textuales

```dtd
<!DOCTYPE aviso [
    <!ENTITY condiciones SYSTEM "condiciones.txt">
]>
<documento>
    <titulo>Aviso Legal</titulo>
    <contenido>&condiciones;</contenido>
</documento>
```

### 5.3 Entidades externas no textuales (binarias)

Se declaran con `NDATA` y se referencian mediante un atributo de tipo `ENTITY`:

```dtd
<!DOCTYPE galeria [
    <!ELEMENT imagen (titulo)>
    <!ATTLIST imagen archivo ENTITY #REQUIRED>
    <!ENTITY logo SYSTEM "logo.png" NDATA png>
]>
<galeria>
    <imagen archivo="logo">
        <titulo>Logotipo corporativo</titulo>
    </imagen>
</galeria>
```

### 5.4 Entidades predefinidas

XML define `&lt;` `<`, `&gt;` `>`, `&amp;` `&`, `&quot;` `"` y `&apos;` `'`. Se usan para incluir caracteres que el parser interpretaría como marcado.

## 6. Validación con herramientas

En **NetBeans**:

| Comando | Qué comprueba |
|---|---|
| **Check XML** | Que el XML está bien formado |
| **Check DTD** | Que el DTD es sintácticamente correcto |
| **Validate XML** | Que el XML cumple el DTD |

Alternativas: extensión **XML** de VS Code (muestra “Valid”), validadores online como `xmlvalidation.com` o `stratecode.tools`.

Errores habituales que detecta el validador:

- Falta un atributo `#REQUIRED`.
- Un atributo enumerado tiene un valor no permitido.
- Un `ID` está duplicado o empieza por dígito.
- Los hijos están en orden incorrecto o falta un elemento obligatorio (`+`).
- Aparece un elemento o atributo no declarado en el DTD.

> [!tip] El DTD no valida tipos de datos
> `CDATA` acepta cualquier texto: no comprueba que `numero_raciones` sea numérico ni que una fecha sea real. Para eso harían falta tipos de XML Schema (XSD) o validación en la aplicación.

## 7. Ejemplo completo

```dtd
<?xml version="1.0" encoding="UTF-8"?>
<!ELEMENT agenda (propietario, contactos)>
<!ELEMENT propietario (nombre, telefono+)>
<!ELEMENT contactos (contacto+)>
<!ELEMENT contacto (nombre, telefono+, email?)>
<!ATTLIST contacto codigo ID #REQUIRED>
<!ELEMENT nombre (#PCDATA)>
<!ELEMENT telefono (#PCDATA)>
<!ELEMENT email (#PCDATA)>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE agenda SYSTEM "agenda.dtd">
<agenda>
    <propietario>
        <nombre>Alma López</nombre>
        <telefono>970898765</telefono>
    </propietario>
    <contactos>
        <contacto codigo="p01">
            <nombre>Inés López</nombre>
            <telefono>970123123</telefono>
            <email>ines@example.com</email>
        </contacto>
        <contacto codigo="p02">
            <nombre>Roberto Gutiérrez</nombre>
            <telefono>970987456</telefono>
            <telefono>942333323</telefono>
        </contacto>
    </contactos>
</agenda>
```

## 8. Limitaciones del DTD

- Su sintaxis **no es XML** (se escribe con `<!ELEMENT>`, `<!ATTLIST>`…).
- No tiene tipos de datos reales (todo es texto salvo enumeraciones).
- No soporta **namespaces** ni restricciones de unicidad complejas.
- Alternativas modernas: **XML Schema (XSD)** y **RELAX NG**. Aun así, el DTD es sencillo, está muy extendido y es el que se trabaja en este módulo.

## Ver también

- [[UD1 - Atributos en XML|Atributos en XML]] — atributos vs elementos
- [[Lenguajes de marcas/Ejercicios/UD1 - Ejemplos XML|Documentos XML del curso]] — XML de UD1 resumidos
- [[Lenguajes de marcas/Ejercicios/UD1 - Ejercicios DTD (1-24)|Ejercicios DTD (1-24)]] — 24 DTDs de ejemplo
- [[Lenguajes de marcas/Ejercicios/UD1 - Supuesto agenda (DTD)|Supuesto agenda]] y [[Lenguajes de marcas/Ejercicios/UD1 - Supuesto recetas (DTD)|supuesto recetas]] — prácticas completas
- [[_Índice Lenguajes de marcas]]

---

← Volver a [[_Índice Lenguajes de marcas]]
