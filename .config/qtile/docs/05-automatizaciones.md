# 05 - Automatizaciones y Scripts del Sistema

Kael OS delega tareas específicas y menús interactivos a scripts escritos en Bash y Python que se ubican de forma centralizada en [`~/.config/qtile/scripts/`](file:///home/jose/.config/qtile/scripts/).

## 1. Lanzadores e Interfaces de Rofi

### A. Menú de Apagado y Salida (`power`)
*   **Archivo:** [`~/.config/qtile/scripts/power`](file:///home/jose/.config/qtile/scripts/power)
*   **Función:** Despliega un menú en Rofi para realizar acciones del sistema: Bloquear pantalla, Cerrar sesión, Suspender, Reiniciar o Apagar el ordenador.
*   **Atajo:** `Super + X` (o click izquierdo en el icono `󰐥` del panel superior).

### B. Selector de Temas (`thememenu`)
*   **Archivo:** [`~/.config/qtile/scripts/thememenu`](file:///home/jose/.config/qtile/scripts/thememenu)
*   **Función:** Lee de forma dinámica todos los temas disponibles en `~/.config/qtile/themes/` y los presenta en Rofi. Al seleccionar uno, edita el archivo [`theme.py`](file:///home/jose/.config/qtile/theme.py) para cambiar el tema activo y recargar Qtile instantáneamente.
*   **Atajo:** `Super + Shift + T`.

### C. Gestor de Almacenamiento Removible (`manage_drives`)
*   **Archivo:** [`~/.config/qtile/scripts/manage_drives`](file:///home/jose/.config/qtile/scripts/manage_drives)
*   **Función:** Escanea los directorios activos bajo `/media/jose/` y los presenta en Rofi. Si seleccionas uno, te da la opción de **Desmontar** (unmount) o **Expulsar** (eject) de forma segura enviando notificaciones mediante Dunst.
*   **Atajo:** Click derecho sobre la sección de discos en la barra lateral izquierda.

---

## 2. Scripts de Control del Entorno

### A. Script de Inicio Automático (`autostart.sh`)
*   **Archivo:** [`~/.config/qtile/scripts/autostart.sh`](file:///home/jose/.config/qtile/scripts/autostart.sh)
*   **Función:** Se ejecuta una sola vez al cargar Qtile (`startup_once`). Inicia servicios base:
    *   `lxpolkit`: Autenticación gráfica para permisos root.
    *   `feh`: Asigna el fondo de pantalla según el tema activo.
    *   `picom`: Compositor de ventanas en segundo plano.
    *   `dunst`: Servidor de notificaciones del sistema.
    *   `nm-applet`: Icono de red inalámbrica y cableada.
    *   `udiskie`: Demonio de automontaje de dispositivos USB en segundo plano.

### B. Control de Volumen con Notificaciones (`changevolume`)
*   **Archivo:** [`~/.config/qtile/scripts/changevolume`](file:///home/jose/.config/qtile/scripts/changevolume)
*   **Función:** Recibe argumentos (`up`, `down`, `mute`), modifica el nivel de volumen mediante `amixer` o `pactl`, y envía una notificación de Dunst con una barra de progreso que indica el volumen actual de manera limpia.
*   **Atajos:** `Super + F10/F11/F12` o las teclas multimedia `XF86Audio*`.
