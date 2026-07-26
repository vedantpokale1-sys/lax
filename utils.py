"""Shared helpers used by the scripts in this repo."""

import operator
import sys

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def read_text(prompt):
    """Read a line, turning a closed or interrupted stdin into a clean exit."""
    try:
        return input(prompt)
    except EOFError:
        raise SystemExit("no input available, exiting")
    except KeyboardInterrupt:
        raise SystemExit("cancelled by user")


def read_number(prompt):
    """Ask for a number until the answer can be parsed as a float."""
    while True:
        raw = read_text(prompt)
        try:
            return float(raw)
        except ValueError:
            print(f"'{raw}' is not a number, try again", file=sys.stderr)


def calculate(a, b, symbol):
    """Apply the operator named by `symbol` to `a` and `b`."""
    if symbol not in OPERATIONS:
        raise ValueError(f"invalid operator: {symbol!r}")
    if symbol == "/" and b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return OPERATIONS[symbol](a, b)


def print_lines(*lines):
    for line in lines:
        print(line)
