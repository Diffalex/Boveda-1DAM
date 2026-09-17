---
tags:
  - guia
  - colaboracion
  - general
asignatura: general
---

# GUÍA DE CLASE — Cómo colaborar en los apuntes (1 DAM)

Bienvenido/a a la red de apuntes compartida de la clase. Aquí tienes todo lo que necesitas para **ver y editar** los apuntes desde tu propio Obsidian.

> [!important] Requisitos previos
> - Cuenta de **GitHub** (gratis): crea una en https://github.com/signup
> - **Git** instalado en tu equipo: https://git-scm.com/downloads
> - **Obsidian** instalado: https://obsidian.md/download
>
> Sin invitación del administrador no podrás acceder al repositorio.

---

## Paso 1 — Acepta la invitación

El administrador te invitará por email a colaborar en el repositorio `Boveda-1DAM`.

1. Abre el email de GitHub y pulsa en **"View invitation"**
2. Confirma la invitación (solo una vez)

---

## Paso 2 — Clona el repositorio

Abre un **terminal** (Windows: *PowerShell* o *Git Bash*; macOS/Linux: *Terminal*) y escribe:

```bash
git clone https://github.com/Diffalex/Boveda-1DAM.git
```

Esto descarga una copia de los apuntes en tu equipo, en una carpeta llamada `Boveda-1DAM`.

> [!tip] Si no sabes dónde estás
> El terminal se abre en tu carpeta de usuario. Para guardar los apuntes en una ruta concreta (por ejemplo el Escritorio):
> ```bash
> cd Escritorio        # Windows: cd OneDrive/Escritorio (o la que tengas)
> git clone https://github.com/Diffalex/Boveda-1DAM.git
> ```

---

## Paso 3 — Abre la bóveda en Obsidian

1. Abre Obsidian → **"Open folder as vault"** (Abrir carpeta como bóveda)
2. Selecciona la carpeta `Boveda-1DAM`
3. Verás la red de apuntes organizada por asignaturas:

```
00 - General/           → hub e índice principal de asignaturas
Programación/           → UD1 (identificadores, estructura, E/S, Scanner)
Sistemas informáticos/  → T1 (hardware, software, VirtualBox) y T2 (sistemas operativos)
Bases de datos/         → pendiente
Digitalización/         → pendiente
Entornos de desarrollo/ → pendiente
Lenguajes de marcas/    → pendiente
```

> [!tip] Vista de gráfico
> Pulsa **Ctrl+G** para ver la "red" de apuntes y las conexiones entre notas.

---

## Paso 4 — Instala el plugin "Obsidian Git"

Este plugin sincroniza los cambios de forma **semiautomática** (no es tiempo real): baja lo nuevo al abrir y sube tu trabajo periódicamente.

1. **Ajustes** ⚙️ (icono abajo a la izquierda) → **Comunidad / Community plugins**
2. Pulsa **Activar plugins de la comunidad** (Activate community plugins)
3. **Examinar** → busca **"Obsidian Git"** → **Instalar** → después **Activar** (Enable)

---

## Paso 5 — Configura Obsidian Git

Dentro de **Ajustes → Obsidian Git**:

| Ajuste | Valor |
|---|---|
| **Backup interval (minutes)** | `10` |
| **Auto backup after stopping file edits** | Activado |
| **Pull changes on startup** | Activado |
| **Pull changes on backup** | Activado |

Con esto, al abrir Obsidian bajará los cambios de todos, y cada 10 minutos subirá/actualizará los tuyos.

---

## Paso 6 — Subir y bajar cambios (rutina diaria)

| ¿Qué quieres hacer? | Cómo |
|---|---|
| **Bajar** los cambios de los demás | Automático (pull al abrir) o **Ctrl+P → "Obsidian Git: Pull"** |
| **Subir** tus apuntes | **Ctrl+P → "Obsidian Git: Push"** |
| Ver historial / deshacer un cambio | **Ctrl+P → "Obsidian Git: Open Source Control view"** |

---

## Reglas de oro para evitar conflictos

1. **Haz pull antes de empezar a editar** (o abre Obsidian y espera a que sincronice).
2. **Cada quien edita sus apuntes**: no toques notas que esté trabajando otro compañero a la vez.
3. **Sube pronto** (al terminar de escribir) y en **pedazos pequeños**.
4. Si dos personas editáis la misma nota al mismo tiempo, git avisará de un **conflicto**:

   ```
   <<<<<<< HEAD
   tu cambio
   =======
   el cambio del otro
   >>>>>>> origin/main
   ```

   Se resuelve quedándote con la versión correcta (borra los marcadores `<<<<<<<`, `=======` y `>>>>>>>`) y luego:
   ```bash
   git add nombre-de-la-nota.md
   git commit -m "Resuelto conflicto"
   git push
   ```

---

## Solución de problemas rápida

| Problema | Solución |
|---|---|
| `git clone` pide usuario y contraseña | Introduce tu **usuario de GitHub** y como contraseña un **Personal Access Token** (https://github.com/settings/tokens → *Generate new token* → marca *repo* / *Contents: Read and write*) |
| *"Permission denied"* al hacer push | No has aceptado la invitación, o tu token no tiene permisos. Repasa el Paso 1 |
| *"repository not found"* al clonar | Confirma el nombre exacto: `Diffalex/Boveda-1DAM` y que has aceptado la invitación |
| Obsidian Git marca error de autenticación | En Windows usa **Git Credential Manager**; en Linux/macOS vuelve a hacer login de git con el token |

---

## Estructura y convenciones (para los que creen apuntes)

- **Cada asignatura es una carpeta**; cada tema/unidad, un archivo `.md`.
- Los **índices** (`_Índice Nombre.md`) enlazan a las notas de esa asignatura.
- Los nombres llevan prefijo de orden: `UD1 -`, `T1 -`, `T2 -`...
- Las notas enlazan entre sí con `[[Nombre de la nota]]`.
- Cada nota empieza con metadatos (tags) para colorearlas en el gráfico.

---

## ANEXO — Instala y configura Obsidian igual que el administrador

Para que **tu Obsidian quede exactamente igual** que el del administrador (vista de archivos, red de enlaces, paneles laterales), sigue esta guía la primera vez.

### 1. Descarga e instala Obsidian

| Sistema | Cómo |
|---|---|
| **Windows** | Descarga el instalador `.exe` de https://obsidian.md/download e instala |
| **macOS** | Descarga el `.dmg`, arrastra Obsidian a *Aplicaciones* |
| **Linux** | Descarga el `.AppImage` (o paquete `.deb`/.rpm según tu distribución), dale permisos de ejecución y ábrelo |
| **Móvil** | Google Play / App Store (también funciona, pero la edición con git es más fácil desde el ordenador) |

### 2. Abre la bóveda (una sola vez)

- Al abrir Obsidian → **"Open folder as vault"** → selecciona la carpeta `Boveda-1DAM`
- Acepta la opción de *Trust author and enable plugins* si te la ofrece

### 3. Activa los paneles y vistas

Obsidian del administrador tiene estos paneles **a la derecha** (iconos de la barra lateral derecha, o **Ctrl + click** en el icono):

1. **Enlaces entrantes** (flechas llegando) — muestra qué notas enlazan a la actual
2. **Enlaces salientes** (flechas saliendo) — muestra a dónde enlaza la nota actual
3. **Etiquetas** (`#`) — todas las etiquetas de la bóveda
4. **Propiedades** (ficha) — metadatos de cada nota
5. **Esquema** (lista) — índice de secciones de la nota activa

Y a la **izquierda**:
1. **Explorador de archivos** (carpeta) — el árbol de la bóveda
2. **Buscar** (lupa)
3. **Marcadores** (estrella) — notas favoritas

> [!tip] Si no ves la barra lateral derecha
> Se activa pulsando el icono de **panel lateral derecho** en la barra superior, o con el atajo de tu sistema (en Windows/Linux: **Ctrl+P** → *"Toggle right sidebar"*).

### 4. Activa los plugins principales (si están deshabilitados)

**Ajustes ⚙️ → Plugins principales (Core plugins)**. Los que usa la bóveda:

- **Vista de gráfico** (Graph view) — la red de apuntes
- **Enlaces entrantes** (Backlinks)
- **Enlaces salientes** (Outgoing links)
- **Etiquetas** (Tag pane)
- **Propiedades** (Properties)
- **Esquema** (Outline)
- **Paleta de comandos** (Command palette)
- **Cambiador rápido** (Quick switcher)
- **Búsqueda global** (Global search)
- **Marcadores** (Bookmarks)

### 5. Dales una vuelta con los atajos clave

| Atajo (Win/Linux) | Atajo (macOS) | Acción |
|---|---|---|
| **Ctrl+G** | Cmd+G | Abrir la **Vista de gráfico** (la "red" de apuntes) |
| **Ctrl+O** | Cmd+O | Cambiador rápido (navegar entre notas) |
| **Ctrl+P** | Cmd+P | Paleta de comandos (p. ej. "Obsidian Git: Push") |
| **Ctrl+E** | Cmd+E | Alternar modo editor / vista previa |
| **Ctrl+Click** en un enlace | Cmd+Click | Abrir la nota enlazada en una pestaña nueva |

### 6. Colorea el gráfico por asignatura (opcional, igual que el admin)

1. Desde **Ctrl+G**, pulsa el icono de **filtrar/grupos** de color (paleta)
2. **Grupos de color → Agregar grupo**
3. Añade uno por asignatura, por ejemplo:
   - `tag:#sistemas-informaticos` → color azul
   - `tag:#programacion` → color verde
   - `tag:#bases-de-datos`, `tag:#digitalizacion`, `tag:#entornos-de-desarrollo`, `tag:#lenguajes-de-marcas`

Cada nota ya lleva sus etiquetas en los metadatos, por lo que los colores se aplican solos.

---

← Volver a [[Asignaturas 1 DAM]]