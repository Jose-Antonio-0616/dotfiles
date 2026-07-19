from libqtile.config import Group, Match, ScratchPad, DropDown

groups = [
    Group('1', label="1", layout="bsp_manual"),
    Group('2', label="2", layout="bsp_manual"),
    Group('3', label="3", layout="bsp_manual", matches=[
        Match(wm_class="brave-browser"),
        Match(wm_class="Brave-browser"),
        Match(wm_class="brave-origin"),
        Match(wm_class="Brave-origin")
    ]),
    Group('4', label="4", layout="bsp_manual", screen_affinity=1),
    Group('5', label="5", layout="bsp_manual", screen_affinity=1),
]

# Define scratchpads using Kitty terminal (Cyber-Rasta themed)
groups.append(ScratchPad("scratchpad", [
    DropDown("terminal", "kitty --class=scratchpad", width=0.7, height=0.6, x=0.15, y=0.20, opacity=0.95),
    DropDown("audio", "kitty --class=audio -e pulsemixer", width=0.6, height=0.5, x=0.2, y=0.25, opacity=0.95),
]))
