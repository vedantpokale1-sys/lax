print("im the boss")


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("that is not a number, try again")


name = input("my name is the vedant")
a = read_number("enter the first number: ")
b = read_number("enter the second number: ")
operator = input("choose the following operator (+, -, *, /): ")
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0:
        print("cannot divide by zero")
    else:
        print(a / b)
else:
    print("invalid operator")

print("this is my calculator")
print("this is for only testing not fina;")
print("im vedant ")
