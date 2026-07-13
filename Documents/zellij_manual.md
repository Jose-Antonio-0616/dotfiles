# Manual de Zellij Terminal Multiplexer - Kael OS

Zellij es un multiplexor de terminal moderno escrito en Rust, diseñado para organizar tus flujos de trabajo en pestañas (tabs) y paneles (panes) de forma intuitiva, sin las complejas combinaciones de teclas de tmux.

---

## 📂 Archivos de Configuración
*   **Configuración General:** [`~/.config/zellij/config.kdl`](file:///home/jose/.config/zellij/config.kdl) (Define el shell predeterminado como Zsh, desactiva bordes gruesos y aplica el tema Cyber-Rasta).

---

## ⌨️ Atajos de Teclado y Flujo de Trabajo

Zellij muestra una barra de ayuda inferior con los atajos activos según el modo en el que te encuentres. 

### 1. Bloqueo de Atajos (Lock Mode)
*   **`Ctrl + g`** → Cambia entre el modo bloqueado y desbloqueado.
    *   *Nota*: El modo bloqueado sirve para que los atajos de Zellij no entren en conflicto con los atajos de Neovim o de la shell.

### 2. Gestión de Paneles (Pane Mode)
Presiona **`Ctrl + p`** para entrar en el modo panel:
*   `n` → Crear nuevo panel (división inteligente).
*   `d` → Dividir panel hacia abajo (split vertical).
*   `r` → Dividir panel hacia la derecha (split horizontal).
*   `x` → Cerrar el panel enfocado actualmente.
*   `f` → Alternar panel a pantalla completa (Fullscreen).
*   `Flechas / Vim keys` → Cambiar el foco entre paneles.

### 3. Gestión de Pestañas (Tab Mode)
Presiona **`Ctrl + t`** para entrar en el modo pestaña:
*   `n` → Crear nueva pestaña.
*   `x` → Cerrar pestaña actual.
*   `r` → Renombrar pestaña.
*   `p` / `n` → Ir a la pestaña anterior (previous) o siguiente (next).

### 4. Modo Desplazamiento (Scroll Mode)
Presiona **`Ctrl + s`** para navegar por el historial del terminal:
*   `j` / `k` o Flechas → Subir y bajar línea por línea.
*   `Ctrl + f` / `Ctrl + b` → Subir o bajar página completa.
*   `/` → Buscar texto dentro del historial del terminal.

### 5. Salir de Zellij
*   **`Ctrl + q`** → Salir de Zellij cerrando la sesión actual y todos sus terminales.
*   **`Ctrl + o`** y luego `d` → Desacoplarse (Detach) de la sesión, permitiendo que Zellij siga corriendo de fondo.
