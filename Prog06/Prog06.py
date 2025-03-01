# Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

try:
    base = float(input("Enter the base number: "))
    exponent = float(input("Enter the exponent number: "))
    
    result = base ** exponent
    print(f"The result is {result}")
    
except ValueError:
    print("Please enter a valid number")

