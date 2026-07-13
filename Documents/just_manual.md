# Manual de Just (Command Runner) - Kael OS

`just` es un ejecutor de comandos rápido y moderno similar a `make`, pero especializado en guardar recetas y scripts frecuentes en un archivo `justfile` para no tener que recordar largas sintaxis de comandos.

---

## 📂 Archivos de Configuración
*   **Recetas de Kael OS:** [`~/justfile`](file:///home/jose/justfile) (Configura actualización de sistema con nala, limpieza y ciclos de Docker y bases de datos virtuales).

---

## 🚀 Lista de Recetas Disponibles

Para ejecutar cualquier receta, abre tu terminal y escribe `just <nombre-receta>`:

### 1. Mantenimiento del Sistema
*   **`just upgrade`**
    *   *Acción*: Actualiza la lista de repositorios, actualiza los paquetes instalados de Debian mediante `nala`, y actualiza los paquetes Flatpak en segundo plano de forma unificada.
*   **`just clean`**
    *   *Acción*: Remueve dependencias huérfanas en el sistema y limpia los cachés locales de descarga de paquetes.

### 2. Ciclo de Docker Host
*   **`just docker-start`**
    *   *Acción*: Inicia el daemon del motor de Docker.
*   **`just docker-stop`**
    *   *Acción*: Detiene por completo Docker y su socket de activación para liberar memoria RAM.
*   **`just docker-disable`**
    *   *Acción*: Desactiva el inicio automático de Docker en el arranque del sistema (óptimo para boot rápido).

### 3. Desarrollo SQL (PostgreSQL en Docker)
*   **`just postgres-start`**
    *   *Acción*: Inicia un contenedor aislado de PostgreSQL en Docker (`local-postgres`) en el puerto 5432, ideal para desarrollo local.
*   **`just postgres-stop`**
    *   *Acción*: Detiene y elimina de forma segura el contenedor de desarrollo PostgreSQL.
*   **`just postgres-shell`**
    *   *Acción*: Entra directamente al shell de administración de base de datos interactivo (`psql`) dentro del contenedor en ejecución.

---

## 💡 Comandos Rápidos de Just
*   `just` o `just --list` → Lista todas las recetas documentadas y disponibles en tu `justfile` actual.
*   `just --show <receta>` → Muestra las líneas de comando exactas que componen una receta determinada sin ejecutarla.
