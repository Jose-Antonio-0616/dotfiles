# Manual de Usuario - Lynx (Navegador Web de Terminal)

`lynx` es el navegador web de terminal más antiguo y clásico. Es de solo texto puro, sumamente rápido y eficiente para entornos sin entorno gráfico o redes muy lentas.

---

## 🚀 Inicio Rápido
*   **Atajo en Qtile**: Presiona `Super + Shift + W` para abrir `lynx` directamente en una terminal Kitty con Google.
*   **Lanzar manualmente**: `lynx <URL>` (ej: `lynx https://html.duckduckgo.com`).

---

## ⚠️ Advertencia de Compatibilidad (Google y JavaScript)
> [!WARNING]
> Google y otros sitios modernos muestran bloqueos ("Navegador no compatible") cuando detectan navegadores sin soporte para JavaScript como `lynx`.
> 
> **Solución Recomendada**:
> Para buscar en terminal de manera fluida, se recomienda usar **DuckDuckGo HTML / Lite**:
> *   **DuckDuckGo HTML**: `https://html.duckduckgo.com` (Soporta tablas y es rápido).
> *   **DuckDuckGo Lite**: `https://lite.duckduckgo.com` (Texto puro ideal para Lynx).

---

## ⌨️ Atajos de Teclado Esenciales

### Navegación de Páginas
*   `Flecha Arriba` / `Flecha Abajo`: Moverse al enlace anterior / siguiente.
*   `Flecha Derecha` / `Enter`: Seguir el enlace seleccionado.
*   `Flecha Izquierda` / `u`: Volver a la página anterior (atrás).
*   `Espacio` / `b`: Avanzar / Retroceder página completa.

### Introducción de Texto
*   En Lynx, los campos de texto se activan automáticamente cuando el cursor se sitúa en ellos. Puedes empezar a escribir directamente.
*   Presiona `Enter` para enviar el formulario o confirmar.

### Utilidades
*   `g`: Ir a una nueva URL (pregunta dirección abajo).
*   `h`: Abrir la ayuda de Lynx.
*   `v`: Ver el historial de páginas visitadas.
*   `\` (barra invertida): Ver el código fuente HTML de la página.
*   `q`: Salir de Lynx (confirma con `y`).
