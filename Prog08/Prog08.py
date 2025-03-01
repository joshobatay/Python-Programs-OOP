# Create a program that ask user to input 10 numbers. Print how many are odd numbers.

'''

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



'''

