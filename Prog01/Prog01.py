# Create a program that ask user to input 2 numbers. Print the bigger number.


def print_number():
    
    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if num1 > num2:
            print("The bigger number is", num1)
        else:
            print("The bigger number is", num2)
            
    except ValueError:
        print("Please enter a valid number")

print_number()