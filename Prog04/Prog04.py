# Create a program that ask user to input 2 numbers. Print the product of the two numbers.

# Create a program that ask user to input 2 numbers. Print the sum of the two numbers.

def multiplication():
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        product = num1 * num2
        print(f"The sum of the two numbers is {product}")
    
    
    except ValueError:
        print("Please enter a valid number")

multiplication()