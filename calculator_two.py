def calculate(op, n1, n2):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2

# results = calculate(operator, number_one, number_two )

# print(results)   

with open ("calc.txt", 'r') as f:
    text_string = f.read().splitlines()
    print("hello")

print (text_string)

