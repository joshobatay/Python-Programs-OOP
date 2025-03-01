# Create a program that ask user to input 10 numbers. Print how many are odd numbers.
'''
def print_odd_numbers():
    
    try:
        sum = 0
        for i in range(10):
            num = float(input("Enter a number: "))
            
print_odd_numbers()


'''
'''
def count_odd_numbers():
    odd_count = 0 

    for i in range(10):  
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))  
                if num % 2 != 0:  
                    odd_count += 1  
                break  
            except ValueError:
                print("Invalid input! Please enter an integer.")

    print(f"The number of odd numbers entered is {odd_count}")


count_odd_numbers()

'''


# Count odd numbers from 10 user inputs
odd_count = sum(1 for _ in range(10) if int(input("Enter a number: ")) % 2 != 0)

print("Total odd numbers:", odd_count)
