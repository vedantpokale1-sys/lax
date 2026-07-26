"""Shared helpers used by the scripts in this repo."""

import operator

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def read_int(prompt):
    """Ask for a number until the answer can be parsed as an int."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("that is not a whole number, try again")


def read_operator(prompt):
    """Ask for one of the supported operators until a valid one is given."""
    while True:
        symbol = input(prompt).strip()
        if symbol in OPERATIONS:
            return symbol
        print("invalid operator")


def calculate(a, b, symbol):
    """Apply the operator named by `symbol` to `a` and `b`."""
    return OPERATIONS[symbol](a, b)


def print_lines(*lines):
    for line in lines:
        print(line)
