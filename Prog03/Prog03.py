# Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    sum = num1 + num2
    print(f"The sum of the two numbers is {sum}")


except ValueError:
    print("Please enter a valid number")

