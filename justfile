# actualizar sistema
upgrade:
    @sudo nala update
    @echo ''
    @sudo nala upgrade
    @echo ''
    @flatpak update

# limpiar sistema
clean:
    @sudo nala autoremove
    @echo ''
    @sudo nala clean

# activar docker
docker-start:
    @sudo systemctl start docker

# detener docker
docker-stop:
    @sudo systemctl stop docker
    @sudo systemctl stop docker.socket

# desactivar inicio automatico de docker
docker-disable:
    @sudo systemctl disable docker
    @sudo systemctl disable docker.socket

# iniciar contenedor de postgresql local para desarrollo
postgres-start:
    @docker run --name local-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
    @echo 'Contenedor local-postgres iniciado en el puerto 5432'

# detener y remover contenedor de postgresql local
postgres-stop:
    @docker stop local-postgres
    @docker rm local-postgres
    @echo 'Contenedor local-postgres detenido y removido'

# entrar al shell interactivo psql en el contenedor de docker
postgres-shell:
    @docker exec -it local-postgres psql -U postgres

# configuracion el sistema con agy
kael-OS:
    agy --conversation=eb466ab0-843d-4d9b-8064-1693c8308c90

