"""
Accept 5 numbers from user and calculate even nos sum and odd nos sum
"""
even_sum = 0
odd_sum = 0

for i in range(1,6):
    num = int(input("Enter a Num : "))

    if num %2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"total even no. are {even_sum}")
print(f"total odd no. are {odd_sum}")