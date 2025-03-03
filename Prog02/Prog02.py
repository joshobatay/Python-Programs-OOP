# Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

try:
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if num1 == num2:
        print('Equal')
    else:
        print('Not Equal')
        
except ValueError:
    print("Please enter a valid number")

