"""
k3color creates colored text on terminal.
"""

from importlib.metadata import version

from .color import (
    Str,
    blue,
    cyan,
    danger,
    dark,
    darkblue,
    darkcyan,
    darkgreen,
    darkpurple,
    darkred,
    darkwhite,
    darkyellow,
    fading_color,
    green,
    loaded,
    normal,
    optimal,
    percentage,
    purple,
    red,
    warn,
    white,
    yellow,
)

__version__ = version("k3color")

__all__ = [
    "Str",
    "blue",
    "cyan",
    "danger",
    "dark",
    "darkblue",
    "darkcyan",
    "darkgreen",
    "darkpurple",
    "darkred",
    "darkwhite",
    "darkyellow",
    "fading_color",
    "green",
    "loaded",
    "normal",
    "optimal",
    "percentage",
    "purple",
    "red",
    "warn",
    "white",
    "yellow",
]
