"""
type() " which type of value store in a varibale.

type casting : to convert one data type value into another data type.
    syntax : datatype(value)

        = int("10")

        = float("10")

        = str(10) // "10"
"""

num1 = input("Enter Number 1 : ")
num2 = input("Enter Number 2 : ")

ans = num1 + num2

print(f"{num1} + {num2} = {ans}")

print(type(num1))

num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

ans = num1 + num2

print(f"{num1} + {num2} = {ans}")
print(type(num1))