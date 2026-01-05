print("SIMPLE CALCULATOR")

num1, num2 = map(int, input("Enter two numbers: ").split())

sign = input("Enter an operator(e.g: +, -, *, /): ")

if sign == '+':
    print(f"Addition: {num1 + num2}")
elif sign == '-':
    print(f"Substraction: {num1 - num2}")
elif sign == '*':
    print(f"Multiplication: {num1 * num2}")
elif sign == "/":
    print(f"Division: {num1 / num2}")
else:
    print("Invalid Operator!!!")