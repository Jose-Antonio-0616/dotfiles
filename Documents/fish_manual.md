# Manual de Fish Shell - Kael OS

Fish (Friendly Interactive Shell) es un shell de línea de comandos inteligente y amigable para el usuario que funciona sin complejas configuraciones iniciales. Está configurado como tu shell secundario/exploratorio en Kael OS.

---

## 📂 Archivos de Configuración
*   **Configuración General:** [`~/.config/fish/config.fish`](file:///home/jose/.config/fish/config.fish) (Configura variables de entorno, alias compatibles con Zsh, prompt modular y tema de colores Cyber-Rasta).

---

## 🌟 Características Clave de Fish

### 1. Autosugerencias Inteligentes
Mientras escribes un comando, Fish buscará en tu historial de comandos recientes y sugerirá el resto en color gris atenuado.
*   **Flecha Derecha** o **`Ctrl + f`** → Aceptar la sugerencia completa.
*   **`Alt + Flecha Derecha`** → Aceptar la sugerencia palabra por palabra.

### 2. Resaltado de Sintaxis
Fish valida los comandos en tiempo real:
*   Si el comando que escribes está instalado o existe, se coloreará en **Verde Esmeralda** (`#00e676`).
*   Si contiene errores de sintaxis o el comando no existe, se coloreará en **Rojo Neón** (`#ff3a3a`).
*   Las variables y parámetros válidos se muestran en gris/blanco y las comillas en **Amarillo/Dorado** (`#ffdf00`).

### 3. Configuración Gráfica
Fish permite configurar tus colores, prompt y funciones de manera visual e interactiva desde el navegador web.
*   **Comando:** `fish_config` (Levanta un servidor web local temporal para personalizar tu shell).

### 4. Ayuda Integrada
*   **`man` en el navegador**: Escribe `help` y presiona Enter para abrir la documentación oficial de Fish en tu navegador.
