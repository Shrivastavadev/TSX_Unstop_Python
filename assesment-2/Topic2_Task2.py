# Task 2: Write a script that takes two numbers as input and prints whether
#         the first number is greater than, less than, or equal to the second number.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
if num1 > num2:
    print(f"Number 1: {num1} is greater than Number2: {num2}")
elif num1 == num2:
    print(f"Number 1: {num1} is equal to the Number2: {num2}")
else:
    print(f"Number 1: {num1} is smaller than Number2: {num2}")