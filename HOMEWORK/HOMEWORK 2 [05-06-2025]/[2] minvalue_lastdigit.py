''' [2] Write a function that takes two numbers and returns the number that has minimum 
        value in the last digit.                                                                  '''

def lastdigit_minvalue(a,b):
    l1 = a % 10
    l2 = b % 10
    if l1 < l2:
        return a
    elif l1 > l2:
        return b
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
result = lastdigit_minvalue(number1, number2)
print("The number with the smaller last digit is:", result)