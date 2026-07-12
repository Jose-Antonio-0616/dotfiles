from libqtile import widget
from libqtile.lazy import lazy
import os
import subprocess
from theme import colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo



# Battery status helpers
def get_battery_icon():
    import os
    for bat in ["BAT0", "BAT1"]:
        path = f"/sys/class/power_supply/{bat}"
        if os.path.exists(path):
            try:
                capacity_file = os.path.join(path, "capacity")
                status_file = os.path.join(path, "status")
                if os.path.exists(capacity_file):
                    with open(capacity_file, "r") as f:
                        cap = f.read().strip()
                    cap_int = int(cap)
                    icon = "󰁹"
                    if cap_int < 10:
                        icon = "󰁺"
                    elif cap_int < 20:
                        icon = "󰁻"
                    elif cap_int < 30:
                        icon = "󰁼"
                    elif cap_int < 40:
                        icon = "󰁽"
                    elif cap_int < 50:
                        icon = "󰁾"
                    elif cap_int < 60:
                        icon = "󰁿"
                    elif cap_int < 70:
                        icon = "󰂀"
                    elif cap_int < 80:
                        icon = "󰂁"
                    elif cap_int < 90:
                        icon = "󰂂"
                    
                    if os.path.exists(status_file):
                        with open(status_file, "r") as f:
                            stat = f.read().strip().lower()
                        if "charg" in stat:
                            icon = "󰂄"
                    return icon
            except Exception:
                pass
    try:
        ac_path = "/sys/class/power_supply/AC"
        if os.path.exists(ac_path):
            online_file = os.path.join(ac_path, "online")
            if os.path.exists(online_file):
                with open(online_file, "r") as f:
                    online = f.read().strip()
                if online == "1":
                    return "󰚥"
    except Exception:
        pass
    return ""

def get_battery_percent():
    import os
    for bat in ["BAT0", "BAT1"]:
        path = f"/sys/class/power_supply/{bat}"
        if os.path.exists(path):
            try:
                capacity_file = os.path.join(path, "capacity")
                if os.path.exists(capacity_file):
                    with open(capacity_file, "r") as f:
                        cap = f.read().strip()
                    return f"{cap}%"
            except Exception:
                pass
    try:
        ac_path = "/sys/class/power_supply/AC"
        if os.path.exists(ac_path):
            online_file = os.path.join(ac_path, "online")
            if os.path.exists(online_file):
                with open(online_file, "r") as f:
                    online = f.read().strip()
                if online == "1":
                    return "AC"
    except Exception:
        pass
    return ""

# Updated widget defaults to match Polybar styling
widget_defaults = dict(
    font='Roboto Mono Nerd Font',
    background=backgroundColor,
    foreground=foregroundColor,
    fontsize=16,
    padding=4,
)
extension_defaults = widget_defaults.copy()

# Custom separator to match Polybar
def create_separator():
    return widget.TextBox(
        text="|",
        foreground=foregroundColorTwo,  # disabled color
        padding=8,
        fontsize=14
    )

# List of widgets for the top bar
widgets = [
    # ─── WORKSPACES & APP NAME ──────────────────────────────────────────
    widget.Spacer(length=8),
    
    # Layout indicator (Icon or Text)
    (widget.CurrentLayoutIcon(
        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons/layouts")],
        foreground=colors[6][0],
        scale=0.65,
        padding=4
    ) if hasattr(widget, "CurrentLayoutIcon") else widget.CurrentLayout(
        foreground=colors[6][0],
        padding=4
    )),
    
    create_separator(),
    
    # Workspaces 1-5 (defined dynamically)
    widget.GroupBox(
        disable_drag=True,
        use_mouse_wheel=False,
        active=foregroundColor,
        inactive=foregroundColorTwo,
        highlight_method='line',
        highlight_color=[backgroundColor, backgroundColor],
        this_current_screen_border=colors[3][0], # Emerald Green
        this_screen_border=colors[1][0],
        other_current_screen_border=colors[1][0],
        other_screen_border=backgroundColor,
        urgent_alert_method='text',
        urgent_text=colors[10][0], # Yellow/Gold Alert
        rounded=False,
        margin_x=0,
        margin_y=3,
        padding_x=10,
        padding_y=6,
        borderwidth=3,
        hide_unused=False,
    ),
    
    create_separator(),
    
    # Current active application title
    widget.WindowName(
        format='{name}',
        max_chars=50,
        foreground=foregroundColor,
        padding=6
    ),

    # Spacer to separate left controls from right telemetry
    widget.Spacer(),

    # ─── TELEMETRÍA (CPU, RAM, DISCO, WIFI) ───────────────────────────
    
    # CPU (Rojo)
    widget.TextBox(
        text="󰻠",
        foreground=colors[9][0],  # Neon Red
        padding=6,
        fontsize=18,
    ),
    widget.CPU(
        format="{load_percent:2.0f}%",
        foreground=foregroundColor,
        padding=6
    ),
    
    create_separator(),
    
    # RAM / Memory (Amarillo/Dorado)
    widget.TextBox(
        text="󰍛",
        foreground=colors[6][0],  # Yellow/Gold
        padding=6,
        fontsize=18,
    ),
    widget.Memory(
        format='{MemPercent:2.0f}%',
        foreground=foregroundColor,
        padding=6
    ),
    
    create_separator(),
    
    # Disk (Verde Esmeralda)
    widget.TextBox(
        text="󰋊",
        foreground=colors[3][0],  # Emerald Green
        padding=6,
        fontsize=18,
    ),
    widget.DF(
        visible_on_warn=False,
        format='{r:.0f}%',
        partition='/',
        foreground=foregroundColor,
        padding=6
    ),
    


    create_separator(),

    # ─── HARDWARE & TIEMPO (VOLUMEN, BATERÍA, RELOJ) ─────────────────
    
    # Volumen (Amarillo/Dorado)
    widget.TextBox(
        text="󰕾",
        foreground=colors[6][0],  # Yellow/Gold
        padding=6,
        fontsize=18,
    ),
    widget.Volume(
        fmt="{}",
        mute_command="pamixer -t",
        volume_up_command="pamixer -i 2",
        volume_down_command="pamixer -d 2",
        get_volume_command="pamixer --get-volume-human",
        check_mute_command="pamixer --get-mute",
        check_mute_string="true",
        foreground=foregroundColor,
        padding=6
    ),
    
    create_separator(),
    
    # Batería - Icono (Verde Esmeralda / Dinámico y Seguro)
    widget.GenPollText(
        func=get_battery_icon,
        update_interval=10,
        foreground=colors[3][0],  # Emerald Green
        padding=4,
    ),
    # Batería - Texto (Blanco)
    widget.GenPollText(
        func=get_battery_percent,
        update_interval=10,
        foreground=foregroundColor,
        padding=2,
    ),
    
    create_separator(),
    
    # Fecha (Icon + Text)
    widget.TextBox(
        text="󰃭",
        foreground=colors[3][0],  # Emerald Green
        padding=4,
        fontsize=16,
    ),
    widget.Clock(
        format='%a %b %-d',
        foreground=foregroundColor,
        padding=6,
        mouse_callbacks={'Button1': lazy.spawn('gsimplecal')}
    ),
    
    create_separator(),
    
    # Hora (Icon + Text - Amarillo/Dorado)
    widget.TextBox(
        text="󰅐",
        foreground=colors[6][0],  # Yellow/Gold
        padding=4,
        fontsize=16,
    ),
    widget.Clock(
        format='%-l:%M %p',
        foreground=foregroundColor,  # White
        padding=6,
    ),
    
    create_separator(),

    # ─── ACCIONES Y SYSTRAY ───────────────────────────────────────────
    
    # Indicador de Mayúsculas (Caps Lock)
    widget.GenPollText(
        func=lambda: " CAPS " if "Caps Lock:   on" in subprocess.run(['xset', 'q'], capture_output=True, text=True).stdout else "",
        update_interval=1,
        padding=4,
        foreground=backgroundColor,
        background=colors[10][0],
    ),
    
    # Systray para aplicaciones de fondo (como nm-applet, etc.)
    widget.Systray(
        icon_size=20,
        padding=8,
    ),
    
    # Atajo de Captura de Pantalla
    widget.TextBox(
        text="󰻛",
        foreground=colors[4][0],  # Emerald Green
        padding=10,
        fontsize=18,
        mouse_callbacks={'Button1': lazy.spawn('flameshot gui')}
    ),
    
    # Botón de Apagado
    widget.TextBox(
        text="󰐥",
        foreground=colors[9][0],  # Neon Red
        padding=10,
        fontsize=18,
        mouse_callbacks={'Button1': lazy.spawn(os.path.expanduser('~/.config/qtile/scripts/power'))}
    ),
    
    widget.Spacer(length=8),
]

# ─── LÓGICA Y WIDGETS DE LA BARRA LATERAL (PANEL CONTEXTUAL) ──────────

# Sección 1 - Ventanas Abiertas Helper (Solo Iconos)
def get_open_windows_icons():
    from libqtile import qtile
    if not qtile:
        return "󰖲"
    icon_map = {
        "kitty": "",
        "st": "",
        "firefox-esr": "",
        "firefox": "",
        "brave-browser": "",
        "brave": "",
        "helium": "",
        "thunar": "",
        "geany": "",
        "neovim": "",
        "gimp": "",
        "discord": "󰙯",
        "obs": "",
    }
    class_counts = {}
    for group in qtile.groups:
        if group.name == "scratchpad":
            continue
        for window in group.windows:
            wm_class = window.get_wm_class()
            if wm_class:
                cls = wm_class[0].lower() if isinstance(wm_class, list) else wm_class.lower()
                class_counts[cls] = class_counts.get(cls, 0) + 1
    icons = []
    for cls, count in class_counts.items():
        icon = icon_map.get(cls, "")
        if count > 1:
            icons.append(f"{icon}×{count}")
        else:
            icons.append(icon)
    if icons:
        return "\n".join(icons)
    return "󰖲" # Icono por defecto si no hay ventanas abiertas

# Sección 2 - Almacenamiento Dinámico Helper (Solo Iconos)
def get_mounted_drives_string():
    import os
    media_path = "/media/jose"
    drives = []
    if os.path.exists(media_path):
        for name in os.listdir(media_path):
            if os.path.isdir(os.path.join(media_path, name)):
                icon = "" if "ssd" in name.lower() or "disk" in name.lower() else ""
                drives.append(icon)
    if drives:
        return "\n".join(drives)
    return ""

# Sección 3 - Hardware Activo Helper (Solo Iconos)
def get_active_hardware():
    import subprocess
    perifs = []
    try:
        xinput_res = subprocess.run(["xinput", "list"], capture_output=True, text=True)
        lines = xinput_res.stdout.split("\n")
        has_ext_mouse = False
        has_ext_kbd = False
        for line in lines:
            line_lower = line.lower()
            if "pointer" in line_lower:
                if any(x in line_lower for x in ["usb", "wireless", "bluetooth", "mouse"]) and not "xtest" in line_lower:
                    has_ext_mouse = True
            elif "keyboard" in line_lower:
                if any(x in line_lower for x in ["usb", "wireless", "bluetooth", "keyboard"]) and not any(x in line_lower for x in ["xtest", "virtual", "hp wmi", "power button", "video bus", "at translated"]):
                    has_ext_kbd = True
        if has_ext_mouse:
            perifs.append("󰍽")
        if has_ext_kbd:
            perifs.append("󰌌")
    except Exception:
        pass

    try:
        wpctl_res = subprocess.run(["wpctl", "status"], capture_output=True, text=True)
        lines = wpctl_res.stdout.split("\n")
        in_sinks = False
        for line in lines:
            if "Sinks:" in line:
                in_sinks = True
            elif in_sinks and not line.strip():
                in_sinks = False
            elif in_sinks:
                if any(x in line.lower() for x in ["bluez", "bluetooth", "headphone", "headset", "usb", "auricular"]) and "*" in line:
                    perifs.append("󰋋")
                    break
    except Exception:
        pass
        
    if perifs:
        return "\n".join(perifs)
    return ""

# Sección 4 - Contexto de Desarrollo Helper (Solo Iconos)
def get_dev_context():
    import subprocess
    context = []
    
    # 1. Tmux / Zellij
    try:
        if subprocess.run(["pgrep", "tmux"], capture_output=True).returncode == 0:
            context.append("")
        elif subprocess.run(["pgrep", "zellij"], capture_output=True).returncode == 0:
            context.append("")
    except Exception:
        pass
        
    # 2. Python Venv
    try:
        if subprocess.run(["pgrep", "-f", "/.venv/bin/python"], capture_output=True).returncode == 0 or \
           subprocess.run(["pgrep", "-f", "/venv/bin/python"], capture_output=True).returncode == 0:
            context.append("🐍")
    except Exception:
        pass
        
    # 3. Docker (Check only dockerd daemon to match service status)
    try:
        if subprocess.run(["pgrep", "dockerd"], capture_output=True).returncode == 0:
            context.append("🐳")
    except Exception:
        pass
        
    # 4. Django
    try:
        if subprocess.run(["pgrep", "-f", "manage.py runserver"], capture_output=True).returncode == 0:
            context.append("🌐")
    except Exception:
        pass
        
    if context:
        return "\n".join(context)
    return ""

# Separador vertical
def create_vertical_separator():
    return widget.TextBox(
        text="───",
        foreground=foregroundColorTwo,
        padding=0,
        fontsize=10,
        rotate=False,
    )

# Lista de widgets para la barra lateral izquierda (Panel Contextual)
left_widgets = [
    widget.Spacer(length=16),
    
    # Sección 1 - Ventanas Abiertas (Iconos dinámicos en lista vertical)
    widget.GenPollText(
        func=get_open_windows_icons,
        update_interval=2,
        foreground=colors[3][0],  # Verde Esmeralda
        fontsize=18,
        rotate=False,
        padding=0,
        mouse_callbacks={
            'Button1': lazy.spawn('rofi -show window -theme ~/.config/qtile/rofi/config.rasi')
        }
    ),
    
    widget.Spacer(), # Distribución vertical flexible
    create_vertical_separator(),
    widget.Spacer(), # Distribución vertical flexible
    
    # Sección 2 - Almacenamiento Dinámico (Solo iconos)
    widget.GenPollText(
        func=get_mounted_drives_string,
        update_interval=3,
        foreground=colors[3][0],  # Verde Esmeralda
        fontsize=18,
        rotate=False,
        padding=0,
        mouse_callbacks={
            'Button1': lazy.spawn('thunar'),
            'Button3': lazy.spawn(os.path.expanduser('~/.config/qtile/scripts/manage_drives')),
        }
    ),
    
    widget.Spacer(), # Distribución vertical flexible
    create_vertical_separator(),
    widget.Spacer(), # Distribución vertical flexible
    
    # Sección 3 - Hardware Activo (Solo iconos)
    widget.GenPollText(
        func=get_active_hardware,
        update_interval=4,
        foreground=colors[6][0],  # Amarillo/Dorado
        fontsize=18,
        rotate=False,
        padding=0,
    ),
    
    widget.Spacer(), # Distribución vertical flexible
    create_vertical_separator(),
    widget.Spacer(), # Distribución vertical flexible
    
    # Sección 4 - Contexto de Desarrollo (Solo iconos)
    widget.GenPollText(
        func=get_dev_context,
        update_interval=4,
        foreground=colors[3][0],  # Verde Esmeralda
        fontsize=18,
        rotate=False,
        padding=0,
    ),
    
    widget.Spacer(length=16),
]

