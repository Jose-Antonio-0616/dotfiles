from libqtile import layout
from libqtile.config import Match
from theme import colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo

# Define layouts and layout themes
layout_theme = {
    "margin": 5,
    "border_width": 4,
    "border_focus": colors[3],
    "border_normal": colors[1]
}

# Layout preference by monitor type:
# MonadTall - Default layout (master-stack tiling)
# BSP - Traditional monitors (16:9, 4:3)
# Columns - Ultrawide monitors (21:9, 32:9)
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Columns(**layout_theme, num_columns=3),
    layout.Max(**layout_theme),
    layout.TreeTab(
        active_bg=colors[3][0],
        active_fg=backgroundColor,
        inactive_bg=colors[1][0],
        inactive_fg=foregroundColor,
        bg_color=backgroundColor,
        border_width=2,
        font='Roboto Mono Nerd Font',
        fontsize=14,
        panel_width=200,
        sections=['Main'],
        section_fontsize=14,
        section_fg=foregroundColorTwo,
    ),
    layout.Floating(**layout_theme),
    layout.Zoomy(**layout_theme),
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
