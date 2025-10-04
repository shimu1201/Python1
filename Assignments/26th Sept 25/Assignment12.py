balance = int(input("Enter your account balance : "))
withdrawal = int(input("Enter your withdrawal amount : "))

daily_limit = 30000

if withdrawal <= balance:
    if withdrawal <= daily_limit:
        balance -= withdrawal
        print(f"Withdrawal successful! New balance: {balance}")
    else:
        print(f"Withdrawal amount exceeds daily limit.")
else:
    print("Insufficient balance.")
