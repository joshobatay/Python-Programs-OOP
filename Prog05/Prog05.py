# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point

def division():
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        quotient = num1 / num2
        print(f"The quotient of the two numbers is {quotient}")
    
    
    except ValueError:
        print("Please enter a valid number")
        
division()