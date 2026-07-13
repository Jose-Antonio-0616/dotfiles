# Manual de Yazi File Manager - Kael OS

Yazi es un administrador de archivos basado en terminal (TUI) ultra rápido escrito en Rust. Utiliza un diseño de 3 columnas (directorio padre, directorio actual y previsualización).

---

## 📂 Archivos de Configuración
*   **Configuración General:** [`~/.config/yazi/yazi.toml`](file:///home/jose/.config/yazi/yazi.toml) (Configura previsualización de imágenes Kitty y visibilidad de archivos ocultos).
*   **Tema de Colores:** [`~/.config/yazi/theme.toml`](file:///home/jose/.config/yazi/theme.toml) (Tema Cyber-Rasta integrado).

---

## ⌨️ Atajos de Teclado Fundamentales

### 1. Navegación Básica
*   `j` / `k` o Flechas Abajo/Arriba → Moverse por la lista de archivos.
*   `h` / `l` o Flechas Izquierda/Derecha → Entrar en carpeta / Salir a carpeta padre.
*   `g` + `g` → Ir al principio de la lista.
*   `G` → Ir al final de la lista.
*   `.` / `~` → Mostrar u ocultar archivos ocultos (dotfiles).

### 2. Saltos Rápidos (Go to)
*   `g` + `h` → Ir a tu directorio personal (`~`).
*   `g` + `c` → Ir a tu directorio de configuración (`~/.config`).
*   `g` + `d` → Ir a `~/Downloads`.
*   `g` + `m` → Ir a `/media/` (montajes externos).

### 3. Operaciones de Archivos
*   `Enter` → Abrir archivo (ejecuta Neovim para texto, MPV para multimedia, xdg-open para PDFs/imágenes).
*   `Space` → Seleccionar/Deseleccionar archivo individual.
*   `v` → Activar modo de selección visual.
*   `c` → Copiar archivo(s) al portapapeles de Yazi.
*   `x` → Cortar archivo(s).
*   `p` → Pegar archivos copiados/cortados.
*   `d` → Eliminar archivos (solicita confirmación).
*   `r` → Renombrar archivo.
*   `a` → Crear nuevo archivo o carpeta (añadir barra `/` al final para crear carpeta).

### 4. Búsqueda y Filtrado
*   `/` → Buscar archivos dinámicamente en el directorio actual.
*   `f` → Buscar archivos en subdirectorios usando `fd` / `fzf`.
*   `Ctrl + s` → Buscar texto dentro de archivos usando `ripgrep` (rg).
