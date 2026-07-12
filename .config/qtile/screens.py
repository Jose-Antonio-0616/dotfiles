from libqtile.config import Screen
from libqtile import bar
from theme import (
    colors,
    backgroundColor,
    foregroundColor,
    workspaceColor,
    foregroundColorTwo,
)
from widgets import widgets, left_widgets

screens = [
    Screen(
        top=bar.Bar(
            widgets,
            34,
            background=backgroundColor,
            margin=[0, 0, 0, 0],
        ),
        left=bar.Bar(
            left_widgets,
            50,  # Thinner, more compact layout
            background=backgroundColor,
            margin=[0, 0, 0, 0],
        ),
    ),
]
