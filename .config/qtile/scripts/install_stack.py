#!/usr/bin/env python3
import os
import sys
import urllib.request
import json
import tarfile
import zipfile
import shutil
import tempfile

# Directorio de instalación local del usuario (ya en el PATH)
BIN_DIR = os.path.expanduser("~/.local/bin")
os.makedirs(BIN_DIR, exist_ok=True)

# Listado de aplicaciones a instalar desde GitHub con sus patrones de assets
GITHUB_APPS = {
    "zellij": {
        "repo": "zellij-org/zellij",
        "asset_pattern": "x86_64-unknown-linux-musl.tar.gz",
        "binary_name": "zellij"
    },
    "yazi": {
        "repo": "sxyazi/yazi",
        "asset_pattern": "x86_64-unknown-linux-musl.zip",
        "binary_name": "yazi",
        "subpath": "yazi-x86_64-unknown-linux-musl/yazi" # Yazi está dentro de un subdirectorio en el zip
    },
    "lazydocker": {
        "repo": "jesseduffield/lazydocker",
        "asset_pattern": "Linux_x86_64.tar.gz",
        "binary_name": "lazydocker"
    },
    "k9s": {
        "repo": "derailed/k9s",
        "asset_pattern": "Linux_amd64.tar.gz",
        "binary_name": "k9s"
    },
    "lazysql": {
        "repo": "jorgerojas26/lazysql",
        "asset_pattern": "Linux_x86_64.tar.gz",
        "binary_name": "lazysql"
    }
}

def get_latest_release_url(repo, pattern):
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    req = urllib.request.Request(url, headers={"User-Agent": "KaelOS-Installer"})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            for asset in data.get("assets", []):
                if pattern in asset.get("name", ""):
                    return asset.get("browser_download_url"), asset.get("name")
    except Exception as e:
        print(f"Error consultando GitHub API para {repo}: {e}")
    return None, None

def download_file(url, dest):
    print(f"Descargando: {url}...")
    req = urllib.request.Request(url, headers={"User-Agent": "KaelOS-Installer"})
    with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

def extract_binary(archive_path, app_config, extract_dir):
    bin_name = app_config["binary_name"]
    dest_path = os.path.join(BIN_DIR, bin_name)
    
    if archive_path.endswith(".tar.gz"):
        with tarfile.open(archive_path, "r:gz") as tar:
            # Buscar el binario dentro del tar
            member = None
            if "subpath" in app_config:
                member = tar.getmember(app_config["subpath"])
            else:
                for m in tar.getmembers():
                    if m.name == bin_name or m.name.endswith("/" + bin_name):
                        member = m
                        break
            if member:
                # Extraer miembro temporalmente
                tar.extract(member, path=extract_dir)
                src_path = os.path.join(extract_dir, member.name)
                shutil.move(src_path, dest_path)
                return True
    elif archive_path.endswith(".zip"):
        with zipfile.ZipFile(archive_path, "r") as zip_ref:
            member_name = None
            if "subpath" in app_config:
                member_name = app_config["subpath"]
            else:
                for name in zip_ref.namelist():
                    if name == bin_name or name.endswith("/" + bin_name):
                        member_name = name
                        break
            if member_name:
                zip_ref.extract(member_name, path=extract_dir)
                src_path = os.path.join(extract_dir, member_name)
                shutil.move(src_path, dest_path)
                return True
    return False

def main():
    print("=== Instalador de Aplicaciones CLI para Kael OS ===")
    
    # 1. Avisar sobre paquetes de APT necesarios
    print("\n[APT Packages] Por favor ejecuta esto en tu terminal si aún no lo has hecho:")
    print("sudo apt update && sudo apt install -y fish ncdu sqlite3 w3m lazygit docker.io docker-compose\n")
    
    # 2. Descargar e instalar binarios desde GitHub
    for app, config in GITHUB_APPS.items():
        print(f"\nProcesando {app}...")
        
        # Verificar si ya está instalado
        target_path = os.path.join(BIN_DIR, config["binary_name"])
        if os.path.exists(target_path):
            print(f"-> {app} ya está instalado en {target_path}. Saltando.")
            continue
            
        download_url, file_name = get_latest_release_url(config["repo"], config["asset_pattern"])
        if not download_url:
            print(f"-> No se pudo encontrar el URL de descarga para {app}.")
            continue
            
        with tempfile.TemporaryDirectory() as temp_dir:
            archive_dest = os.path.join(temp_dir, file_name)
            try:
                download_file(download_url, archive_dest)
                success = extract_binary(archive_dest, config, temp_dir)
                if success:
                    os.chmod(target_path, 0o755)
                    print(f"-> ¡{app} instalado exitosamente en {target_path}!")
                else:
                    print(f"-> Error al extraer el binario de {app}.")
            except Exception as e:
                print(f"-> Ocurrió un error al instalar {app}: {e}")

    print("\n=== Proceso finalizado ===")

if __name__ == "__main__":
    main()
