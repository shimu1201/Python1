# when I m adding 18.5 getting error

BMI = float(input("Enter BMI : "))
if BMI < 18.5:
    print("Underweight")
elif BMI > 18.5 and BMI < 25:
    print("Normal")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
else:
    print("Obese")
