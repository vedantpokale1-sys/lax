import sys

print("im the boss")


def read_number(prompt):
    while True:
        try:
            raw = input(prompt)
        except EOFError:
            raise SystemExit("no input available, exiting")
        except KeyboardInterrupt:
            raise SystemExit("cancelled by user")
        try:
            return float(raw)
        except ValueError:
            print(f"'{raw}' is not a number, try again", file=sys.stderr)


def calculate(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return a / b
    raise ValueError(f"invalid operator: {operator!r}")


def main():
    a = read_number("enter the first number: ")
    b = read_number("enter the second number: ")
    try:
        operator = input("choose the following operator (+, -, *, /): ")
    except EOFError:
        raise SystemExit("no input available, exiting")
    except KeyboardInterrupt:
        raise SystemExit("cancelled by user")

    try:
        print(calculate(a, b, operator))
    except (ValueError, ZeroDivisionError) as exc:
        print(exc, file=sys.stderr)
        return 1

    print("this is my calculator")
    print("this is for only testing not fina;")
    print("im vedant ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
