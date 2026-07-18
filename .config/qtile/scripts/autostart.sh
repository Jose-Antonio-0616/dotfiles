#!/bin/sh

# polkit
lxpolkit &

# monitor resolution and layout
if xrandr | grep -q "HDMI-1 connected"; then
    xrandr --output LVDS-1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI-1 --mode 1920x1080 --right-of LVDS-1 --rotate normal
else
    xrandr --output LVDS-1 --primary --mode 1366x768 --pos 0x0 --rotate normal
fi

# background
feh --bg-center --image-bg black /home/jose/.config/qtile/wallpaper/rasta_1.jpeg &

# GTK live theme updates
xsettingsd &

# compositor
picom --config ~/.config/qtile/picom/picom.conf -b &

# Notifications
dunst -config ~/.config/qtile/dunst/dunstrc &

# WIFI
nm-applet &

# Automount USB
udiskie &

# First-login welcome (shown once, dismissable)
if [ ! -f "$HOME/.cache/qtile/welcomed" ]; then
    mkdir -p "$HOME/.cache/qtile"
    touch "$HOME/.cache/qtile/welcomed"
    (
        sleep 3
        notify-send -u normal -t 15000 \
            "Welcome to Qtile" \
            "Press Super + / anytime to see all keybindings.&#10;See ~/QUICKSTART-qtile.md for a cheat sheet."
    ) &
fi

# Run pending updates checker
check-updates &

# Bloqueo automático de pantalla (15 minutos = 900 segundos)
# xset configura el temporizador de inactividad y apaga el monitor
xset s 900
xset dpms 900 900 900
# xss-lock escucha los eventos de inactividad (y suspensión de logind) para lanzar kael-lock
xss-lock -l -- ~/.config/qtile/scripts/kael-lock &
