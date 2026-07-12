# 02 - Diseño de la Interfaz (UI/UX)

Kael OS adopta un diseño visual coherente llamado **"Cyber-Rasta" Contextual**, priorizando un contraste nítido, legibilidad de noche y telemetría no invasiva.

## 1. Paleta de Colores (Cyber-Rasta)
*   **Fondo (Background):** Negro absoluto (`#000000`) para las barras y negro carbón (`#0c0c0e`) para las ventanas y marcos de widgets, maximizando el ahorro de energía en pantallas OLED y reduciendo la fatiga visual.
*   **Texto Principal:** Blanco/Gris suave (`#e0e0e0`) para que las métricas y textos sean legibles sin destellar.
*   **Acentos Vibrantes:**
    *   **Verde Esmeralda (`#00e676`):** Indica salud del sistema, redes activas, batería en carga y entornos virtuales activos.
    *   **Amarillo/Dorado (`#ffdf00`):** Alertas suaves, telemetría de memoria RAM, volumen, fecha/hora y hardware periférico externo.
    *   **Rojo Neón (`#ff3a3a`):** Alertas de uso crítico (CPU alta) y botones de acción física (apagado/reinicio).

---

## 2. Barra Superior (Telemetría y Tiempo)
Permanece siempre visible a lo largo de todas las pantallas en la parte superior (`34px` de alto). Su función es proporcionar el estado histórico y la telemetría pasiva del sistema:

*   **Workspaces (1-5):** Indicador numérico estático de los escritorios. Resalta el escritorio activo y tiene soporte para arrastre/navegación.
*   **Métricas de Hardware:**
    *   `CPU` (Rojo): Consumo en porcentaje.
    *   `RAM` (Amarillo): Uso de memoria activa.
    *   `SSD` (Verde): Espacio libre en la partición raíz `/`.
*   **Métricas de Conexión:**
    *   `WiFi / Ethernet` (Verde): Indica la red inalámbrica o cableada conectada activa mediante Nm-Applet y SysTray.
*   **Controladores locales:**
    *   `Volumen` (Amarillo): Control interactivo del mezclador de audio.
    *   `Batería` (Verde): Muestra el estado actual y la carga en tiempo real (con tolerancia a fallos ACPI).
*   **Reloj y Acciones**:
    *   `Fecha/Hora` (Amarillo/Verde): Separados para facilitar su lectura en la esquina derecha.
    *   `Snapshot Button` (Verde): Lanza Flameshot para capturas rápidas.
    *   `Power Button` (Rojo): Lanza Rofi en modo apagado/reinicio.

---

## 3. Panel Contextual (Barra Lateral Izquierda)
Una barra lateral de **`50px`** de ancho de tipo **Icon-Only** (sin texto descriptivo, centrada verticalmente) que responde a la pregunta: *¿Qué está pasando actualmente en mi sistema?*

*   **Ventanas Abiertas (Apps):** Iconos de las aplicaciones activas (ej. ``, ``). Si hay múltiples instancias, añade contadores (ej. `×2`). Al hacer click izquierdo, abre la selección de ventanas en Rofi (`rofi -show window`).
*   **Almacenamiento Dinámico (Discos):** Muestra si hay USBs (``) o discos (``) montados en `/media/jose/`. Click izquierdo abre `Thunar`, click derecho abre el menú de desmontado seguro en Rofi.
*   **Hardware Activo:** Muestra periféricos conectados (ratón `󰍽`, teclado `󰌌`, auriculares `󰋋`) mediante monitoreo en `xinput` y `wpctl`.
*   **Contexto de Desarrollo (Dev):** Muestra de forma inteligente la infraestructura en uso (`🐍` para entornos virtuales python, `🐳` para Docker, `🌐` para Django, `` para tmux/zellij).

---

## 4. Compositor y Efectos (Picom)
Se utiliza **`picom` (versión v13)** para gestionar sombras y bordes redondeados:
*   Las ventanas de aplicaciones tienen sombras suaves y esquinas redondeadas (`corner-radius = 10`).
*   Para evitar aberraciones estéticas, las barras de Qtile (identificadas por su propiedad X11 `_NET_WM_STATE_BELOW`) están configuradas con **`corner-radius = 0`** (esquinas totalmente rectas) y opacidad del **`100%`** (completamente sólidas).
