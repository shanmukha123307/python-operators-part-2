hight=float(input("enter your hight in cm"))
weight=float(input("enter your weight in kg"))
bmi=weight/(hight/100)**2
print("your bmi is",bmi)
if bmi<=18.4:
    print(" you are under weight")
elif bmi<=24.9:
    print("you'r helthey")
elif bmi<=29.9:
    print("your over weight")
elif bmi<=34.9:
    print("you are severlery over weight")
elif bmi<=39.9:
    print("you are obese")
else:
    print("you are severly obese")