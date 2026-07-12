from libqtile.config import Key
from libqtile.lazy import lazy
import os
import subprocess
from groups import groups

mod = "mod4"
terminal = "kitty"
browser = "firefox-esr"

def notify_layout():
    """Show current layout in notification"""
    def _notify_layout(qtile):
        layout_name = qtile.current_group.layout.name
        layout_map = {
            "monadtall": "Monad Tall",
            "columns": "Columns", 
            "bsp": "BSP",
            "treetab": "Tree Tab",
            "matrix": "Matrix",
            "plasma": "Plasma",
            "floating": "Floating",
            "spiral": "Spiral",
            "ratiotile": "Ratio Tile",
            "max": "Maximized",
            "monadwide": "Monad Wide",
            "tile": "Tile",
            "verticaltile": "Vertical Tile",
            "stack": "Stack",
            "zoomy": "Zoomy"
        }
        display_name = layout_map.get(layout_name, layout_name.title())
        subprocess.run(["notify-send", "Layout", display_name, "-t", "1500", "-u", "low"])
    return _notify_layout

def notify_restart():
    """Show restart notification"""
    def _notify_restart(qtile):
        subprocess.run(["notify-send", "Qtile", "Restarting...", "-t", "2000", "-u", "normal"])
    return _notify_restart

def toggle_float_center():
    """Toggle floating and center at 75% size"""
    def _toggle_float_center(qtile):
        window = qtile.current_window
        if window:
            was_floating = window.floating
            window.toggle_floating()
            if not was_floating and window.floating:
                # Only resize/center when going from tiled to floating
                screen = qtile.current_screen
                width = int(screen.width * 0.70)
                height = int(screen.height * 0.60)
                window.set_size_floating(width, height)
                window.center()
    return _toggle_float_center

def resize_left():
    """Resize window left - intuitive based on focus"""
    def _resize_left(qtile):
        if not qtile.current_window:
            return
        layout_name = qtile.current_layout.name
        group = qtile.current_group

        if layout_name in ["bsp", "columns"]:
            qtile.current_layout.grow_left()
        elif layout_name in ["monadtall", "monadwide", "tile", "ratiotile"]:
            current_idx = group.windows.index(qtile.current_window)
            if current_idx == 0:
                qtile.current_layout.shrink()
            else:
                qtile.current_layout.grow()
        else:
            qtile.current_layout.shrink()
    return _resize_left

def resize_right():
    """Resize window right - intuitive based on focus"""
    def _resize_right(qtile):
        if not qtile.current_window:
            return
        layout_name = qtile.current_layout.name
        group = qtile.current_group

        if layout_name in ["bsp", "columns"]:
            qtile.current_layout.grow_right()
        elif layout_name in ["monadtall", "monadwide", "tile", "ratiotile"]:
            current_idx = group.windows.index(qtile.current_window)
            if current_idx == 0:
                qtile.current_layout.grow()
            else:
                qtile.current_layout.shrink()
        else:
            qtile.current_layout.grow()
    return _resize_right

def focus_left():
    """Focus window to the left, or cycle if floating"""
    def _focus_left(qtile):
        if not qtile.current_window:
            return
        if qtile.current_layout.name == "floating" or qtile.current_window.floating:
            qtile.current_group.prev_window()
        else:
            qtile.current_layout.left()
    return _focus_left

def focus_right():
    """Focus window to the right, or cycle if floating"""
    def _focus_right(qtile):
        if not qtile.current_window:
            return
        if qtile.current_layout.name == "floating" or qtile.current_window.floating:
            qtile.current_group.next_window()
        else:
            qtile.current_layout.right()
    return _focus_right

def toggle_treetab():
    """Toggle between TreeTab (qtile's closest thing to bspwm-tabs) and MonadTall"""
    def _toggle_treetab(qtile):
        group = qtile.current_group
        target = "monadtall" if group.layout.name == "treetab" else "treetab"
        group.setlayout(target)
        subprocess.run(["notify-send", "Layout",
                        "Tree Tab" if target == "treetab" else "Monad Tall",
                        "-t", "1500", "-u", "low"])
    return _toggle_treetab


keys = [
# === WM CONTROL ===
    Key([mod], "q", lazy.window.kill(), desc="Close focused window"),
    Key([mod, "shift"], "r", lazy.function(notify_restart()), lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Exit Qtile"),
    Key([mod], "x", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/power")), desc="Power menu"),

# === LAUNCH ===
    Key([mod], "space", lazy.spawn("rofi -show drun -modi drun -line-padding 4 -hide-scrollbar -show-icons -theme ~/.config/qtile/rofi/config.rasi"), desc="Launch Rofi"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod, "shift"], "b", lazy.spawn(browser + " -private-window"), desc="Launch browser (private)"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch GUI file manager (Thunar)"),
    
    # TUI Dev & Tooling Stack
    Key([mod], "v", lazy.spawn("kitty -e nvim"), desc="Launch Neovim"),
    Key([mod, "shift"], "v", lazy.spawn("kitty -e fresh"), desc="Launch Fresh TUI editor"),
    Key([mod], "y", lazy.spawn("kitty -e yazi"), desc="Launch Yazi TUI file manager"),
    Key([mod], "z", lazy.spawn("kitty -e zellij"), desc="Launch Zellij multiplexer"),
    Key([mod], "g", lazy.spawn("kitty -e lazygit"), desc="Launch Lazygit"),
    Key([mod], "d", lazy.spawn("kitty -e lazydocker"), desc="Launch Lazydocker"),
    Key([mod], "s", lazy.spawn("kitty -e lazysql"), desc="Launch Lazysql"),
    Key([mod, "shift"], "s", lazy.spawn("kitty -e lazyssh"), desc="Launch Lazyssh"),
    Key([mod, "mod1"], "k", lazy.spawn("kitty -e k9s"), desc="Launch k9s Kubernetes TUI"),

    Key([mod], "o", lazy.spawn("obs"), desc="Launch OBS"),
    Key([mod], "slash", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/help")), desc="Show keybindings"),
    Key([mod, "shift"], "t", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/thememenu")), desc="Theme switcher"),

# === WINDOW NAVIGATION ===
    Key([mod], "Left", lazy.function(focus_left()), desc="Focus left"),
    Key([mod], "h", lazy.function(focus_left()), desc="Focus left"),
    Key([mod], "Right", lazy.function(focus_right()), desc="Focus right"),
    Key([mod], "l", lazy.function(focus_right()), desc="Focus right"),
    Key([mod], "Up", lazy.layout.up(), desc="Focus up"),
    Key([mod], "k", lazy.layout.up(), desc="Focus up"),
    Key([mod], "Down", lazy.layout.down(), desc="Focus down"),
    Key([mod], "j", lazy.layout.down(), desc="Focus down"),
    Key(["mod1"], "Tab", lazy.group.next_window(), desc="Alt-Tab cycle windows"),

# === WINDOW MOVE/SWAP ===
    Key([mod, "shift"], "Left",  lazy.layout.shuffle_left(),  lazy.layout.swap_left(),  desc="Swap window left"),
    Key([mod, "shift"], "h",     lazy.layout.shuffle_left(),  lazy.layout.swap_left(),  desc="Swap window left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), lazy.layout.swap_right(), desc="Swap window right"),
    Key([mod, "shift"], "l",     lazy.layout.shuffle_right(), lazy.layout.swap_right(), desc="Swap window right"),
    Key([mod, "shift"], "Up",    lazy.layout.shuffle_up(),    desc="Swap window up"),
    Key([mod, "shift"], "k",     lazy.layout.shuffle_up(),    desc="Swap window up"),
    Key([mod, "shift"], "Down",  lazy.layout.shuffle_down(),  desc="Swap window down"),
    Key([mod, "shift"], "j",     lazy.layout.shuffle_down(),  desc="Swap window down"),

# === WINDOW RESIZE ===
    Key([mod, "control"], "Left",  lazy.function(resize_left()),  desc="Resize window left"),
    Key([mod, "control"], "h",     lazy.function(resize_left()),  desc="Resize window left"),
    Key([mod, "control"], "Right", lazy.function(resize_right()), desc="Resize window right"),
    Key([mod, "control"], "l",     lazy.function(resize_right()), desc="Resize window right"),
    Key([mod, "control"], "Up",    lazy.layout.grow_up(),   lazy.layout.grow(),   lazy.layout.decrease_nmaster(), desc="Grow window up"),
    Key([mod, "control"], "k",     lazy.layout.grow_up(),   lazy.layout.grow(),   lazy.layout.decrease_nmaster(), desc="Grow window up"),
    Key([mod, "control"], "Down",  lazy.layout.grow_down(), lazy.layout.shrink(), lazy.layout.increase_nmaster(), desc="Grow window down"),
    Key([mod, "control"], "j",     lazy.layout.grow_down(), lazy.layout.shrink(), lazy.layout.increase_nmaster(), desc="Grow window down"),
    Key([mod, "control"], "equal", lazy.layout.normalize(), desc="Reset all window sizes"),

# === LAYOUTS ===
    Key([mod], "Tab", lazy.next_layout(), lazy.function(notify_layout()), desc="Cycle layouts"),
    Key([mod], "t", lazy.layout.toggle_split(), desc="Toggle split direction (BSP)"),
    Key([mod], "w", lazy.function(toggle_treetab()), desc="Toggle tab group (TreeTab)"),
    Key([mod, "shift"], "y", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/layoutmenu")), desc="Layout menu"),

# === WINDOW STATE ===
    Key([mod, "shift"], "space", lazy.function(toggle_float_center()), desc="Toggle floating, center"),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),

# === SCRATCHPADS ===
    Key([mod, "shift"], "Return", lazy.group['scratchpad'].dropdown_toggle('terminal'), desc="Toggle terminal scratchpad"),
    Key([mod, "mod1"], "a", lazy.group['scratchpad'].dropdown_toggle('audio'), desc="Toggle audio scratchpad"),

# === MEDIA & BRIGHTNESS ===
    Key([mod], "F12", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/changevolume up")), desc="Volume up"),
    Key([mod], "F11", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/changevolume down")), desc="Volume down"),
    Key([mod], "F10", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/changevolume mute")), desc="Mute/Unmute"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/changevolume up")), desc="Volume up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/changevolume down")), desc="Volume down"),
    Key([], "XF86AudioMute", lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/changevolume mute")), desc="Mute/Unmute"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%"), desc="Brightness up"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"), desc="Brightness down"),

# === SCREENSHOTS ===
    Key([], "Print", lazy.spawn("flameshot full --path " + os.path.expanduser("~/Screenshots/")), desc="Screenshot (full)"),
    Key([mod], "Print", lazy.spawn("flameshot gui --path " + os.path.expanduser("~/Screenshots/")), desc="Screenshot (region)"),
]

# Switch to groups key bindings
for i in groups:
    if i.name != "scratchpad":  # Skip scratchpad groups
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                ),
            ]
        )
