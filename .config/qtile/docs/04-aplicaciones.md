# 04 - Stack Tecnológico y Aplicaciones

Kael OS define un conjunto de aplicaciones robustas, ligeras y con interfaces de terminal (TUI) para evitar el uso excesivo de recursos gráficos y acelerar el flujo de trabajo mediante el teclado.

## 1. Núcleo de Terminal y Multiplexor
*   **Kitty (Instalado y Configurado):** El emulador de terminal principal, acelerado por GPU, con soporte nativo para visualización de imágenes en terminal y alta velocidad de refresco.
*   **Zellij (Instalado y Configurado):** Multiplexor de terminal moderno escrito en Rust, diseñado con layouts intuitivos y pestañas sin requerir una compleja curva de aprendizaje como `tmux`.

## 2. Shells y Entornos
*   **Zsh (Instalado y Configurado):** El shell interactivo por defecto (ButterZsh), configurado con autocompletado inteligente e histórico persistente.
*   **Bash (Instalado):** Reservado exclusivamente para la ejecución de scripts del sistema y automatizaciones modulares.
*   **Fish (Instalado y Configurado):** Utilizado para exploración rápida y autocompletados basados en el historial del sistema sin configuraciones extra.
*   **Neovim + LazyVim (Instalado y Configurado):** El editor de código principal del sistema, equipado con LSP, formateadores y navegación de archivos de alto rendimiento.
*   **Fresh (Instalado):** Editor de texto y entorno de desarrollo (IDE) TUI en Rust moderno y ultra rápido.

## 3. Administración y Navegación de Archivos
*   **Yazi (Instalado y Configurado):** Administrador de archivos en terminal (TUI) escrito en Rust, ultra rápido y con previsualizaciones de imágenes a través de Kitty.
*   **Thunar (Instalado):** Administrador de archivos gráfico ligero oficial (XFCE), útil para arrastrar archivos o tareas visuales simples.

## 4. Herramientas CLI Core (Rust & Go)
*   **fzf / ripgrep (rg) / fd (Instalado):** El trío esencial para búsquedas difusas rápidas de texto y archivos en todo el sistema.
*   **zoxide (Instalado):** Un reemplazo inteligente de `cd` que aprende de tus hábitos de navegación para saltar de carpeta rápidamente.
*   **just (Instalado):** Gestor de comandos basado en un archivo `justfile` para simplificar la ejecución de scripts de desarrollo local.
*   **ncdu (Instalado):** Utilidad en terminal para auditar de forma visual el uso de espacio en disco.
*   **btop (Instalado):** Monitor de recursos del sistema con una interfaz TUI interactiva y moderna.
*   **fastfetch (Instalado):** Muestra información del sistema al iniciar terminales.

## 5. Infraestructura y Bases de Datos
*   **Docker & Docker Compose (Instalado):** Capa de infraestructura y virtualización local para aislamiento de entornos de desarrollo.
*   **psql (Instalado):** Cliente nativo de terminal para PostgreSQL.
*   **sqlite3 (Instalado):** Motor de base de datos local e interactivo para proyectos rápidos.
*   **lazysql (Instalado y Configurado):** Interfaz TUI para navegar y consultar bases de datos relacionales sin usar SQL plano en terminal.

## 6. Navegación Web y Multimedia
*   **Brave Browser (Pendiente) / Firefox (Instalado):** Brave es el navegador principal objetivo por su rendimiento y bloqueo nativo de anuncios. Firefox actúa como respaldo estable instalado.
*   **lynx / w3m (Instalados):** Navegadores web en terminal para lectura rápida de documentación sin interfaz gráfica.
*   **mpv (Instalado y Configurado):** Reproductor multimedia minimalista de alto rendimiento controlado por teclado.

## 7. Ecosistema de Interfaces TUI ("Lazy")
Interfaces basadas en terminal para gestionar servicios externos con atajos rápidos de teclado:
*   **lazygit (Instalado y Configurado):** Interfaz para control de versiones Git.
*   **lazydocker (Instalado y Configurado):** Interfaz para contenedores y volúmenes de Docker.
*   **k9s (Instalado):** Orquestador interactivo para Kubernetes.
*   **lazyssh (Instalado y Configurado):** Gestor de conexiones SSH remotas.
*   **lazyjournal (Pendiente):** Navegador interactivo para el log del sistema (journald).
