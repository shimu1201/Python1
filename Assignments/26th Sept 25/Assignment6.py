num = int(input("Enter a number : "))
if num%3 == 0 and num%5 == 0:
    print(f"Divisible by both", {num})
elif num%3 == 0:
    print(f"Divisible by 3", {num})
else:
    print(f"Divisible by 5", {num})