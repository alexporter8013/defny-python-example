from lorrel_py.__about__ import __version__

# import our functions which were defined in Dafny
from lorrel_py.Lorrel.extension import Min, Max, MinMax

__all__ = [
    "__version__",
    "Min",
    "Max",
    "MinMax",
]
