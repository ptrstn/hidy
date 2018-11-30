import argparse
import subprocess

from hidy.configurator import Configurator
from hidy.parser import parse_config


def parse_arguments():
    parser = argparse.ArgumentParser(description="A multi monitor high dpi display configurator")

    parser.add_argument(
        "configs", metavar="monitor", nargs="+", help="monitor configuration files"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()
    monitors = [parse_config(config) for config in args.configs]
    configurator = Configurator(*monitors)
    command = configurator.xrandr_command()
    print(command)
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    main()
