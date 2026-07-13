# Manual de Configuración de Zsh (ButterZsh) - Kael OS

Este manual describe la configuración modular de Zsh activa en tu sistema, detallando sus opciones, alias prácticos, plugins cargados y la estructura de archivos en la que se organiza.

---

## 📂 Estructura de Archivos
La configuración de Zsh es modular para facilitar su mantenimiento. El archivo principal de inicio es `~/.zshrc` y la lógica se distribuye bajo `~/.config/zsh/`:

```text
~/.config/zsh/
├── aliases.zsh     # Colección de alias de sistema, git, red y navegación.
├── fzf.zsh         # Integración del buscador difuso (fzf).
├── keybinds.zsh    # Atajos de teclado específicos para la shell.
├── prompt.zsh      # Configuración del prompt visual y cabecera de bienvenida.
├── zoxide.zsh      # Configuración del salto rápido de directorios (zoxide).
└── functions/      # Directorio para funciones personalizadas de shell.
```

---

## ⚙️ Opciones de Shell Activas
*   **AUTO_CD (`setopt AUTO_CD`):** Permite cambiar de directorio simplemente escribiendo su nombre sin necesidad de anteponer el comando `cd`. (Ej. escribir `Downloads` y presionar Enter).
*   **SHARE_HISTORY (`setopt SHARE_HISTORY`):** Comparte el historial de comandos ingresados instantáneamente entre todas las terminales abiertas.
*   **Completado Inteligente:**
    *   Navegación mediante flechas de dirección (`zstyle ':completion:*' menu select`).
    *   Búsqueda insensible a mayúsculas/minúsculas (`matcher-list 'm:{a-zA-Z}={A-Za-z}'`).
    *   Clasificación en grupos visuales por tipo de archivo o categoría.

---

## 🔌 Plugins Integrados (Carga Limpia)
Cargados desde rutas del sistema para evitar dependencias innecesarias:
1.  **`zsh-autosuggestions`**: Sugiere de forma translúcida comandos del historial mientras escribes.
    *   **Atajo:** Presiona `Ctrl + Espacio` para aceptar la sugerencia completa.
2.  **`zsh-syntax-highlighting`**: Colorea los comandos en tiempo real.
    *   **Verde**: Comando válido/instalado.
    *   **Rojo**: Comando inexistente o con error de sintaxis.

---

## 🚀 Alias Útiles (Accesos Rápidos)

### 1. Navegación y LS
*   `..` / `...` / `....` → Sube 1, 2 o 3 niveles de directorio.
*   `-` → Vuelve al directorio anterior.
*   `ls` / `l` / `ll` / `la` → Mapeados a `eza` / `exa` (con iconos, directorios primero y cabeceras) si están instalados, o a variantes enriquecidas de `ls` por defecto.

### 2. Telemetría y Recursos
*   `top` → Ejecuta `btop` de manera prioritaria.
*   `df` / `du` / `free` → Muestran espacio en disco y memoria en formato humano (`-h`).
*   `mem` → Muestra memoria libre y el top 5 de procesos que más consumen.
*   `cpu` → Muestra el top 5 de procesos por consumo de CPU.

### 3. Red y Puertos
*   `myip` → Muestra tu IP privada y pública de forma limpia.
*   `ports` → Lista todas las conexiones TCP/UDP activas.
*   `listening` → Lista todos los puertos abiertos en escucha.

### 4. Accesos a Directorios
*   `g.` → Cambia al directorio de configuración (`~/.config`).
*   `dl` → Cambia a `~/Downloads`.
*   `doc` → Cambia a `~/Documents`.
*   `vid` → Cambia a `~/Videos`.

### 5. Git Simplificado
*   `g` → `git`
*   `gs` → `git status`
*   `ga` / `gaa` → `git add` / `git add -A`
*   `gc` / `gcm` → `git commit` / `git commit -m`
*   `gp` / `gpl` → `git push` / `git pull`
*   `gl` → `git log --oneline --graph --decorate`

### 6. Configuración Rápida
*   `zshrc` → Abre el archivo de configuración en tu `$EDITOR`.
*   `reload` → Recarga las configuraciones de Zsh instantáneamente.
*   `nvimrc` → Abre la configuración de tu Neovim.

### 7. Alias Globales (Se usan al final de cualquier comando)
*   `G` (ej: `cat file G texto`) → Filtra mediante `grep -i`.
*   `L` (ej: `ls L`) → Pasa el resultado por el paginador `less`.
*   `H` / `T` → Pasa el resultado por `head` o `tail`.
*   `N` (ej: `ping host N`) → Redirige la salida de error a `/dev/null`.
*   `J` → Pasa el resultado formateado a través de `jq`.

---

## 🎨 Prompt Cyber-Rasta
El prompt muestra:
`[HH:MM:SS] usuario at host in ~/directorio (rama-git*) [estado_salida]`
*   **Git Activo**: Muestra la rama actual y añade un asterisco (`*`) en color verde si hay cambios pendientes (dirty).
*   **Estado de Salida**: Muestra un icono de check verde (`✔`) si el último comando terminó con éxito, o un icono de cruz con código de error en color rojo (`✘ <code_error>`).
