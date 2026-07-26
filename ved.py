from utils import calculate, print_lines, read_number, read_operator

print("im the boss")
name = input("my name is the vedant")
a = read_number("enter the first number: ")
b = read_number("enter the second number: ")
operator = read_operator("choose the following operator (+, -, *, /): ")
if operator == "/" and b == 0:
    print("cannot divide by zero")
else:
    print(calculate(a, b, operator))

print_lines(
    "this is my calculator",
    "this is for only testing not fina;",
    "im vedant ",
)
