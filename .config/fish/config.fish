# Kael OS - Configuración de Fish Shell
# Tema: Cyber-Rasta

# ─── OPCIONES GENERALES ──────────────────────────────────────────────
set -g fish_greeting "" # Desactivar mensaje de bienvenida

# ─── VARIABLES DE ENTORNO Y PATH ──────────────────────────────────────
fish_add_path $HOME/.local/bin
fish_add_path $HOME/scripts
fish_add_path /usr/local/go/bin
fish_add_path $HOME/.cargo/bin

set -gx EDITOR nvim
set -gx VISUAL nvim

# ─── CONFIGURACIÓN DE COLORES (CYBER-RASTA) ───────────────────────────
set -g fish_color_normal e0e0e0
set -g fish_color_command 00e676      # Verde Esmeralda
set -g fish_color_quote ffdf00        # Amarillo/Dorado
set -g fish_color_redirection e0e0e0
set -g fish_color_end e0e0e0
set -g fish_color_error ff3a3a        # Rojo Neón
set -g fish_color_param e0e0e0
set -g fish_color_comment 4e4e54      # Gris/Muted
set -g fish_color_match --background=1a1a1e
set -g fish_color_selection --background=1a1a1e
set -g fish_color_search_match --background=1a1a1e
set -g fish_color_operator 00e5ff     # Cyan
set -g fish_color_escape 00e5ff
set -g fish_color_autosuggestion 4e4e54

# ─── PROMPT CYBER-RASTA ───────────────────────────────────────────────
function fish_prompt
    set -l last_status $status
    set -l status_color (set_color green)
    set -l status_icon "✔"
    if test $last_status -ne 0
        set status_color (set_color red)
        set status_icon "✘ $last_status"
    end

    echo -n (set_color 4e4e54)(date +"%H:%M:%S")" "(set_color green)$USER" "(set_color white)"at "(set_color yellow)(prompt_hostname)" "(set_color white)"in "(set_color blue)(prompt_pwd)
    
    # Git
    if set -l git_prompt (fish_git_prompt)
        echo -n (set_color cyan)"$git_prompt"
    end
    
    echo -e "\n$status_color$status_icon "(set_color cyan)"\$ "(set_color normal)
end

# Personalización del Git prompt de Fish
set -g __fish_git_prompt_showcolorhints yes
set -g __fish_git_prompt_showdirtystate yes

# ─── ALIAS (CONSISTENTES CON ZSH) ─────────────────────────────────────
# Navegación
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."

# LS
if type -q eza
    alias l="eza -l --group --color=always --group-directories-first"
    alias ls="eza -al --group --header --icons --group-directories-first"
    alias ll="eza -la --group --icons --group-directories-first"
    alias la="eza -la --group --icons --group-directories-first"
else if type -q exa
    alias l="exa -l --group --color=always --group-directories-first"
    alias ls="exa -a --group --icons --group-directories-first"
    alias ll="exa -la --group --icons --group-directories-first"
    alias la="exa -la --group --icons --group-directories-first"
else
    alias l="ls -lF"
    alias ll="ls -laF"
    alias la="ls -A"
end

# Sistema
alias df="df -h"
alias du="du -h"
alias free="free -h"
alias top="btop"

# Git
alias g="git"
alias gs="git status"
alias ga="git add"
alias gaa="git add -A"
alias gc="git commit"
alias gcm="git commit -m"
alias gp="git push"
alias gpl="git pull"
alias gl="git log --oneline --graph --decorate"

# Editores
alias v="nvim"
alias vv="nvim ."
alias x="exit"
alias c="clear"
