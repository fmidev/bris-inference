import numbers
import os


def expand_time_tokens(string, unixtime):
    # TODO: Implement
    return string

def create_directory(filename):
    """Creates all sub directories necessary to be able to write filename"""
    dir = os.path.dirname(filename)
    if dir != "":
        os.makedirs(dir, exist_ok=True)

def is_number(value):
    return isinstance(value, numbers.Number)
