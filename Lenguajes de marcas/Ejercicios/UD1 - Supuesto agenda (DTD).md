---
tags:
  - lenguajes-de-marcas
  - ud1
  - xml
  - dtd
  - agenda
asignatura: Lenguajes de marcas
unidad: UD1
tema: Supuesto agenda (validación con DTD)
---

# UD1 — Supuesto agenda (DTD)

Actividad presencial 4.3: validar `agenda.xml` con el DTD `agenda.dtd`, entregando además `agenda_dtd.xml` enlazado y validado.

> [!info] Ficheros
> - `Ejercicios/DTD/agenda/agenda.dtd` — reglas
> - `Ejercicios/DTD/agenda/agenda.xml` — plantilla (vacía)
> - `Ejercicios/DTD/agenda/agenda_dtd.xml` — instancia completa y válida
> - `Anexos/descripcionAgenda.pdf` — enunciado
> - `Anexos/supuestoAgenda.zip` — paquete original (no incluye el DTD)

## Estructura

```
agenda
├── propietario
│   ├── identificadores
│   │   ├── nombre
│   │   └── apellidos
│   ├── direccion
│   │   ├── calle
│   │   ├── localidad
│   │   └── cp
│   └── telefonos
│       ├── movil?
│       ├── casa?
│       └── trabajo?
└── contactos
    └── persona+            (atributo cod_persona)
        ├── identificadores
        ├── direccion
        └── telefonos
```

## DTD

```dtd
<?xml version="1.0" encoding="UTF-8"?>
<!ELEMENT agenda (propietario, contactos)>
<!ELEMENT propietario (identificadores, direccion, telefonos)>
<!ELEMENT identificadores (nombre, apellidos)>
<!ELEMENT nombre (#PCDATA)>
<!ELEMENT apellidos (#PCDATA)>
<!ELEMENT direccion (calle, localidad, cp)>
<!ELEMENT calle (#PCDATA)>
<!ELEMENT localidad (#PCDATA)>
<!ELEMENT cp (#PCDATA)>
<!ELEMENT telefonos (movil?, casa?, trabajo?)>
<!ELEMENT movil (#PCDATA)>
<!ELEMENT casa (#PCDATA)>
<!ELEMENT trabajo (#PCDATA)>
<!ELEMENT contactos (persona+)>
<!ELEMENT persona (identificadores, direccion, telefonos)>
<!ATTLIST persona cod_persona CDATA #REQUIRED>
```

## Decisiones de diseño

| Regla | Por qué |
|---|---|
| `agenda (propietario, contactos)` | Exactamente un propietario y un bloque de contactos, en ese orden |
| `contactos (persona+)` | La agenda debe tener **al menos un** contacto |
| `telefonos (movil?, casa?, trabajo?)` | Los tres teléfonos son opcionales; una persona puede no tener, por ejemplo, teléfono del trabajo |
| `cod_persona CDATA #REQUIRED` | Identifica a cada contacto y es obligatorio, pero **no es `ID`** porque en la instancia aparece `cod_persona="03"` y un `ID` no puede empezar por dígito |
| Sin atributo en `propietario` | El propietario es único; no necesita identificador |

> [!important] `CDATA` vs `ID`
> Si se declarara `cod_persona ID #REQUIRED`, la instancia con `"03"` sería **inválida**. Para usar `ID` habría que cambiar los valores a `p03`, `p04`… o mantener `CDATA`, como hace la solución del curso.

## Instancia válida

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE agenda SYSTEM "agenda.dtd">
<agenda>
    <propietario>
        <identificadores>
            <nombre>Alma</nombre>
            <apellidos>López Terán</apellidos>
        </identificadores>
        <direccion>
            <calle>El Percebe 13, 6F</calle>
            <localidad>Torrelavega</localidad>
            <cp>39300</cp>
        </direccion>
        <telefonos>
            <movil>970898765</movil>
            <casa>942124567</casa>
            <trabajo>628983456</trabajo>
        </telefonos>
    </propietario>
    <contactos>
        <persona cod_persona="p01">
            <identificadores>
                <nombre>Inés</nombre>
                <apellidos>López Pérez</apellidos>
            </identificadores>
            <direccion>
                <calle>El Ranchito 24, 6B</calle>
                <localidad>Santander</localidad>
                <cp>39006</cp>
            </direccion>
            <telefonos>
                <movil>970123123</movil>
            </telefonos>
        </persona>
        <persona cod_persona="p02">
            <identificadores>
                <nombre>Roberto</nombre>
                <apellidos>Gutiérrez Gómez</apellidos>
            </identificadores>
            <direccion>
                <calle>El Marranito 4, 2F</calle>
                <localidad>Santander</localidad>
                <cp>39004</cp>
            </direccion>
            <telefonos>
                <movil>970987456</movil>
                <casa>942333323</casa>
            </telefonos>
        </persona>
        <persona cod_persona="03">
            <identificadores>
                <nombre>Juan</nombre>
                <apellidos>Sánchez Martínez</apellidos>
            </identificadores>
            <direccion>
                <calle>El Cangrejo 10, sn</calle>
                <localidad>Torrelavega</localidad>
                <cp>39300</cp>
            </direccion>
            <telefonos>
                <movil>997564343</movil>
                <casa>942987974</casa>
                <trabajo>677899234</trabajo>
            </telefonos>
        </persona>
    </contactos>
</agenda>
```

## Validación

Desde `Ejercicios/DTD/agenda/`:

```bash
xmllint --noout --valid agenda.xml
xmllint --noout --valid agenda_dtd.xml
```

Ambos pasan sin errores. En NetBeans: **Check DTD** → **Validate XML**.

Pruebas de error que conviene documentar en la entrega:

- Quitar `cod_persona` de una persona → falta un atributo `#REQUIRED`.
- Poner un teléfono antes de `identificadores` → orden incorrecto.
- Dejar `contactos` vacío → `persona+` exige al menos una.
- Repetir un `cod_persona` **no** da error mientras sea `CDATA`; sí lo daría si se cambiara a `ID`.

> [!warning] Pendiente de la entrega
> El enunciado pide una **captura de una validación errónea** comentada. No venía incluida en el material; hay que generarla al hacer la actividad (basta con provocar uno de los errores anteriores).

## Ver también

- [[UD1 - DTD (validación de XML)|Teoría de DTD]]
- [[Lenguajes de marcas/Ejercicios/UD1 - Ejercicios DTD (1-24)|Ejercicios DTD (1-24)]]
- [[Lenguajes de marcas/Ejercicios/UD1 - Supuesto recetas (DTD)|Supuesto recetas]]
- [[_Índice Lenguajes de marcas]]

---

← Volver a [[_Índice Lenguajes de marcas]]
