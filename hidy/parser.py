import yaml

from hidy.monitor import Monitor


def parse_config(file):
    config = yaml.load(open(file))
    return Monitor(**config)
