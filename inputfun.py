"""
There are two types of values

1) static values : fix value
2) dynamic values : at run time accept from user

for dynamic values :

input() : input is a function which is used to accpet value from user at run time.

    syntax :

        input("prompt message")

    note : by default input function accept value in string format.

    string means ("")
"""

name = input("Enter your Name :")

print(f"My name is {name}")