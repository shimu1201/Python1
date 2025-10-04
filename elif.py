"""
elif statement ::: when there are multiple conditions

syntax :

if condition:
    statement
elif condition:
    statement
elif condition:
    statement
else:
    statement
"""
marks = int(input("Enter your marks :"))
if marks >= 70:
    print("A Garde")
elif marks >= 60 and marks <70:
    print("B Garde")
elif marks >= 50 and marks <60:
    print("C Garde")
elif marks >= 40 and marks <50:
    print("D Garde")
else:
    print("Fail")