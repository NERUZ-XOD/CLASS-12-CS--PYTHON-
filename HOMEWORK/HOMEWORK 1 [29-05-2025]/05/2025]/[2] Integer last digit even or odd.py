number = int(input("Enter an integer number: "))
last_digit = number % 10
if last_digit % 2 == 0:
    print("The last digit is even.")
else:
    print("The last digit is odd.")