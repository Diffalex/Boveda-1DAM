---
tags:
  - lenguajes-de-marcas
  - ud1
  - xml
  - atributos
asignatura: Lenguajes de marcas
unidad: UD1
tema: Análisis del uso de atributos en XML
---

# UD1 — Análisis del uso de atributos en XML

Los **atributos** en XML añaden información complementaria a los elementos. Es fundamental distinguir cuándo un dato debe representarse como **atributo** y cuándo como **elemento**, según su significado, estructura y posible evolución.

## Cuándo usar atributos

Los atributos son adecuados cuando la información es **identificativa, breve, no estructurada** y **no necesita subelementos**.

```xml
<producto id="P001" tipo="electrónico">
    <nombre>Ratón inalámbrico</nombre>
</producto>

<factura moneda="EUR" fecha="2025-10-14" tipo="A">
    <cliente nombre="Juan Pérez" />
</factura>
```

**Casos típicos de uso de atributos:**

- Información identificativa (`id`, `código`, `ISBN`, `NIF`, etc.).
- Propiedades simples o metadatos (`tipo`, `versión`, `idioma`, `moneda`).
- Valores que sirven para clasificar o filtrar elementos.
- Información que no puede repetirse ni tiene jerarquía interna.

## Cuándo no usar atributos

No deben usarse cuando la información forma parte **esencial del contenido** o puede requerir **estructura, repetición o formato**.

```xml
<!-- Incorrecto: dirección es contenido estructurado -->
<direccion valor="Calle Mayor, 10, Madrid"/>

<!-- Correcto: la dirección se descompone en elementos -->
<direccion>
    <calle>Calle Mayor, 10</calle>
    <ciudad>Madrid</ciudad>
</direccion>
```

**Evitar atributos cuando:**

- El dato tiene estructura o puede desglosarse (dirección, persona, producto…).
- Puede repetirse (colores, autores, teléfonos…).
- Puede requerir formato, idioma o etiquetas internas.
- Es parte importante del contenido semántico del documento.

## Comparativa: atributos vs elementos

| Criterio | Atributo | Elemento |
|---|---|---|
| Información corta o metadato | ✅ | |
| Información estructurada o compleja | | ✅ |
| Puede repetirse | | ✅ |
| Tiene subelementos | | ✅ |
| Afecta al significado del documento | | ✅ |
| Identificación o clasificación | ✅ | |
| Valor simple (fecha, número, código) | ✅ | |
| Se necesita orden o formato | | ✅ |

> [!tip] Regla práctica
> Los **atributos** (propiedades o metadatos) sirven para información **breve, identificativa y no estructurada**. Los **elementos** (contenido) representan el **contenido principal, estructurado o jerárquico**.

## Ver también

- [[Lenguajes de marcas/Ejercicios/UD1 - Ejemplos XML|Ejemplos XML]] — Biblioteca y Clínica resueltas
- [[_Índice Lenguajes de marcas]] — índice de la asignatura

---

← Volver a [[_Índice Lenguajes de marcas]]