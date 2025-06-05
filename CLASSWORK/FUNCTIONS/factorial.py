# Function to get factorial of a number

def factorial(n):                                   # Function header
    factorial = 1
    for i in range(1,n + 1):
        factorial *= i                              # Function body
    return factorial

number = int(input("Enter the number : "))
print("Factorial of",number,"is",factorial(number))