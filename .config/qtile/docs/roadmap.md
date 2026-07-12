# Roadmap de Kael OS

Este documento traza las fases de desarrollo y optimizaciones futuras planificadas para perfeccionar el entorno de trabajo **Kael OS**.

---

## 📅 Hitos del Roadmap

### Fase 1: Finalización de la Modularización y UI (Completado)
*   [x] Separar el archivo monolítico `config.py` en módulos dedicados.
*   [x] Integrar la paleta de colores Cyber-Rasta en Qtile y Dunst.
*   [x] Diseñar e implementar la barra superior limpia.
*   [x] Diseñar e implementar la barra lateral izquierda (Panel Contextual) de 50px con iconos activos.
*   [x] Corregir la integración con el compositor Picom v13 para quitar bordes curvos y sombras de las barras.

### Fase 2: Configuración del Stack Tecnológico (Completado)
*   [x] Instalar y configurar el multiplexor de terminal **Zellij** con la paleta de colores Cyber-Rasta.
*   [x] Instalar el shell **Fish** para pruebas rápidas y configurar su historial.
*   [x] Instalar y configurar el gestor de archivos TUI **Yazi**.
*   [x] Instalar y configurar **Docker** y **Docker Compose** para servicios locales (con permisos sin sudo).
*   [ ] Instalar **Brave Browser** como navegador oficial principal y establecer Firefox como navegador de respaldo secundario (Firefox-esr activo como respaldo).
*   [x] Instalar y configurar el ecosistema TUI "Lazy": **lazygit**, **lazydocker**, **lazysql**, **lazyssh** y **k9s**.

### Fase 3: Mapeo Definitivo de Atajos de Teclado (Completado)
*   [x] Reasignar `Super + E` para lanzar Thunar de forma consistente con la filosofía de explorador gráfico oficial.
*   [x] Remover Geany y liberar atajos para herramientas del stack de desarrollo.
*   [x] Mapear atajos de terminal interactivos para abrir herramientas TUI del stack (ej. `Super + G` para lazygit, `Super + D` para lazydocker, `Super + S` para lazysql, `Super + Y` para yazi, etc.).
*   [x] Corregir el script de ayuda (`help`) para que lea dinámicamente de `keys.py`.

### Fase 4: Enrutamiento Automático y Reglas de Ventana (Completado)
*   [x] Mapear clases de aplicaciones críticas (ej. Discord, Firefox) para que se abran de forma automática en sus escritorios correspondientes (ruteo dinámico).
*   [x] Configurar reglas avanzadas en [`layouts.py`](file:///home/jose/.config/qtile/layouts.py) para controlar diálogos flotantes molestos.
*   [x] Configurar Scratchpads de sistema para usar Kitty (con soporte para tema Cyber-Rasta).
*   [x] Solucionar el problema de resolución y posicionamiento del monitor secundario HDMI-1 (1920x1080) en autostart.sh.

### Fase 5: Automatización del Mantenimiento y Dotfiles (Completado)
*   [x] Desarrollar un script de sincronización centralizado (`dotfiles-sync`) para respaldar configuraciones críticas (Qtile, Kitty, Neovim, Yazi, Zellij, Fish, SSH y Just) bajo el directorio `~/dotfiles/` utilizando control de versiones Git.
*   [x] Crear atajo de teclado en `keys.py` (`Super + Shift + B`) para lanzar el respaldo y notificar al usuario sobre cambios detectados.
*   [x] Desarrollar un script de comprobación de actualizaciones de sistema (`check-updates`) que alerta visualmente vía Dunst si hay actualizaciones, integrado en el inicio del sistema a través de `autostart.sh`.
