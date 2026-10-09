"""
k3color creates colored text on terminal.
"""

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


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3color")
