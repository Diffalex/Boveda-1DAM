---
tags:
  - entornos-de-desarrollo
  - ud1
  - desarrollo-software
  - ciclo-vida
  - metodologias-agiles
  - scrum
  - kanban
  - xp
  - lenguajes
asignatura: Entornos de desarrollo
unidad: UD1
tema: Desarrollo de software
---

# UD1 — Desarrollo de software

Teoría de la Unidad 1 a partir de los enunciados `ED01 - Actividades Ud01..docx` y `ED01 - Actividades01 - Introducción y lenguajes.docx`, y de la entrega resuelta `Anexos/ED01_Act01_EscobarValero_Alejandro.pdf`.

> [!info] Contenido
> 1. Software, hardware y código
> 2. Ciclo de vida del software
> 3. Modelos de desarrollo
> 4. Metodologías ágiles
> 5. Lenguajes de programación

## Software, hardware y código

El **software** es el conjunto de programas, datos e instrucciones que permiten al hardware realizar tareas. Se clasifica en tres grandes grupos:

| Tipo | Función | Ejemplos |
|---|---|---|
| **Software de sistema** | Gestiona el hardware y sirve de base al resto | Sistemas operativos, controladores, utilidades |
| **Software de programación** | Herramientas para crear programas | Compiladores, intérpretes, editores, IDE |
| **Software de aplicación** | Programas para tareas concretas del usuario | Navegadores, ofimática, videojuegos, WhatsApp |

### Relación entre hardware y software

1. El software se almacena de forma permanente en el **almacenamiento secundario** (disco duro o SSD).
2. Al ejecutarlo, el sistema lo carga en la **memoria RAM**.
3. La **CPU** lee y ejecuta sus instrucciones.
4. Los dispositivos de **entrada/salida** permiten la comunicación con el usuario.

En resumen: el hardware **almacena, carga y ejecuta**; el software **indica qué hacer**.

### Código fuente, objeto y ejecutable

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Código fuente** | Programa escrito por el programador en un lenguaje de alto nivel; legible por humanos | `suma.c`, `Suma.java`, `suma.py` |
| **Código objeto** | Resultado de compilar el fuente; en lenguaje máquina o intermedio, con referencias pendientes | `suma.o`, `Suma.class` |
| **Código ejecutable** | Código objeto enlazado y listo para ejecutarse | `suma`, `suma.exe`, `Suma.jar` |

> [!note] Java y el bytecode
> `javac` traduce `Suma.java` a `Suma.class`, un **bytecode** portable. No es código máquina nativo: lo ejecuta la **JVM**, que lo interpreta o lo compila con **JIT**. Puede considerarse código objeto/intermedio.

## Ciclo de vida del software

El **ciclo de vida del software** es el conjunto de fases por las que pasa un programa desde que se plantea su necesidad hasta que se retira.

| Fase | Qué se hace |
|---|---|
| **Análisis de requisitos** | Recoger y definir qué debe hacer el sistema |
| **Diseño** | Decidir arquitectura, módulos, interfaces y datos |
| **Codificación** | Escribir el código fuente |
| **Pruebas** | Comprobar que funciona y cumple los requisitos |
| **Despliegue** | Instalar y poner el sistema en producción |
| **Mantenimiento** | Corregir errores, adaptar y mejorar el sistema |

### Verificación y validación

| Concepto | Pregunta | Qué comprueba |
|---|---|---|
| **Verificación** | ¿Estamos construyendo bien el producto? | Que cumple especificaciones y diseño |
| **Validación** | ¿Estamos construyendo el producto correcto? | Que satisface las necesidades del usuario |

> [!important] No son lo mismo
> Un programa puede estar **verificado** (cumple lo especificado) y no ser **válido** (no resuelve el problema real). Lo ideal es cumplir ambas.

## Modelos de desarrollo

### Modelo en cascada

Las fases se realizan **en secuencia**: cada una empieza cuando termina la anterior. Es rígido y documentado.

| Ventajas | Inconvenientes |
|---|---|
| Sencillo de entender y planificar | Poco flexible ante cambios |
| Documentación abundante | El cliente ve el resultado muy tarde |
| Costes previsibles si los requisitos son estables | Un error detectado tarde es caro de corregir |

Es adecuado para proyectos con requisitos **estables y bien definidos**.

### Desarrollo mediante prototipos

Se construye una **versión rápida y simplificada** para que el usuario la pruebe y dé feedback. El prototipo se puede desechar o evolucionar hasta el producto final.

- **Ventaja:** detecta malentendidos y requisitos ocultos pronto.
- **Riesgo:** el usuario puede confundir el prototipo con el producto terminado.

### Modelo espiral

Combina iteraciones con **análisis de riesgos**. Cada vuelta de la espiral tiene cuatro cuadrantes:

1. Determinar objetivos y alternativas.
2. Analizar y resolver riesgos.
3. Desarrollar y verificar.
4. Planificar la siguiente iteración.

Es útil en proyectos **grandes o con riesgos altos**, pero puede ser costoso y complejo.

## Metodologías ágiles

Las metodologías ágiles priorizan la **entrega frecuente de software funcional**, la colaboración con el cliente y la adaptación al cambio.

### Manifiesto Ágil

El Manifiesto Ágil establece **cuatro valores** (el enunciado los llama “principios”):

| Se valora más | Que |
|---|---|
| **Individuos e interacciones** | Procesos y herramientas |
| **Software funcionando** | Documentación exhaustiva |
| **Colaboración con el cliente** | Negociación contractual |
| **Respuesta ante el cambio** | Seguir un plan rígido |

> [!note] Doce principios
> Además de los cuatro valores, el Manifiesto incluye **12 principios**: entrega temprana y continua, bienvenida al cambio, entregas frecuentes, colaboración negocio-desarrollo, motivación del equipo, comunicación cara a cara, software como medida de progreso, ritmo sostenible, excelencia técnica, simplicidad, equipos autoorganizados y reflexión para mejorar.

### Historias de usuario

Una **historia de usuario** describe una necesidad desde el punto de vista del usuario:

> Como **[rol]**, quiero **[funcionalidad]** para **[beneficio]**.

Debe ser pequeña, comprensible y verificable. Se suele completar con **criterios de aceptación** y se recomienda que cumpla **INVEST**: independiente, negociable, valiosa, estimable, pequeña y testeable.

### Lean software

**Lean** busca eliminar todo lo que no aporta valor al cliente. Sus siete principios:

1. Eliminar desperdicios.
2. Amplificar el aprendizaje.
3. Decidir lo más tarde posible.
4. Entregar lo más rápido posible.
5. Empoderar al equipo.
6. Construir integridad.
7. Ver el conjunto, no solo las partes.

### Kanban

**Kanban** es un sistema visual de gestión del flujo de trabajo. Prácticas clave:

- Visualizar las tareas en un tablero (por ejemplo: Pendiente, En curso, Hecho).
- Limitar el **trabajo en curso (WIP)**.
- Gestionar el flujo y medir el tiempo de ciclo.
- Hacer explícitas las políticas.
- Usar bucles de feedback.
- Mejorar de forma colaborativa.

| Ventajas de una pizarra digital | Inconvenientes |
|---|---|
| Acceso desde cualquier lugar y equipo | Depende de conexión y herramientas |
| Actualización en tiempo real | Puede generar exceso de notificaciones |
| Historial y métricas automáticas | Curva de aprendizaje y coste según herramienta |
| Integración con repositorios y CI | Menos “táctil” que una pizarra física |

#### Kanban frente a Scrum

| Aspecto | Kanban | Scrum |
|---|---|---|
| **Cadencia** | Flujo continuo | Sprints de duración fija |
| **Cambios** | Se pueden introducir en cualquier momento | Se evitan durante el sprint |
| **Roles** | No prescribe roles | Product Owner, Scrum Master y equipo |
| **Límite de trabajo** | Límites WIP explícitos | Compromiso del sprint |
| **Métricas** | Tiempo de ciclo y rendimiento | Velocidad del equipo |
| **Reuniones** | Opcionales | Planificación, daily, review y retrospectiva |

### Scrum

**Scrum** es un marco ágil basado en iteraciones cortas llamadas **sprints** (normalmente 2-4 semanas).

| Elemento | Componentes |
|---|---|
| **Roles** | Product Owner, Scrum Master, equipo de desarrollo |
| **Artefactos** | Product Backlog, Sprint Backlog, Incremento |
| **Eventos** | Sprint Planning, Daily Scrum (15 min), Sprint Review, Sprint Retrospective |

- El **Product Backlog** es la lista priorizada de todo lo que podría necesitar el producto.
- El **Sprint Backlog** contiene las tareas elegidas para el sprint actual.
- Sinónimos habituales: *jefe de proyecto* ≈ **Product Owner**; *cliente* ≈ **stakeholders/Product Owner**; *equipo de desarrollo* = **Development Team**.
- Requisitos: equipo **transversal y autoorganizado**, compromiso, transparencia, inspección y adaptación, y una **Definition of Done** acordada.

### XP (Programación Extrema)

XP es una metodología ágil centrada en la calidad técnica y en ciclos muy cortos. Sus **cinco valores** son:

1. **Comunicación**
2. **Simplicidad**
3. **Feedback**
4. **Coraje**
5. **Respeto**

Prácticas características: **programación en pareja**, **TDD** (desarrollo guiado por pruebas), **integración continua**, **refactorización**, **propiedad colectiva del código**, **entregas pequeñas**, **cliente en el equipo**, **juego de la planificación**, **diseño simple** y **estándares de codificación**.

## Lenguajes de programación

### Imperativos y declarativos

| Estilo | Cómo describe el programa | Ejemplos |
|---|---|---|
| **Imperativo** | Indica **cómo** resolverlo: secuencia de instrucciones y estado | C, Java, Python, Pascal |
| **Declarativo** | Indica **qué** se quiere obtener, sin detallar los pasos | SQL, Prolog, Lisp funcional |

> [!note] Matices
> Muchos lenguajes son **multiparadigma**: Python, JavaScript o C++ combinan estilos. La clasificación indica el paradigma principal, no una jaula.

### Compilar e interpretar

| Aspecto | Compilado | Interpretado |
|---|---|---|
| **Traducción** | Todo el programa antes de ejecutarse | Instrucción a instrucción durante la ejecución |
| **Resultado** | Código objeto y ejecutable | No genera ejecutable; usa un intérprete |
| **Velocidad** | Normalmente mayor | Normalmente menor |
| **Errores** | Se detectan al compilar | Aparecen durante la ejecución |
| **Portabilidad** | Depende de la plataforma | Basta con tener el intérprete |
| **Ejemplos** | C, C++, Rust, Go | Python, JavaScript, Ruby |

**Ventajas de los compilados:** rendimiento, distribución sin fuente, detección temprana de errores y equipo destino sin compilador.
**Ventajas de los interpretados:** portabilidad, ejecución inmediata, depuración y modificación más sencillas.

### Java: bytecode y JVM

1. `javac Suma.java` genera `Suma.class` (**bytecode**).
2. `java Suma` arranca la **JVM**, que ejecuta el bytecode.
3. La JVM puede **interpretar** o **compilar con JIT** las partes calientes.
4. El bytecode es portable; el mismo `.class` funciona en cualquier equipo con una JVM compatible.

### Niveles de lenguaje

| Nivel | Característica | Ejemplo |
|---|---|---|
| **Bajo nivel** | Muy cercano a la máquina; instrucciones y registros | Lenguaje máquina, ensamblador |
| **Nivel medio** | Acceso a memoria y bajo nivel, pero más legible | C |
| **Alto nivel** | Abstracción de la máquina; más productivo | Python, Java, JavaScript |

### Paradigmas

| Lenguaje | Paradigma principal |
|---|---|
| **C** | Imperativo/estructurado |
| **C++** | Multiparadigma: imperativo, orientado a objetos y genérico |
| **SQL** | Declarativo |
| **Java** | Orientado a objetos (con base imperativa) |
| **JavaScript** | Multiparadigma: imperativo, orientado a objetos y funcional |
| **Lisp** | Funcional (declarativo) |
| **Prolog** | Lógico (declarativo) |

### Criterios para elegir un lenguaje

- Tipo de proyecto: web, móvil, escritorio, sistemas, datos, videojuegos.
- Rendimiento y consumo de recursos.
- Portabilidad entre sistemas operativos.
- Librerías, frameworks y ecosistema.
- Experiencia del equipo y facilidad de aprendizaje.
- Comunidad, soporte y documentación.
- Coste, licencia y herramientas (IDE, depurador).
- Salida laboral y demanda del mercado.

## Ver también

- [[Entornos de desarrollo/Ejercicios/UD1 - ED01 Actividades|ED01 — Actividades resueltas]] — respuestas del cuestionario
- [[Entornos de desarrollo/Ejercicios/UD1 - Práctica 01 (compilación vs interpretación)|Práctica 01 — Compilación vs interpretación]]
- [[Entornos de desarrollo/Ejercicios/UD1 - Práctica 01 (IntelliJ)|Práctica 01 — IntelliJ: fuente, objeto y ejecutable]]
- [[UD1 - Cuestiones previas|Cuestiones previas]]
- [[_Índice Entornos de desarrollo]]

---

← Volver a [[_Índice Entornos de desarrollo]]
