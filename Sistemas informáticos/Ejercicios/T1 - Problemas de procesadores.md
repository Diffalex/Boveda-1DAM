---
tags:
  - sistemas-informaticos
  - tema1
  - ejercicios
  - cpu
  - rendimiento
asignatura: Sistemas informáticos
tema: 1
tipo: ejercicios
---

# T1 — Problemas de procesadores

**Pendiente.** Tres problemas de cálculo de rendimiento de microprocesadores. Teoría en [[T1 - Procesadores y rendimiento]] (fuente: `Anexos/problemas_procesadores.pdf`).

Fórmulas a usar:

```
Rendimiento Teórico Núcleo = Velocidad de reloj (GHz) × Operaciones por ciclo (IPC)
Rendimiento Teórico Total  = Rendimiento Teórico Núcleo × Nº de núcleos
Frecuencia                 = 1 / Velocidad de procesamiento   (segundos)
Rendimiento Real           = Rendimiento Teórico Total × Eficiencia de la caché
Tiempo de ejecución        = Nº de instrucciones / Velocidad Real de Cómputo
```

> [!note] Eficiencia de caché
> La eficiencia se da como porcentaje (ej. 95% → `0,95`). Si no se indica, se asume un valor a concretar en clase.

## Problema 1 — Microprocesador M1

- 6 núcleos
- Velocidad de reloj por núcleo: 3 GHz
- IPC: 1,5

Calcula:
- a) Rendimiento teórico por núcleo.
- b) Rendimiento teórico total.
- c) Frecuencia de cada ciclo de reloj.
- d) Rendimiento real del microprocesador en su conjunto.

## Problema 2 — Microprocesador M2

- 12 núcleos
- Velocidad de reloj por núcleo: 2 GHz
- IPC: 1,5

Calcula:
- a) Rendimiento teórico por núcleo.
- b) Rendimiento teórico total.
- c) Frecuencia de cada ciclo de reloj.
- d) Rendimiento real del microprocesador en su conjunto.

## Problema 3 — Ejecución de un programa

Se desea ejecutar un programa de **3 mil millones de instrucciones** en ambos equipos (M1 y M2):

- a) Determina el **tiempo de ejecución real** en cada equipo.
- b) Si el programa solo puede disponer de **dos núcleos**, ¿en cuál de los dos tarda menos? Razona la respuesta.

## Ver también

- [[T1 - Procesadores y rendimiento|Procesadores y rendimiento]] — teoría de las fórmulas
- [[T1 - Componentes hardware|Componentes hardware]] — CPU y caché
- [[_Índice Sistemas informáticos|Índice de Sistemas informáticos]]

---

← Volver a [[_Índice Sistemas informáticos]]