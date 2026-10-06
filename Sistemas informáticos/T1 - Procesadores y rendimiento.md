---
tags:
  - sistemas-informaticos
  - tema1
  - hardware
  - cpu
  - rendimiento
asignatura: Sistemas informáticos
tema: 1
subtema: Procesadores y rendimiento
---

# T1 — Procesadores y rendimiento

Apuntes sobre cómo se calcula la velocidad de cómputo de un procesador (fuente: `Anexos/problemas_procesadores.pdf`). Completa [[T1 - Componentes hardware]].

## Definiciones y jerarquía

- **Arquitectura de Von Neumann**: modelo conceptual (años 40) de un computador con CPU (Unidad de Control + Unidad Aritmético-Lógica), una memoria única para datos e instrucciones, y dispositivos de E/S.
- **Microprocesador**: chip físico de silicio en la placa base; hoy actúa como contenedor principal de la CPU.
- **Núcleos (cores)**: unidades de procesamiento independientes dentro del microprocesador.

## ¿Cómo se relacionan?

- **Cada núcleo es una CPU completa**: posee su propia circuitería para ejecutar el ciclo completo de instrucción (captar, decodificar, ejecutar): una implementación en miniatura del modelo de Von Neumann.
- **De mono-núcleo a multi-núcleo**: antes un microprocesador albergaba un solo núcleo; hoy se colocan 2, 4, 8 o más para ganar potencia sin sobrecalentar el chip.
- **Trabajo compartido**: comparten la misma RAM externa y los mismos buses del sistema; cada núcleo puede ejecutar una tarea/hilo distinto simultáneamente.

## Cálculo de la velocidad de cómputo

### Límite teórico

```
Rendimiento Teórico Núcleo = Velocidad de reloj (GHz) × Operaciones por ciclo (IPC)
Rendimiento Teórico Total  = Rendimiento Teórico Núcleo × Nº de núcleos
```

- **Velocidad de reloj (GHz)**: miles de millones de ciclos por segundo (ej. 3,5 GHz = 3,5·10⁹ ciclos/s).
- **Operaciones por ciclo (IPC)**: instrucciones que resuelve en un único "tic" de reloj (depende de la arquitectura).
- **Núcleos**: un chip de 8 núcleos tiene, teóricamente, 8 veces la capacidad de uno de 1 núcleo a la misma velocidad.

### El "freno" de la realidad: la memoria caché

El rendimiento teórico nunca se alcanza al 100% por el **cuello de botella de Von Neumann** (el procesador es mucho más rápido que la RAM). La caché lo modifica mediante la **tasa de aciertos** (*Hit Rate*):

- **Cache Hit**: el dato está en la caché (1-2 ns) → rendimiento cercano al 100% teórico.
- **Cache Miss**: el núcleo va a la RAM externa (hasta 100× más lenta) → se queda "pausado" sin hacer nada; la velocidad real se desploma.

```
Rendimiento Real de Cómputo = Rendimiento Teórico Total × Eficiencia de la caché
```

> [!note] Eficiencia en tanto por uno
> Una eficiencia del 95% se introduce como `0,95` en la fórmula.

Una máquina con muchos núcleos y GHz pero caché pequeña pasará mucho tiempo esperando a la RAM: velocidad real baja. Una caché grande y rápida mantiene los núcleos "alimentados".

## Ciclo de reloj frente a IPC

- **Ciclo de reloj (el "tic")**: unidad de tiempo más pequeña del procesador (3 GHz = 3.000 millones de latidos/s).
- **IPC**: cantidad de trabajo que termina en cada latido. En CPUs actuales, **IPC > 1** (varias instrucciones por ciclo).

Duración de un ciclo (frecuencia):

```
Frecuencia = 1 / Velocidad de procesamiento   (en segundos)
```

## Velocidad real de ejecución de un programa

```
Tiempo de ejecución = Número de instrucciones del programa / Velocidad Real de Cómputo
```

Tres factores:

1. **Subir los GHz**: el metrónomo va más rápido, más "tics" por segundo.
2. **Mejorar la arquitectura (IPC)**: más instrucciones por tic (línea de montaje optimizada).
3. **El freno (caché/RAM)**: si la instrucción/dato no está en caché, la línea de montaje se detiene (*pipeline stall*): el reloj sigue latiendo (gasta energía y ciclos) pero el IPC cae a cero mientras espera a la RAM.

> [!important] Núcleos reales
> Al ejecutar un programa no siempre se dispone de todos los núcleos: normalmente está limitado a un número concreto. Hay que calcular la velocidad con el número de núcleos que **realmente** usa el programa.

## Escala de medidas (frecuencia)

| Unidad | Abrev. | Equivalencia | Contexto |
|---|---|---|---|
| Hercio | Hz | 1 ciclo/s | Velocidad puramente teórica |
| Megahercio | MHz | 1.000.000 Hz | Procesadores de los 80/90 (ej. Pentium 133 MHz) |
| Gigahercio | GHz | 1.000 MHz | Estándar actual: 2,5 – 5,5 GHz |

## Conclusiones (cómo elegir procesador)

- **Tareas pesadas** (vídeo, videojuegos, IA): pocos núcleos pero **mucha velocidad de reloj** (cada aplicación usa pocos núcleos; el resto quedaría ocioso).
- **Muchas tareas ligeras en paralelo** (ofimática, desarrollo de software): **muchos núcleos** con menos velocidad de reloj (no se necesita mucha potencia individual por aplicación).

## Ver también

- [[T1 - Componentes hardware]] — partes de la CPU, caché L1/L2/L3
- [[T1 - Memorias y velocidad de almacenamiento|Memorias y almacenamiento]] — escala MT/s y ancho de banda
- [[Sistemas informáticos/Ejercicios/T1 - Problemas de procesadores|Problemas de procesadores]] — ejercicios de rendimiento (pendientes)
- [[Sistemas informáticos/Ejercicios/T1 - Preguntas y respuestas Von Neumann|Preguntas y respuestas Von Neumann]]
- [[_Índice Sistemas informáticos|Índice de Sistemas informáticos]]

---

← Volver a [[_Índice Sistemas informáticos]]