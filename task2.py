"""
Accept 5 number from user and calculate total positive numbers and total negative numbers
"""
pos_count = 0
neg_count = 0

for i in range(1,6):
    num = int(input("Enter a Num: "))
    if num > 0:
        pos_count += 1
    else:
        neg_count += 1

print(f"total positive no. are {pos_count}")
print(f"total negative no. are {neg_count}")
