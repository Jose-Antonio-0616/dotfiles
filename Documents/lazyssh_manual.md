# Manual de LazySSH - Kael OS

LazySSH es un gestor de conexiones SSH en terminal interactivo escrito en Go. Lee directamente tu configuración SSH local para permitirte conectar a tus servidores de forma rápida y sin memorizar direcciones IP.

---

## 📂 Archivos de Configuración
*   **Conexiones SSH:** [`~/.ssh/config`](file:///home/jose/.ssh/config) (Permisos seguros `600` requeridos).
*   **Llaves Criptográficas:** `~/.ssh/id_ed25519` (Llave privada) y `id_ed25519.pub` (Llave pública).

---

## ⌨️ Uso e Interacción

### 1. Iniciar LazySSH
Puedes iniciarlo escribiendo `lazyssh` en tu terminal, o directamente mediante el atajo del Window Manager:
*   **`Super + Shift + S`**

### 2. Filtrado y Selección
*   **Filtrar (Búsqueda difusa):** Empieza a escribir cualquier carácter. LazySSH filtrará dinámicamente tu lista de servidores por nombre (`Host`), dirección IP (`HostName`) o usuario (`User`).
*   `j` / `k` o Flechas → Moverse por la lista filtrada de servidores.
*   **`Enter`** → Iniciar la conexión SSH interactiva al servidor seleccionado en tu pestaña de terminal actual.
*   `q` o `Esc` → Cerrar LazySSH.
