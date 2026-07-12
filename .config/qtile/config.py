# Kael OS - Configuración Principal de Qtile
# Archivo maestro que importa los demás módulos

from libqtile import hook, qtile
from libqtile.config import Click, Drag
from libqtile.lazy import lazy
import os
import subprocess

# Importar configuración modular
from keys import keys, mod
from groups import groups
from layouts import layouts, floating_layout
from screens import screens
from widgets import widget_defaults, extension_defaults

# ─── Hooks de Inicio ──────────────────────────────────────────────────

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.run([home])

@hook.subscribe.startup
def set_wallpaper():
    autostart = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    with open(autostart) as f:
        for line in f:
            if 'feh' in line:
                cmd = line.strip().rstrip('&').strip()
                subprocess.Popen(cmd, shell=True)
    set_bar_properties()

# ─── Configuración de Propiedades de las Barras ──────────────────────

def set_bar_properties():
    if not qtile or qtile.core.name != "x11":
        return
    for wid, win in qtile.windows_map.items():
        if win.__class__.__name__ == "Internal":
            try:
                # Establecer WM_CLASS
                win.set_property("WM_CLASS", "qtile-bar\0qtile-bar\0")
                # Establecer _NET_WM_WINDOW_TYPE a _NET_WM_WINDOW_TYPE_DOCK
                atom = qtile.core.conn.atoms["_NET_WM_WINDOW_TYPE_DOCK"]
                win.set_property("_NET_WM_WINDOW_TYPE", [atom])
            except Exception:
                pass

# ─── Controles del Ratón ──────────────────────────────────────────────

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# ─── Opciones Generales de Qtile ──────────────────────────────────────

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "qtile"
