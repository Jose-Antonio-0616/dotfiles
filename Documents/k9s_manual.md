# Manual de K9s Kubernetes TUI - Kael OS

K9s es un terminal de interfaz de usuario interactivo (TUI) para monitorear y gestionar clústeres de Kubernetes sin requerir escribir largos comandos de kubectl.

---

## ⌨️ Comandos y Navegación Básica

### 1. Iniciar K9s
*   **`Super + Alt + K`** o escribiendo `k9s` en terminal.

### 2. Panel Principal e Inspección
*   `j` / `k` o Flechas → Navegar entre filas del recurso actual (ej. Pods, Services).
*   `Enter` → Inspeccionar el recurso seleccionado (ej: ver los contenedores que componen un Pod).
*   `Esc` → Volver al nivel anterior.

### 3. Navegación entre Recursos
Presiona **`:`** para abrir la barra de comandos de K9s y escribe el recurso a consultar:
*   `:pods` o `:po` → Listar Pods.
*   `:services` o `:svc` → Listar Servicios.
*   `:deployments` o `:deploy` → Listar Deployments.
*   `:namespaces` o `:ns` → Cambiar o ver espacios de nombres.
*   `:contexts` → Cambiar de clúster / contexto de kubernetes.

### 4. Acciones sobre Recursos (Pods/Deployments)
*   `l` → Ver logs en tiempo real del Pod seleccionado.
*   `d` → Describir (Describe) detalladamente el recurso.
*   `e` → Editar la definición de YAML del recurso en vivo utilizando Neovim.
*   `y` → Ver el manifiesto YAML completo del recurso.
*   `Ctrl + d` → Eliminar (Delete) el recurso seleccionado (solicita confirmación).
*   `s` → Iniciar una sesión de terminal interactiva (Shell) dentro del Pod.

### 5. Ayuda y Salida
*   `?` → Mostrar la ayuda detallada con todos los atajos contextuales del recurso activo.
*   `Ctrl + c` / `:q` → Salir de K9s.
