def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("that is not a number, try again")


def calculate(a, b, operator):
    """Return the result of applying operator to a and b, or None if unknown."""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return None


def format_result(a, b, operator):
    if operator == "/" and b == 0:
        return "cannot divide by zero"
    result = calculate(a, b, operator)
    if result is None:
        return "invalid operator"
    return str(result)


def main():
    print("im the boss")
    name = input("my name is the vedant")
    a = read_number("enter the first number: ")
    b = read_number("enter the second number: ")
    operator = input("choose the following operator (+, -, *, /): ")
    print(format_result(a, b, operator))

    print("this is my calculator")
    print("this is for only testing not fina;")
    print("im vedant ", name)


if __name__ == "__main__":
    main()
