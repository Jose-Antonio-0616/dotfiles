# 03 - Gestión de Workspaces (Escritorios)

Kael OS optimiza la organización espacial de las ventanas utilizando un esquema de workspaces (grupos) lógicos estáticos, evitando el desorden visual y promoviendo el enfoque.

## 1. Definición de Workspaces
El archivo [`groups.py`](file:///home/jose/.config/qtile/groups.py) define **5 workspaces principales** identificados de forma numérica:

*   **`1` (Main / Terminales):** Workspace por defecto para terminales interactivas, tareas de sistema rápidas y navegación TUI.
*   **`2` (Dev / Código):** Reservado para editores de código (Neovim/Geany) y terminales de depuración de desarrollo.
*   **`3` (Web / Documentación):** Destinado para navegadores web principales (Firefox/Brave) para visualización de interfaces y lectura.
*   **`4` (File Manager / Media):** Destinado a la administración de archivos gráfica (Thunar) y reproducción multimedia (mpv).
*   **`5` (Comms / Chat):** Espacio exclusivo para clientes de comunicación como Discord, Slack, correo o herramientas secundarias.

---

## 2. Navegación e Interacción

### Navegación por Teclado (Recomendada)
*   `Super + [1-5]` → Cambia instantáneamente al Workspace correspondiente.
*   `Super + Shift + [1-5]` → Mueve la ventana enfocada actualmente al Workspace seleccionado y cambia el foco a él (comportamiento ágil para arrastre).

### Navegación por Ratón
*   Hacer click izquierdo en los números `1` al `5` en la barra superior cambia de escritorio.
*   El scroll del ratón sobre la barra de Workspaces superior permite ciclar secuencialmente entre escritorios activos.

---

## 3. Comportamiento en la Barra Lateral
Mientras que la barra superior mantiene un listado numérico estático de los escritorios para saber siempre en cuál estás situado, la **Barra Lateral Izquierda** (Panel Contextual) consolida los iconos de las aplicaciones abiertas en todos los escritorios de manera global. 

Esto te permite ver qué aplicaciones están abiertas en el sistema completo en una sola vista, y al dar click izquierdo sobre ellas, abrir la lista de ventanas en Rofi para saltar directamente a cualquiera de ellas sin importar en qué workspace esté oculta.

---

## 4. Scratchpads (Escritorios Flotantes Ocultos)
Además de los 5 escritorios principales, existe un grupo especial llamado `scratchpad` que contiene utilidades flotantes que se despliegan sobre cualquier escritorio activo mediante un atajo de teclado:

*   **Terminal Rápida (Kitty):** Se activa y oculta con `Super + Shift + Enter`. Perfecta para comandos rápidos, compilaciones rápidas o consultas de sistema rápidas.
*   **Controlador de Audio (Pulsemixer):** Se activa y oculta con `Super + Alt + A`. Abre un mezclador de audio TUI flotante en el centro de la pantalla para ajustar canales y dispositivos de forma inmediata.
