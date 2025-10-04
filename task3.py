"""
Accept 5 numbers from user and calculate total even nos are there and total odd numbers are there
"""
even_count = 0
odd_count = 0

for i in range(1,6):
    num = int(input("Enter a Num : "))

    if num %2 == 0:
        print("even")
    else:
        print("odd")

print(f"total even no. are {even_count}")
print(f"total odd no. are {odd_count}")