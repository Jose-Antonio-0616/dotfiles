# Manual de Lazydocker - Kael OS

Lazydocker es una interfaz de terminal interactiva (TUI) para gestionar servicios, contenedores, imágenes y volúmenes de Docker de forma rápida y sin escribir largos comandos de CLI.

---

## 📂 Archivos de Configuración
*   **Configuración General:** [`~/.config/lazydocker/config.yml`](file:///home/jose/.config/lazydocker/config.yml) (Tema Cyber-Rasta integrado).

---

## 🖥️ Distribución de Paneles
1.  **Services**: Servicios activos (especialmente útil si usas Docker Compose).
2.  **Containers**: Contenedores en ejecución o detenidos.
3.  **Images**: Imágenes descargadas localmente en tu sistema.
4.  **Volumes**: Volúmenes de almacenamiento creados por Docker.

---

## ⌨️ Atajos de Teclado Fundamentales

### 1. Navegación
*   `Tab` / `Shift + Tab` → Cambiar de panel.
*   `Vim keys` (`j`, `k`) o Flechas → Moverse por la lista seleccionada.

### 2. Gestión de Contenedores y Servicios
*   `Space` → Pausar (pause) o reanudar el contenedor seleccionado.
*   `s` → Detener (stop) el contenedor seleccionado.
*   `r` → Reiniciar (restart) el contenedor seleccionado.
*   `d` → Eliminar (remove) el contenedor seleccionado.
*   `E` → Ejecutar un shell interactivo (`sh`/`bash`) dentro del contenedor seleccionado.
*   `l` → Ver logs en tiempo real (puedes desplazarte usando las teclas de scroll).
*   `v` → Mostrar métricas de consumo de CPU/Memoria en tiempo real en forma de gráficos.

### 3. Gestión de Imágenes y Volúmenes
*   `d` → Eliminar la imagen seleccionada o purgar volúmenes huérfanos.
*   `c` → Limpiar contenedores huérfanos del sistema (Prune).

### 4. Utilidades
*   `?` → Mostrar ayuda detallada de atajos.
*   `q` → Salir de Lazydocker.
