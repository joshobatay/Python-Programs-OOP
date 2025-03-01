# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

def sum_of_numbers():
    
    try:
        sum = 0
        for i in range(10):
            num = float(input(f"Enter number {i+1}: "))
            sum +=num
        print(f"The sum of all the numbers is {sum}")
    except ValueError:
        print("Please enter a valid number")

sum_of_numbers()

