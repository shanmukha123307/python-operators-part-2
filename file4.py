# Program to identify whether input is a letter or a number

imp = input("Enter a character: ")

if imp.isalpha():
    print("It is a letter.")
elif imp.isdigit():
    print("It is a number.")
else:
    print("It is neither a letter nor a number.")
