#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul ,div


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operat = sys.argv[2]
    b = int(sys.argv[3])

    if operat == "+":
        result = add(a, b)
    elif operat == "-":
        result = sub(a, b)
    elif operat == "*":
        result = mul(a, b)
    elif operat == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operat, b, result))

if __name__ == "__main__":
    main()
    

