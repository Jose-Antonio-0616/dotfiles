# 00 - Filosofía de Kael OS

Kael OS no es simplemente una distribución gráfica personalizada; es una filosofía de diseño y entorno de trabajo optimizada para la productividad, la consistencia y el control absoluto. Se construye sobre los cimientos de la minimalismo, la navegación eficiente por teclado y la resiliencia del sistema.

## Principios Fundacionales

### 1. Minimalismo Estricto
*   **Consumo de Recursos en Reposo:** El entorno debe consumir menos de **`1 GB`** de memoria RAM en reposo. Esto se logra minimizando los demonios de fondo, evitando entornos de escritorio pesados como GNOME o KDE, y delegando la visualización del sistema a Qtile y Xorg.
*   **Sin Software de Relleno (No-Bloat):** Solo se instalan y ejecutan herramientas con un propósito específico y probado. La estética gráfica nunca debe justificar la degradación del rendimiento.

### 2. Teclado como Interfaz Principal (Keyboard First)
*   **Navegación Tiling:** Las ventanas se distribuyen de forma matemática sin superponerse para optimizar el área visible.
*   **Reducción del Uso del Ratón:** Toda acción común (abrir aplicaciones, mover ventanas, cambiar de foco, gestionar workspaces, controlar volumen/brillo y apagar el equipo) se puede realizar instantáneamente mediante combinaciones de teclado con la tecla `Super` (mod4).

### 3. Modularidad y Coherencia
*   **Lógica Separada (Dotfiles Limpios):** En lugar de un archivo de configuración gigante y monolítico en Qtile, las configuraciones se dividen en módulos de Python bien definidos (`keys.py`, `groups.py`, `widgets.py`, etc.).
*   **Independencia de Componentes:** Cada herramienta del stack (Kitty para la terminal, Neovim para el código, Dunst para notificaciones, Picom para composición) hace una sola cosa de manera óptima y se comunica mediante protocolos limpios (notificaciones, variables de entorno, scripts de control).

### 4. Tolerancia a Fallos y Reproducibilidad
*   **Capa de Recuperación Btrfs:** El sistema de archivos Btrfs gestiona copias de seguridad instantáneas (snapshots), permitiendo que el sistema pueda retornar a un estado funcional previo en segundos ante un fallo de actualización o configuración.
*   **Fácil Reinstalación:** Todo el stack está preparado para poder replicarse y reinstalarse rápidamente desde dotfiles portables.
