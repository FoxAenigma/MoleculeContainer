import argparse
import helpers as hp
import sys
from config import TIME, STEPS, DT, PREFIX

### Parser functions

def init_parser():
    parser = argparse.ArgumentParser(description = "Molecule simulator pipeline")
    parser.add_argument(
        '--temp',
        type = float,
        nargs= "+",
        help = "temperatures point in °K",
        required = True
    )

    parser.add_argument(
        '--time',
        type = str,
        nargs = 2,
        default = TIME if hp.check_default() else None,
        help = "time pre/pos equilibrium",
    )

    parser.add_argument(
        '--dt',
        type = str,
        nargs = 2,
        default = DT if hp.check_default() else None,
        help = "simulation sample time",
    )

    parser.add_argument(
        '--steps',
        type = str,
        nargs = 2,
        default = STEPS if hp.check_default() else None,
        help = "simulation steps",
    )

    parser.add_argument(
        '--default',
        nargs = "?",
        default = False,
        const = True,
        help = "set default values to main parameters",
    )
    return parser

# Parser transformations

def fix_arguments(parser):
    if hp.check_default():
        return hp.get_values(parser)
    
    conditions = sum(map(lambda arg: arg.startswith("--"), sys.argv)) - 1
    if conditions < 2:
        sys.exit("Number of temporal conditions less than 2, need more data")
    
    state = hp.get_values(parser)
    for param in state.keys():
        if state[param] == None:
            state[param] = hp.compute_param(parser, param)
    return state

