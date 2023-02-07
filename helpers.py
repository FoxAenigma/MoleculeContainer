import sys
from config import PREFIX

def compute_param(parser, param):
    if param == "time":
        return [
            string_val(numeric_val(get_param(parser, "steps")[0])*numeric_val(get_param(parser, "dt")[0])),
            string_val(numeric_val(get_param(parser, "steps")[1])*numeric_val(get_param(parser, "dt")[1])),
        ]
    if param == "steps":
        return [
            string_val(round(numeric_val(get_param(parser, "time")[0])/numeric_val(get_param(parser, "dt")[0])), unit=''),
            string_val(round(numeric_val(get_param(parser, "time")[1])/numeric_val(get_param(parser, "dt")[1])), unit='')
        ]
    if param == "dt":    
        return [
            string_val(numeric_val(get_param(parser, "time")[0])/numeric_val(get_param(parser, "steps")[0])),
            string_val(numeric_val(get_param(parser, "time")[1])/numeric_val(get_param(parser, "steps")[1]))
        ]


def check_default():
    if "--default" in sys.argv:
        return True
    return False

def get_values(parser):
    configurables = [x for x in dir(parser.parse_args()) if not x.startswith('_')]
    values = [getattr(parser.parse_args(), conf) for conf in configurables]
    return dict(zip(configurables, values))

def get_param(parser, label):
    return getattr(parser.parse_args(), label)

def numeric_val(n):
    composition = split_val(n)
    val = float(composition[0])
    unit = composition[-1][0] if len(composition[-1]) > 1 else ""
    return val*PREFIX[unit]

def string_val(n, unit="ps"):
        reg = unit[0] if len(unit) > 0 else unit
        return f"{n*PREFIX[reg]}{unit}"

def split_val(n):
    composition = (n, '')
    for i in range(len(n)):
        if not (n[i].isnumeric() or n[i]=='.'):
            composition = (n[:i-1], n[i-1:])
    return composition
    