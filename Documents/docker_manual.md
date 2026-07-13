# Manual de Docker & Docker Compose - Kael OS

Docker es la plataforma de virtualización basada en contenedores oficial elegida para desarrollo local en Kael OS, permitiendo aislar servicios de bases de datos y frameworks sin ensuciar el sistema Debian host.

---

## ⚙️ Integración con el Sistema y Permisos

En Kael OS, Docker está configurado para:
1.  **Ejecutarse sin `sudo`**: Tu usuario pertenece al grupo `docker`, permitiéndote lanzar comandos de contenedores y usar interfaces interactivas como `lazydocker` con permisos de usuario normal.
2.  **Desactivado al arrancar (On-Demand)**: El servicio no se levanta automáticamente al iniciar la PC para conservar el consumo de memoria RAM por debajo de 1GB en reposo.

---

## ⌨️ Comandos y Recetas Frecuentes

### 1. Gestión de Servicios (vía `just`)
Puedes iniciar y detener Docker de manera rápida usando las recetas integradas de tu `justfile`:
*   `just docker-start` → Levantar el motor de Docker.
*   `just docker-stop`  → Detener Docker y su socket de activación para liberar memoria RAM.

### 2. Comandos CLI Esenciales
*   `docker ps` → Listar todos los contenedores activos.
*   `docker ps -a` → Listar todos los contenedores (activos y detenidos).
*   `docker images` → Listar todas las imágenes descargadas localmente.
*   `docker logs <nombre-contenedor>` → Ver la salida de registro de un contenedor.
*   `docker exec -it <nombre-contenedor> sh` → Entrar de forma interactiva al terminal de un contenedor en ejecución.

### 3. Docker Compose
Docker Compose simplifica la definición de entornos multi-contenedor mediante un archivo `docker-compose.yml`:
*   `docker compose up -d` → Iniciar todos los servicios definidos en segundo plano (detached).
*   `docker compose down` → Detener y eliminar los contenedores, redes y volúmenes asociados.
*   `docker compose logs -f` → Seguir la salida de logs de todos los contenedores del proyecto.
