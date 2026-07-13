# Manual de Usuario - w3m (Navegador Web de Terminal)

`w3m` es un navegador web rápido y ligero en modo texto que permite visualizar páginas HTML directamente en tu terminal. En Kael OS está optimizado con soporte para ratón, atajos Vim y prevención de estiramiento de imágenes.

---

## 🚀 Inicio Rápido
*   **Atajo en Qtile**: Presiona `Super + W` para abrir `w3m` directamente en una terminal Kitty con Google de página de inicio.
*   **Lanzar manualmente**: `w3m <URL>` (ej: `w3m https://html.duckduckgo.com`).

---

## ⚠️ Advertencia de Compatibilidad (Google y JavaScript)
> [!WARNING]
> Google y otros motores pesados implementan bloqueos y alertas de seguridad ("Navegador no compatible") cuando detectan navegadores de terminal sin JavaScript (como `w3m` y `lynx`).
> 
> **Solución Recomendada**:
> Para una experiencia de búsqueda en terminal fluida y 100% libre de advertencias, utiliza **DuckDuckGo HTML / Lite**:
> *   **DuckDuckGo HTML**: `https://html.duckduckgo.com` (Altamente recomendado, carga limpia y rápida).
> *   **DuckDuckGo Lite**: `https://lite.duckduckgo.com` (Versión minimalista de solo texto).

---

## ⌨️ Atajos de Teclado Esenciales

### Navegación de Páginas
*   `h, j, k, l`: Moverse a la izquierda, abajo, arriba y derecha (estilo Vim).
*   `Espacio` / `b`: Bajar / Subir una pantalla completa.
*   `Tab` / `Shift + Tab`: Ir al enlace siguiente / anterior.
*   `Enter`: Abrir el enlace seleccionado o **activar un campo de entrada de texto (formulario)**.
*   `B` (Shift + b): Volver a la página anterior en el historial.

### Búsqueda e Introducción de Texto (Muy Importante)
> [!IMPORTANT]
> **Cómo escribir en campos de búsqueda (formularios)**:
> 1. Mueve el cursor con las flechas o haz click sobre la caja de texto (campo de entrada).
> 2. Presiona **`Enter`**. Verás que en la línea inferior de la terminal aparece un prompt que te permite escribir.
> 3. Escribe tu búsqueda y presiona **`Enter`** de nuevo para confirmar el texto en el campo.
> 4. Desplázate (o haz click) sobre el botón de enviar ("Search" o "Buscar") y presiona `Enter`.

*   `/`: Buscar texto dentro de la página actual (`n` para ir al siguiente resultado).

### Gestión de Pestañas
*   `T` (Shift + t): Abrir una nueva pestaña.
*   `Esc-t`: Abrir el menú de pestañas.
*   `{` / `}`: Ir a la pestaña anterior / siguiente.
*   `C-q` / `C-w`: Cerrar la pestaña actual.

### Utilidades Especiales
*   `M` (Shift + m): **Abrir la página actual en Firefox gráfico**.
*   `v`: Ver el código fuente HTML de la página.
*   `s`: Abrir el menú de historial de navegación.
*   `o`: Abrir el panel de configuración de opciones de w3m.
*   `q`: Salir de w3m (pide confirmación `y/n`).
