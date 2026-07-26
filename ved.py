import sys

from utils import calculate, print_lines, read_number, read_text

print("im the boss")


def main():
    read_text("my name is the vedant")
    a = read_number("enter the first number: ")
    b = read_number("enter the second number: ")
    operator = read_text("choose the following operator (+, -, *, /): ")

    try:
        print(calculate(a, b, operator))
    except (ValueError, ZeroDivisionError) as exc:
        print(exc, file=sys.stderr)
        return 1

    print_lines(
        "this is my calculator",
        "this is for only testing not fina;",
        "im vedant ",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
