# Manual de Usuario - Qtile Window Manager (Kael OS)

Este manual resume el funcionamiento general de la interfaz gráfica y el gestor de ventanas (Window Manager) **Qtile** en Kael OS, detallando atajos, flujos de trabajo en múltiples pantallas y personalizaciones de temas y layouts.

---

## 🚀 Conceptos Fundamentales
*   **Gestor de Ventanas en Mosaico (Tiling)**: Las ventanas no se superponen de forma predeterminada; ocupan el espacio de la pantalla en base a un layout activo.
*   **Teclas Modificadoras**:
    *   `Super` (o tecla Windows) es la tecla principal de control del sistema (`mod`).
    *   `Alt` se identifica como `mod1`.

---

## ⌨️ Atajos de Teclado Críticos

### Gestión de Ventanas
*   `Super + q`: Cerrar la ventana en foco.
*   `Super + j / k`: Cambiar el foco a la ventana siguiente / anterior.
*   `Super + h / l`: Cambiar el foco a la ventana izquierda / derecha.
*   `Super + Shift + j / k`: Desplazar la ventana en foco hacia abajo / arriba.
*   `Super + Shift + h / l`: Desplazar la ventana en foco hacia la izquierda / derecha.
*   `Super + Ctrl + h / l / j / k`: Redimensionar las ventanas en mosaico.
*   `Super + Shift + Espacio`: Alternar la ventana activa a modo flotante y centrarla.
*   `Super + Shift + F`: Maximizar ventana activa (Fullscreen).

### Lanzadores de Aplicaciones y TUIs
*   `Super + Enter`: Abrir terminal Kitty.
*   `Super + d`: Ejecutar Rofi (Lanzador de aplicaciones gráficas).
*   `Super + e`: Abrir Thunar (Explorador de archivos gráfico).
*   `Super + /`: Mostrar este buscador de atajos interactivo en pantalla.
*   `Super + v`: Abrir Neovim.
*   `Super + y`: Abrir Yazi (Explorador de archivos TUI).
*   `Super + z`: Abrir Zellij (Multiplexor).
*   `Super + g`: Abrir Lazygit.
*   `Super + s`: Abrir LazySQL.
*   `Super + Shift + S`: Abrir LazySSH.
*   `Super + w`: Abrir w3m (Navegador web de terminal).
*   `Super + Shift + W`: Abrir Lynx (Navegador de terminal de texto puro).
*   `Super + Shift + B`: Ejecutar respaldo de dotfiles instantáneo a GitHub.

### Control de Hardware y Medios
*   `Super + Shift + T`: Abrir selector interactivo de fondos de pantalla (Wallpaper Switcher).
*   `Super + Shift + D`: Abrir selector de distribución de pantallas (Laptop, HDMI-Horizontal, HDMI-Vertical).
*   `F10` / `F11` / `F12`: Silenciar / Bajar volumen / Subir volumen (con barra visual HUD).
*   `Brillo +/-` (Teclas de laptop): Subir / Bajar brillo de la pantalla (con barra visual HUD).

---

## 🖥️ Gestión de Múltiples Monitores y Workspaces
Kael OS implementa un sistema híbrido de espacios de trabajo estáticos para evitar desorden en configuraciones de doble pantalla:

*   **Laptop (Pantalla 0)**: Hospeda de forma fija los Workspaces **`1`** (Consola), **`3`** (Navegador/Firefox) y **`5`** (Discord).
*   **Monitor HDMI (Pantalla 1)**: Hospeda de forma fija los Workspaces **`2`** (Editor de Código) y **`4`** (Archivos/Multimedia).
*   Al abrir aplicaciones como Firefox o editores de código, se enrutan automáticamente a su monitor correspondiente.
*   Si el monitor externo se desconecta, todos los workspaces vuelven a la laptop automáticamente.

---

## 📐 Layouts Disponibles (Ciclar con `Super + Tab`)
1.  **`MonadTall`**: Distribución vertical (Master grande a la izquierda, terminales secundarias apiladas a la derecha).
2.  **`MonadWide`**: Distribución horizontal (Master grande arriba, ideal para el monitor en vertical).
3.  **`BSP (Manual)`**: Partición binaria controlada. Divide en mitades la ventana que tenga el foco activo.
4.  **`BSP (Fair)`**: Partición binaria auto-balanceada automáticamente.
5.  **`Max`**: Muestra una sola ventana en pantalla completa sin bordes.
