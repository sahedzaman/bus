def calculate(op, n1, n2):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2


operator = input("Choose an operator (+, -, *, /)")
number_one = int(input('Choose a number? '))
number_two = int(input('Choose another number? '))

results = calculate(operator, number_one, number_two )

print(results)

