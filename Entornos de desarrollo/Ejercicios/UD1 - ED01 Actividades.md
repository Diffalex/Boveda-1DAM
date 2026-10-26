---
tags:
  - entornos-de-desarrollo
  - ud1
  - actividades
  - resuelto
  - software
  - ciclo-vida
  - metodologias-agiles
  - lenguajes
asignatura: Entornos de desarrollo
unidad: UD1
tema: ED01 Actividades resueltas
---

# UD1 — ED01. Actividades resueltas

Cuestionario de la Unidad 01 — Desarrollo de Software. Las respuestas de los bloques **I** y **III** proceden de la entrega `Anexos/ED01_Act01_EscobarValero_Alejandro.pdf`; el bloque **II** se completa como apoyo a partir de los enunciados y la teoría de [[UD1 - Desarrollo de software|UD1 — Desarrollo de software]].

> [!success] Estado
> Actividades resueltas. La teoría ampliada está en [[UD1 - Desarrollo de software|UD1 — Desarrollo de software]].

## I. Actividades de Introducción

**1. Haz una clasificación del software.**

- **Software de sistema:** gestiona el hardware y sirve de base al resto. Ejemplos: sistemas operativos (Windows, Linux), controladores y utilidades.
- **Software de programación:** herramientas para crear programas. Ejemplos: compiladores, intérpretes, editores de código e IDE.
- **Software de aplicación:** programas que usa el usuario para tareas concretas. Ejemplos: navegadores, ofimática, videojuegos, WhatsApp.

**2. Describe la relación entre los componentes hardware principales de un computador y el almacenamiento y ejecución del software.**

El software se guarda de forma permanente en el **almacenamiento secundario** (disco duro o SSD). Para ejecutarlo, el sistema lo carga en la **memoria RAM** y la **CPU** va leyendo y ejecutando sus instrucciones una a una. Los dispositivos de **entrada/salida** permiten la comunicación con el usuario. En resumen: el hardware almacena, carga y ejecuta el software; el software le dice al hardware qué hacer.

**3. Define código fuente, código objeto y código ejecutable.**

- **Código fuente:** programa escrito por el programador en un lenguaje de alto nivel (C, Java, Python...). Es legible por humanos y no se puede ejecutar directamente.
- **Código objeto:** resultado de compilar el código fuente. Ya está en lenguaje máquina o intermedio, pero todavía no se puede ejecutar porque tiene referencias sin resolver.
- **Código ejecutable:** código objeto que ha pasado por el enlazador (*linker*), quedando como programa final listo para ejecutarse.

## II. Actividades de Ciclo de vida del software

**4. Define “ciclo de vida del software”.**

Es el conjunto de fases por las que pasa un programa desde que se plantea su necesidad hasta que se retira: análisis, diseño, codificación, pruebas, despliegue y mantenimiento.

**5. Nombra las fases principales del desarrollo de software y explica brevemente qué se hace en cada una.**

| Fase | Qué se hace |
|---|---|
| **Análisis de requisitos** | Recoger y definir qué debe hacer el sistema |
| **Diseño** | Decidir arquitectura, módulos, interfaces y datos |
| **Codificación** | Escribir el código fuente |
| **Pruebas** | Comprobar que funciona y cumple los requisitos |
| **Despliegue** | Instalar y poner el sistema en producción |
| **Mantenimiento** | Corregir errores, adaptar y mejorar el sistema |

**6. Explica brevemente en qué consiste el modelo en cascada.**

Es un modelo **secuencial**: cada fase empieza cuando termina la anterior. Primero se analizan los requisitos, luego se diseña, se codifica, se prueba, se despliega y se mantiene. Se documenta mucho y se planifica con antelación.

**7. Ventajas e inconvenientes del modelo en cascada.**

- **Ventajas:** es sencillo de entender y planificar, genera documentación abundante y los costes son previsibles si los requisitos son estables.
- **Inconvenientes:** es poco flexible ante cambios, el cliente ve el resultado muy tarde y un error detectado en una fase avanzada es caro de corregir.

**8. ¿Qué se entiende por verificación? ¿Y por validación?**

- **Verificación:** comprobar que el producto se está construyendo **correctamente**, conforme a las especificaciones y al diseño. *¿Estamos construyendo bien el producto?*
- **Validación:** comprobar que se está construyendo **el producto correcto**, que satisface las necesidades reales del usuario. *¿Estamos construyendo el producto correcto?*

**9. Explica cómo funciona el modelo de desarrollo mediante creación de prototipos.**

Se construye una **versión rápida y simplificada** del sistema para que el usuario la pruebe y dé feedback. Con sus respuestas se aclaran requisitos y se corrige el rumbo. El prototipo puede desecharse o evolucionar hasta el producto final. Su riesgo principal es que el usuario lo confunda con el producto terminado.

**10. Explica cómo funciona el modelo espiral aplicado al desarrollo orientado a objetos.**

Es un modelo **iterativo y basado en riesgos**. Cada vuelta de la espiral tiene cuatro cuadrantes: determinar objetivos y alternativas, analizar y resolver riesgos, desarrollar y verificar, y planificar la siguiente iteración. En cada vuelta se aplican técnicas orientadas a objetos y se revisan los riesgos antes de continuar.

**11. ¿Qué cuatro principios rigen el desarrollo ágil expresados en el Manifiesto Ágil?**

El Manifiesto Ágil establece **cuatro valores**:

1. **Individuos e interacciones** sobre procesos y herramientas.
2. **Software funcionando** sobre documentación exhaustiva.
3. **Colaboración con el cliente** sobre negociación contractual.
4. **Respuesta ante el cambio** sobre seguir un plan rígido.

> [!note] Matiz
> El enunciado habla de “cuatro principios”, pero el Manifiesto los formula como **valores**. Además, incluye **12 principios** que desarrollan estas ideas.

**12. ¿Qué es una historia de usuario?**

Es una descripción breve de una necesidad desde el punto de vista del usuario, con el formato:

> Como **[rol]**, quiero **[funcionalidad]** para **[beneficio]**.

Se completa con **criterios de aceptación** y debe ser pequeña, comprensible y verificable. Se recomienda que cumpla **INVEST**: independiente, negociable, valiosa, estimable, pequeña y testeable.

**13. Resumen de Lean software y sus principios.**

**Lean** busca eliminar todo lo que no aporta valor al cliente. Sus siete principios son: eliminar desperdicios, amplificar el aprendizaje, decidir lo más tarde posible, entregar lo más rápido posible, empoderar al equipo, construir integridad y ver el conjunto.

**14. KANBAN: ventajas e inconvenientes de una pizarra web digital.**

- **Ventajas:** acceso desde cualquier lugar y equipo, actualización en tiempo real, historial y métricas automáticas, e integración con repositorios y CI.
- **Inconvenientes:** dependencia de conexión y herramientas, exceso de notificaciones, curva de aprendizaje y coste según la herramienta. Además, resulta menos “táctil” que una pizarra física.

**15. KANBAN: resumen de la metodología y diferencias frente a SCRUM.**

Kanban es un sistema visual de gestión del flujo: se visualizan las tareas en columnas, se limita el trabajo en curso (WIP), se gestionan las políticas y se mide el tiempo de ciclo.

| Aspecto | Kanban | Scrum |
|---|---|---|
| **Cadencia** | Flujo continuo | Sprints de duración fija |
| **Cambios** | Se pueden introducir en cualquier momento | Se evitan durante el sprint |
| **Roles** | No prescribe roles | Product Owner, Scrum Master y equipo |
| **Límite de trabajo** | Límites WIP explícitos | Compromiso del sprint |
| **Métricas** | Tiempo de ciclo y rendimiento | Velocidad del equipo |
| **Reuniones** | Opcionales | Planificación, daily, review y retrospectiva |

**16. SCRUM: explica cómo funciona.**

Scrum trabaja en **sprints** de 2-4 semanas. El **Product Owner** prioriza el Product Backlog; el equipo elige tareas para el Sprint Backlog en la **Sprint Planning**. Cada día se hace un **Daily Scrum** de 15 minutos. Al final del sprint se entrega un incremento y se revisa en la **Sprint Review**; después, en la **Sprint Retrospective**, el equipo analiza cómo mejorar.

**17. SCRUM: define Product backlog y Sprint backlog.**

- **Product Backlog:** lista priorizada de todo lo que podría necesitar el producto (funcionalidades, mejoras, correcciones). La mantiene el Product Owner.
- **Sprint Backlog:** subconjunto de tareas elegidas para el sprint actual, con el plan para completarlas.

**18. SCRUM: sinónimos de jefe de proyecto, cliente y equipo de desarrollo.**

- **Jefe de proyecto** ≈ **Product Owner** (responsable de maximizar el valor).
- **Cliente** ≈ **stakeholders** o el propio **Product Owner** como representante.
- **Equipo de desarrollo** = **Development Team** (equipo autoorganizado y transversal).

**19. SCRUM: resumen de los requisitos para usarlo.**

Requiere un equipo **transversal y autoorganizado**, compromiso con la transparencia y la inspección, una **Definition of Done** acordada, disponibilidad del Product Owner y capacidad de entregar un incremento funcional al final de cada sprint.

**20. XP: explica los 5 valores de la Programación Extrema.**

1. **Comunicación:** todo el equipo y el cliente hablan con claridad.
2. **Simplicidad:** se implementa lo mínimo que funciona.
3. **Feedback:** pruebas y entregas cortas para corregir pronto.
4. **Coraje:** atreverse a refactorizar y a cambiar lo que no funciona.
5. **Respeto:** relaciones sanas y reconocimiento del trabajo del equipo.

**21. XP: características distintivas frente a otras metodologías ágiles.**

XP destaca por su **intensidad técnica**: programación en pareja, TDD, integración continua, refactorización, propiedad colectiva del código, entregas pequeñas, cliente en el equipo, juego de la planificación, diseño simple y estándares de codificación. Es más prescriptiva en las prácticas de ingeniería que Scrum o Kanban.

## III. Actividades de Lenguajes de Programación

**22. Diferencias entre lenguajes imperativos y declarativos. Nombra al menos 2 de cada tipo.**

- **Imperativos:** indican **cómo** resolver el problema, paso a paso, mediante una secuencia de instrucciones y estado. Ejemplos: **C** y **Java**.
- **Declarativos:** indican **qué** resultado queremos, sin especificar los pasos. Ejemplos: **SQL** y **Prolog**.

**23. Explica qué es compilar y qué es interpretar.**

- **Compilar:** traducir todo el código fuente a código máquina u objeto de una sola vez mediante un compilador, generando un ejecutable.
- **Interpretar:** un intérprete va leyendo y ejecutando el código fuente instrucción por instrucción en tiempo de ejecución.

**24. Ventajas de los lenguajes compilados.**

- Se ejecutan más rápido, porque ya están traducidos.
- Se puede distribuir el programa sin entregar el código fuente.
- Los errores se detectan al compilar.
- El equipo destino no necesita el compilador.

**25. Ventajas de los lenguajes interpretados.**

- Son más portables: solo necesitan el intérprete.
- Permiten ejecución inmediata, sin esperar a compilar.
- Son más fáciles de depurar y modificar.

**26. Nombra 2 lenguajes compilados y otros 2 interpretados.**

- **Compilados:** C y C++.
- **Interpretados:** Python y JavaScript.

**27. ¿Puede considerarse código objeto el bytecode generado en Java tras la compilación? Explica la respuesta.**

Sí. Es el resultado de compilar el código fuente con `javac`, pero no es código máquina nativo del procesador: es un **código intermedio portable** que ejecuta la **JVM** (interpretándolo o compilándolo con JIT). Por eso también se llama código intermedio.

**28. Pon un ejemplo de lenguaje de bajo nivel, nivel medio y alto nivel.**

- **Bajo nivel:** ensamblador (ASM).
- **Nivel medio:** C.
- **Alto nivel:** Python.

**29. ¿Qué paradigma de programación siguen C, C++, SQL, Java, JavaScript, Lisp y Prolog?**

- **C:** imperativo/estructurado.
- **C++:** multiparadigma (imperativo, orientado a objetos y genérico).
- **SQL:** declarativo.
- **Java:** orientado a objetos (con base imperativa).
- **JavaScript:** multiparadigma (imperativo, orientado a objetos y funcional).
- **Lisp:** funcional (declarativo).
- **Prolog:** lógico (declarativo).

**30. Criterios para elegir un lenguaje de programación en un proyecto.**

- Tipo de proyecto: web, móvil, escritorio, sistemas, datos, videojuegos.
- Rendimiento y consumo de recursos.
- Portabilidad entre plataformas.
- Librerías, frameworks y ecosistema disponible.
- Experiencia del equipo y facilidad de aprendizaje.
- Comunidad, soporte y documentación.
- Coste, licencia y herramientas (IDE, depurador).
- Demanda del mercado laboral.

## Ver también

- [[UD1 - Desarrollo de software|UD1 — Desarrollo de software]] — teoría completa
- [[Entornos de desarrollo/Ejercicios/UD1 - Práctica 01 (compilación vs interpretación)|Práctica 01 — Compilación vs interpretación]]
- [[Entornos de desarrollo/Ejercicios/UD1 - Práctica 01 (IntelliJ)|Práctica 01 — IntelliJ]]
- [[UD1 - Cuestiones previas|Cuestiones previas]]
- [[_Índice Entornos de desarrollo]]

---

← Volver a [[_Índice Entornos de desarrollo]]
