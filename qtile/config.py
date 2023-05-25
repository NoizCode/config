######################################################################

#       __        _               ___            _  _                #
#    /\ \ \ ___  (_) ____        / __\ ___    __| |(_) _ __    __ _  #
#   /  \/ // _ \ | ||_  /_____  / /   / _ \  / _` || || '_ \  / _` | #
#  / /\  /| (_) || | / /|_____|/ /___| (_) || (_| || || | | || (_| | #
#  \_\ \/  \___/ |_|/___|      \____/ \___/  \__,_||_||_| |_| \__, | #
#                                                             |___/  #

######################################################################

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

mod = "mod4"
terminal = guess_terminal()

powerline = {
        "decorations": [
            PowerLineDecoration(path="forward_slash",
                                size=7)
        ]
}

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "m", lazy.window.toggle_maximize(), desc="Toggle maximize windows"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("dmenu_run"), desc="launch dmenu"),
    Key([mod], "s", lazy.spawn("xfce4-settings-manager"), desc="settings"),

    #### APPS ####
    Key([mod], "b", lazy.spawn("brave"), desc="Launches brave browser"),
    Key([mod], "c", lazy.spawn("codium"), desc="open vscode"),
    Key([mod], "q", lazy.spawn("pcmanfm"), desc="open file explorer"),

    # Toggle keyboard layout
    Key([mod],"f11", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout"),

    # Media
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc="Lower Volume by 5%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc="Raise Volume by 5%")
]

groups = [Group(i) for i in "1234"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Tile(
        margin = 12,
        border_focus="51E0F0",
        border_width=2),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="/home/noisefuck/Pictures/blue1.jpeg",
        wallpaper_mode='fit',
        top=bar.Bar(
            [
                widget.GroupBox(font="sans Bold",
                                this_current_screen_border="51E0F0",
                                border_width=20),
                widget.Prompt(),
                widget.WindowName(foreground="51E0F0",
                                  font="sans Bold"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Battery(background=["1F1F1F"], # Just to create the last arrow effect
                               foreground="131313",
                               fontsize=0.1,
                               **powerline),
                widget.CheckUpdates(distro='Arch_checkupdates',
                                    update_interval=1800,
                                    display_format="🗘 : {updates}",
                                    no_update_string="🗘 : 0",
                                    font="sans Bold",
                                    colour_no_updates="FFFFFF",
                                    foreground="FFFFFF",
                                    background="51E0F0",
                                    **powerline),
                widget.CPU(format="    {freq_current}GHz {load_percent}%",
                           foreground="FFFFFF",
                           background="5180F0",
                           font="sans Bold",
                           **powerline),
                widget.Memory(measure_mem='G',
                              foreground="FFFFFF",
                              background="51E0F0",
                              font="sans Bold",
                              **powerline),
                widget.Net(interface="enp8s0",
                             format='↑{up} ↓{down}',
                             foreground="FFFFFF",
                             background="5180F0",
                             font="sans Bold",
                             **powerline),
                widget.Clock(format="%d-%m %a %I:%M %p",
                             foreground="FFFFFF",
                             background="51E0F0",
                             font="sans Bold",
                             **powerline),
                widget.PulseVolume(foreground="FFFFFF",
                                   background="5180F0",
                                   font="sans Bold",
                                   **powerline),
                widget.KeyboardLayout(configured_keyboards=['us','gr'],
                                      foreground="FFFFFF",
                                      font="sans Bold",
                                      background="51E0F0",
                                      **powerline),
            ],
            22, background=["1F1F1F"],
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"

######################################################################

#       __        _               ___            _  _                #
#    /\ \ \ ___  (_) ____        / __\ ___    __| |(_) _ __    __ _  #
#   /  \/ // _ \ | ||_  /_____  / /   / _ \  / _` || || '_ \  / _` | #
#  / /\  /| (_) || | / /|_____|/ /___| (_) || (_| || || | | || (_| | #
#  \_\ \/  \___/ |_|/___|      \____/ \___/  \__,_||_||_| |_| \__, | #
#                                                             |___/  #

######################################################################
