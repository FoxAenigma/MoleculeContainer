from transformation import init_parser, fix_arguments
from entities import MoleculeContainer
from config import CONSOLE

if __name__ == "__main__":
    parser = init_parser()
    values = fix_arguments(parser)
    for temp in values["temp"]:
        container = MoleculeContainer(console=CONSOLE, temp=temp, conditions=values)
        container.make_workspace()
    