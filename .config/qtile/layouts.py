from libqtile import layout
from libqtile.config import Match
from theme import colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo

# Define layouts and layout themes
layout_theme = {
    "margin": 8,
    "border_width": 3,
    "border_focus": colors[3],
    "border_normal": colors[1]
}

# Layout preference by monitor type:
# MonadTall - Default layout (master-stack tiling)
# MonadWide - Rotated monitor (horizontal master-stack tiling)
# Bsp - Dynamic manual splits (fair=False)
# Bsp Fair - Dynamic auto-balanced splits (fair=True)
# Max - Fullscreen focused window
layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Bsp(name="bsp", **layout_theme, fair=False),
    layout.Bsp(name="bsp_fair", **layout_theme, fair=True),
    layout.Max(border_width=0, margin=0),
    layout.Floating(**layout_theme),
]

floating_layout = layout.Floating(
    border_width=4,
    border_focus=colors[3],
    border_normal=colors[1],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="qimgv"),  # q image viewer
        Match(wm_class="nwg-look"),  # nwg-look (GTK theme manager)
        Match(wm_class="pavucontrol"),  # pavucontrol
        Match(wm_class="Galculator"),  # calculator
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="lxpolkit"),  # Polkit authentication agent
        Match(wm_class="arandr"),  # Screen layout editor
        Match(wm_class="feh"),  # image viewer
        Match(wm_class="flameshot"),  # screenshot tool
        Match(title="File Operation Progress"),  # File copy/move progress bars
        
        # Standard X11 window types that should always float
        Match(wm_type="dialog"),
        Match(wm_type="utility"),
        Match(wm_type="toolbar"),
        Match(wm_type="splash"),
        Match(wm_type="notification"),
    ]
)
