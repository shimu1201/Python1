num1 = int(input("Enter Num 1: "))
operator = input("Enter Operator (+, -, *, /, %): ")
num2 = int(input("Enter Num 2: "))

print(f"Number 1 = {num1}, Operator = '{operator}', Number 2 = {num2}")

if operator == '+':
    print(f"Result:", num1 + num2)
elif operator == '-':
    print(f"Result:", num1 - num2)
elif operator == '*':
    print(f"Result:", num1 * num2)
elif operator == '/':
    print(f"Result:", num1 / num2)
elif operator == '%':
    print(f"Result:", num1 % num2)
else:
    print(f"Invalid")
