# Manual de Lazygit - Kael OS

Lazygit es una interfaz de terminal interactiva (TUI) para Git escrita en Go. Permite gestionar confirmaciones, ramas, fusiones y conflictos de manera visual y rápida.

---

## 📂 Archivos de Configuración
*   **Configuración General:** [`~/.config/lazygit/config.yml`](file:///home/jose/.config/lazygit/config.yml) (Tema Cyber-Rasta integrado).

---

## 🖥️ Estructura de Paneles
La pantalla está dividida en 5 paneles numerados de izquierda a derecha y de arriba a abajo:
1.  **Status**: Estado del repositorio actual y archivos modificados.
2.  **Files**: Archivos con cambios locales.
3.  **Branches**: Listado de ramas locales y remotas.
4.  **Commits**: Historial de confirmaciones (Git Log).
5.  **Stash**: Confirmaciones guardadas temporalmente.

---

## ⌨️ Atajos de Teclado Fundamentales

### 1. Navegación entre Paneles
*   `Tab` / `Shift + Tab` → Ciclar al panel siguiente o anterior.
*   `1` al `5` → Saltar directamente al panel correspondiente.
*   `Vim keys` (`h`, `j`, `k`, `l`) / `Flechas` → Moverse dentro de una lista o panel.

### 2. Panel de Archivos (Files - Panel 2)
*   `Space` → Preparar (stage) / Despreparar (unstage) el archivo seleccionado.
*   `a` → Preparar (stage) todos los archivos modificados.
*   `d` → Eliminar o revertir cambios locales del archivo seleccionado.
*   `c` → Realizar un commit (abrirá cuadro de diálogo para el mensaje).
*   `C` → Realizar commit usando el editor externo (Neovim).
*   `P` → Hacer push a la rama remota.
*   `p` → Hacer pull desde el repositorio remoto.

### 3. Panel de Ramas (Branches - Panel 3)
*   `Space` → Hacer checkout a la rama seleccionada.
*   `n` → Crear una nueva rama desde la actual.
*   `d` → Eliminar la rama seleccionada (solicita confirmación).
*   `M` → Fusionar (merge) la rama seleccionada dentro de la activa.

### 4. Panel de Commits (Commits - Panel 4)
*   `s` → Hacer squash (fusionar) el commit seleccionado con el anterior.
*   `r` → Renombrar (reword) el mensaje del commit seleccionado.
*   `g` → Hacer un reset (soft/hard) hasta el commit seleccionado.
*   `v` → Revertir (revert) el commit seleccionado.

### 5. Utilidades y Ayuda
*   `?` → Mostrar la lista completa de comandos y atajos activos del panel actual.
*   `Esc` / `q` → Cerrar Lazygit.
