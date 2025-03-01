# Create a program that ask user to input 2 numbers. Print the product of the two numbers.

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    product = num1 * num2
    print(f"The product of the two numbers is {product}")


except ValueError:
    print("Please enter a valid number")

