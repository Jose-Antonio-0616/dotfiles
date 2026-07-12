# Kael OS - Paleta de Colores (Tema Cyber-Rasta)
# Este archivo contiene únicamente la paleta activa oficial del sistema.

def cyber_rasta():
    colors = [
        ["#000000", "#000000"],  # 0: background (oscuro)
        ["#1a1a1e", "#1a1a1e"],  # 1: background-alt
        ["#e0e0e0", "#e0e0e0"],  # 2: foreground
        ["#00e676", "#00e676"],  # 3: secundario/Verde Esmeralda
        ["#00e676", "#00e676"],  # 4: verde
        ["#4e4e54", "#4e4e54"],  # 5: deshabilitado
        ["#ffdf00", "#ffdf00"],  # 6: primario/amarillo-oro
        ["#ff3a3a", "#ff3a3a"],  # 7: Rojo Neón
        ["#1a1a1e", "#1a1a1e"],  # 8: borde
        ["#ff3a3a", "#ff3a3a"],  # 9: rojo
        ["#ffdf00", "#ffdf00"]   # 10: alerta/naranja-oro
    ]
               
    backgroundColor = "#000000"
    foregroundColor = "#e0e0e0"
    workspaceColor = "#00e676"
    foregroundColorTwo = "#4e4e54"
    return colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo
