from rich.console import Console

CONSOLE = Console()
TIME = ["20ps", "30ps"]
DT = ["1ps", "1ps"]
STEPS = ["20", "30"]
PREFIX = {
    "p": 1e-12,
    "n": 1e-9,
    "u": 1e-6,
    "m": 1e-3,
    "s": 1,
    "K": 1e3,
    "M": 1e6,
    "G": 1e9,
    "None": 1,
    "": 1,
}

TAG = {
    "TIME": "time",
}