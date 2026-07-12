from libqtile.config import Group, Match, ScratchPad, DropDown

groups = [
    Group('1', label="1", layout="monadtall"),
    Group('2', label="2", layout="monadtall", matches=[
        Match(wm_class="geany"),
        Match(wm_class="fresh")
    ]),
    Group('3', label="3", layout="monadtall", matches=[
        Match(wm_class="firefox"),
        Match(wm_class="firefox-esr")
    ]),
    Group('4', label="4", layout="monadtall", matches=[
        Match(wm_class="thunar"),
        Match(wm_class="mpv")
    ]),
    Group('5', label="5", layout="monadtall", matches=[
        Match(wm_class="discord"),
        Match(wm_class="Discord")
    ]),
]

# Define scratchpads using Kitty terminal (Cyber-Rasta themed)
groups.append(ScratchPad("scratchpad", [
    DropDown("terminal", "kitty --class=scratchpad", width=0.7, height=0.6, x=0.15, y=0.02, opacity=0.95),
    DropDown("audio", "kitty --class=audio -e pulsemixer", width=0.6, height=0.5, x=0.2, y=0.02, opacity=0.95),
]))
