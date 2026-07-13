# Manual de LazySQL - Kael OS

LazySQL es una interfaz de terminal interactiva (TUI) ligera y rápida para explorar y administrar bases de datos relacionales (SQLite, MySQL, PostgreSQL) de manera unificada mediante atajos inspirados en Vim.

---

## 📂 Archivos de Configuración
*   **Conexiones de Bases de Datos:** [`~/.config/lazysql/config.toml`](file:///home/jose/.config/lazysql/config.toml) (Preconfigurada la base de datos de test `~/dev/local.db`).

---

## ⌨️ Interacción y Navegación

### 1. Panel de Conexión Inicial
*   `Enter` → Conectarse a la base de datos seleccionada.
*   `c` → Crear una nueva conexión (soporta SQLite, MySQL, Postgres).
*   `e` → Editar los parámetros de la conexión seleccionada.
*   `d` → Eliminar la conexión de la lista.

### 2. Navegación en Base de Datos (Modo Explorer)
Una vez conectado, la pantalla se divide en 3 secciones principales: **Tablas**, **Vista de Datos** (grilla) y **Editor de Consultas**.
*   `Tab` / `Shift + Tab` → Alternar el foco entre el panel de tablas, el panel de datos y el editor SQL.
*   `j` / `k` o Flechas → Moverse por la lista de tablas o registros.
*   `h` / `l` o Flechas → Moverse entre columnas en la grilla de datos.
*   `/` → Buscar o filtrar registros en la tabla enfocada.

### 3. Editor de Consultas (SQL Query Editor)
*   Escribe sentencias SQL nativas en el panel superior.
*   **`Ctrl + e`** o **`Ctrl + Enter`** → Ejecutar la consulta SQL escrita. Los resultados se actualizarán inmediatamente en la grilla inferior.

### 4. Salida
*   `q` o `Esc` → Cerrar LazySQL o desconectarse del servidor actual.
